#!/usr/bin/env python3
"""Static operation reporter for PolyBench C kernels.

This tool recursively scans C files, preprocesses macros, performs a static AST walk,
and emits numeric operation counts per function and per file.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape

RUNTIME_DEPENDENCIES = {
    "pycparser": "pycparser",
    "reportlab": "reportlab",
}

EXCLUDED_DIR_NAMES = {
    ".git",
    ".github",
    ".venv",
    "__pycache__",
    "op_reporter",
    ".pytest_cache",
}

DATASET_FLAG_BY_NAME = {
    "MINI": "MINI_DATASET",
    "SMALL": "SMALL_DATASET",
    "MEDIUM": "MEDIUM_DATASET",
    "LARGE": "LARGE_DATASET",
    "EXTRALARGE": "EXTRALARGE_DATASET",
}

DEFAULT_REPORTER_CONFIG = {
    "dataset": "MEDIUM",
    "strict_static": False,
    "llvm_validate": False,
    "master_name": "op_reporter_master_report.md",
    "suffix": "operations",
    "requirements_file": "op_reporter/requirements.txt",
    "no_auto_install": False,
}

CONFIG_REQUIRED_KEYS = {"target"}
CONFIG_ALLOWED_KEYS = CONFIG_REQUIRED_KEYS | set(DEFAULT_REPORTER_CONFIG)

OPERATION_ORDER = [
    "assign",
    "add",
    "sub",
    "mul",
    "mul_const",
    "div",
    "div_const",
    "mod",
    "cmp",
    "logical",
    "bitwise",
    "unary",
    "if",
    "loop_for",
    "call",
]


@dataclass
class FunctionReport:
    name: str
    counts: Counter
    width_counts: dict[str, Counter]
    callees: set[str]
    unresolved_loops: list[str] = field(default_factory=list)


@dataclass
class FileReport:
    c_path: Path
    report_md: Path
    report_pdf: Path
    report_csv: Path
    functions: list[FunctionReport]
    totals: Counter
    width_totals: dict[str, Counter]
    unresolved: list[str]
    llvm_counts: Counter


class StaticCountingError(RuntimeError):
    """Raised when static counting constraints are violated in strict mode."""


def ensure_runtime_dependencies(requirements_path: Path, auto_install: bool) -> None:
    missing: list[str] = []
    for package_name, import_name in RUNTIME_DEPENDENCIES.items():
        if importlib.util.find_spec(import_name) is None:
            missing.append(package_name)

    if not missing:
        return

    if auto_install:
        cmd = [sys.executable, "-m", "pip", "install", *missing]
        subprocess.run(cmd, check=True)
        update_requirements_file(requirements_path, missing)
        return

    raise RuntimeError(
        "Missing runtime packages: "
        + ", ".join(missing)
        + f". Install with: {sys.executable} -m pip install -r {requirements_path}"
    )


def update_requirements_file(requirements_path: Path, packages: list[str]) -> None:
    requirements_path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[str] = []
    if requirements_path.exists():
        existing = [line.strip() for line in requirements_path.read_text().splitlines() if line.strip()]

    merged = sorted(set(existing) | set(packages))
    requirements_path.write_text("\n".join(merged) + "\n")


def pick_cpp_tool() -> str:
    for candidate in ["clang", "gcc", "cpp"]:
        if shutil_which(candidate):
            return candidate
    raise RuntimeError("No C preprocessor found (clang/gcc/cpp).")


def shutil_which(command: str) -> str | None:
    result = subprocess.run(
        ["bash", "-lc", f"command -v {command}"],
        capture_output=True,
        text=True,
        check=False,
    )
    found = result.stdout.strip()
    return found or None


def discover_c_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.c"):
        if any(part in EXCLUDED_DIR_NAMES for part in path.parts):
            continue
        if path.name.endswith(".orig.c"):
            continue
        if path.name == "template-for-new-benchmark.c":
            continue
        files.append(path)
    return sorted(files)


def detect_repo_root(start: Path) -> Path:
    current = start.resolve()
    candidates = [current, *current.parents]
    for candidate in candidates:
        if (candidate / "utilities" / "polybench.h").exists():
            return candidate
    return start.resolve()


def fake_libc_include_path() -> Path:
    bundled = Path(__file__).resolve().parent / "fake_libc_include"
    if bundled.exists():
        return bundled

    import pycparser  # type: ignore

    candidate = Path(pycparser.__file__).resolve().parent / "utils" / "fake_libc_include"
    if candidate.exists():
        return candidate

    raise RuntimeError(
        "No fake libc include directory found. "
        "Expected op_reporter/fake_libc_include or pycparser utils headers."
    )


def preprocess_source(
    c_file: Path,
    repo_root: Path,
    dataset_name: str,
    cpp_tool: str,
) -> str:
    dataset_flag = DATASET_FLAG_BY_NAME[dataset_name]
    fake_libc = fake_libc_include_path()

    args = [
        cpp_tool,
        "-E",
        "-P",
        "-nostdinc",
        f"-I{fake_libc}",
        f"-I{repo_root / 'utilities'}",
        f"-I{c_file.parent}",
        f"-D{dataset_flag}",
        "-DPOLYBENCH_USE_SCALAR_LB",
        str(c_file),
    ]

    proc = subprocess.run(args, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"Preprocessing failed for {c_file}:\n{proc.stderr}")

    source = proc.stdout
    source = "\n".join(
        line
        for line in source.splitlines()
        if not line.lstrip().startswith("#pragma")
    )
    return source


def dump_numeric_macros(
    c_file: Path,
    repo_root: Path,
    dataset_name: str,
    cpp_tool: str,
) -> dict[str, int]:
    dataset_flag = DATASET_FLAG_BY_NAME[dataset_name]
    fake_libc = fake_libc_include_path()

    args = [
        cpp_tool,
        "-E",
        "-dM",
        "-nostdinc",
        f"-I{fake_libc}",
        f"-I{repo_root / 'utilities'}",
        f"-I{c_file.parent}",
        f"-D{dataset_flag}",
        "-DPOLYBENCH_USE_SCALAR_LB",
        str(c_file),
    ]

    proc = subprocess.run(args, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        return {}

    macros: dict[str, int] = {}
    for line in proc.stdout.splitlines():
        match = re.match(r"^#define\s+([A-Za-z_][A-Za-z0-9_]*)\s+(.+)$", line)
        if not match:
            continue
        name, value = match.groups()
        value = value.strip()
        if "(" in value or ")" in value:
            continue
        parsed = parse_c_int_constant(value)
        if parsed is not None:
            macros[name] = parsed
    return macros


def parse_c_int_constant(value: str) -> int | None:
    value = value.strip()
    value = re.sub(r"[uUlL]+$", "", value)
    if not value:
        return None
    try:
        return int(value, 0)
    except ValueError:
        return None


def parse_c_float_constant(value: str) -> float | None:
    value = value.strip().rstrip("fFlL")
    try:
        return float(value)
    except ValueError:
        return None


def c_type_to_width(type_node: Any) -> str:
    from pycparser import c_ast  # type: ignore

    if isinstance(type_node, c_ast.TypeDecl):
        return c_type_to_width(type_node.type)
    if isinstance(type_node, c_ast.PtrDecl):
        return "ptr64"
    if isinstance(type_node, c_ast.ArrayDecl):
        return c_type_to_width(type_node.type)
    if isinstance(type_node, c_ast.IdentifierType):
        names = set(type_node.names)
        if "double" in names:
            return "float64"
        if "float" in names:
            return "float32"
        if "long" in names:
            return "int64"
        if "short" in names:
            return "int16"
        if "char" in names:
            return "int8"
        return "int32"
    return "unknown"


def width_rank(width: str) -> int:
    ranking = {
        "int1": 1,
        "int8": 8,
        "int16": 16,
        "int32": 32,
        "float32": 40,
        "int64": 64,
        "float64": 80,
        "ptr64": 90,
        "unknown": 0,
    }
    return ranking.get(width, 0)


def wider_width(left: str, right: str) -> str:
    return left if width_rank(left) >= width_rank(right) else right


class StaticCounter:
    def __init__(self, constants: dict[str, int], strict_static: bool) -> None:
        self.constants = constants
        self.strict_static = strict_static
        self.counts: Counter = Counter()
        self.width_counts: dict[str, Counter] = defaultdict(Counter)
        self.callees: set[str] = set()
        self.unresolved_loops: list[str] = []
        self.var_widths: dict[str, str] = {}
        self.env: dict[str, int | float] = dict(constants)

    def bump(self, op: str, amount: int, width: str = "unknown") -> None:
        if amount <= 0:
            return
        self.counts[op] += amount
        self.width_counts[op][width] += amount

    def infer_width(self, node: Any) -> str:
        from pycparser import c_ast  # type: ignore

        if node is None:
            return "unknown"
        if isinstance(node, c_ast.ID):
            return self.var_widths.get(node.name, "unknown")
        if isinstance(node, c_ast.Constant):
            if node.type in {"float", "double"}:
                return "float64" if node.type == "double" else "float32"
            if "." in node.value or "e" in node.value.lower():
                if node.value.lower().endswith("f"):
                    return "float32"
                return "float64"
            return "int32"
        if isinstance(node, c_ast.Cast):
            return c_type_to_width(node.to_type.type)
        if isinstance(node, c_ast.BinaryOp):
            return wider_width(self.infer_width(node.left), self.infer_width(node.right))
        if isinstance(node, c_ast.UnaryOp):
            return self.infer_width(node.expr)
        if isinstance(node, c_ast.ArrayRef):
            return self.infer_width(node.name)
        if isinstance(node, c_ast.FuncCall):
            return "unknown"
        return "unknown"

    def eval_const_expr(self, node: Any) -> int | float | None:
        from pycparser import c_ast  # type: ignore

        if node is None:
            return None
        if isinstance(node, c_ast.Constant):
            if node.type in {"int", "char"}:
                return parse_c_int_constant(node.value)
            if node.type in {"float", "double"}:
                return parse_c_float_constant(node.value)
            return None
        if isinstance(node, c_ast.ID):
            return self.env.get(node.name)
        if isinstance(node, c_ast.UnaryOp):
            value = self.eval_const_expr(node.expr)
            if value is None:
                return None
            if node.op == "+":
                return +value
            if node.op == "-":
                return -value
            if node.op == "!":
                return int(not value)
            if node.op == "~":
                return ~int(value)
            return None
        if isinstance(node, c_ast.BinaryOp):
            left = self.eval_const_expr(node.left)
            right = self.eval_const_expr(node.right)
            if left is None or right is None:
                return None
            op = node.op
            if op == "+":
                return left + right
            if op == "-":
                return left - right
            if op == "*":
                return left * right
            if op == "/":
                if right == 0:
                    return None
                return left / right
            if op == "%":
                if right == 0:
                    return None
                return int(left) % int(right)
            if op == "<<":
                return int(left) << int(right)
            if op == ">>":
                return int(left) >> int(right)
            if op == "&":
                return int(left) & int(right)
            if op == "|":
                return int(left) | int(right)
            if op == "^":
                return int(left) ^ int(right)
            if op == "&&":
                return int(bool(left) and bool(right))
            if op == "||":
                return int(bool(left) or bool(right))
            if op == "<":
                return int(left < right)
            if op == "<=":
                return int(left <= right)
            if op == ">":
                return int(left > right)
            if op == ">=":
                return int(left >= right)
            if op == "==":
                return int(left == right)
            if op == "!=":
                return int(left != right)
            return None
        if isinstance(node, c_ast.Cast):
            return self.eval_const_expr(node.expr)
        return None

    def is_constant_multiplication(self, left: Any, right: Any) -> bool:
        return self.eval_const_expr(left) is not None or self.eval_const_expr(right) is not None

    def is_constant_division(self, _dividend: Any, divisor: Any) -> bool:
        return self.eval_const_expr(divisor) is not None

    def analyze_expr(self, node: Any, multiplier: int, *, suppress_cmp: bool = False) -> None:
        from pycparser import c_ast  # type: ignore

        if node is None or multiplier <= 0:
            return
        if isinstance(node, c_ast.BinaryOp):
            op_map = {
                "+": "add",
                "-": "sub",
                "*": "mul",
                "/": "div",
                "%": "mod",
                "<": "cmp",
                "<=": "cmp",
                ">": "cmp",
                ">=": "cmp",
                "==": "cmp",
                "!=": "cmp",
                "&&": "logical",
                "||": "logical",
                "&": "bitwise",
                "|": "bitwise",
                "^": "bitwise",
                "<<": "bitwise",
                ">>": "bitwise",
            }
            operation = op_map.get(node.op)
            if operation is not None and not (suppress_cmp and operation == "cmp"):
                width = self.infer_width(node)
                if node.op == "*" and self.is_constant_multiplication(node.left, node.right):
                    operation = "mul_const"
                if node.op == "/" and self.is_constant_division(node.left, node.right):
                    operation = "div_const"
                self.bump(operation, multiplier, width)
            self.analyze_expr(node.left, multiplier, suppress_cmp=suppress_cmp)
            self.analyze_expr(node.right, multiplier, suppress_cmp=suppress_cmp)
            return
        if isinstance(node, c_ast.UnaryOp):
            self.bump("unary", multiplier, self.infer_width(node))
            self.analyze_expr(node.expr, multiplier, suppress_cmp=suppress_cmp)
            return
        if isinstance(node, c_ast.Assignment):
            width = self.infer_width(node.lvalue)
            self.bump("assign", multiplier, width)

            compound_map = {
                "+=": "add",
                "-=": "sub",
                "*=": "mul",
                "/=": "div",
                "%=": "mod",
                "&=": "bitwise",
                "|=": "bitwise",
                "^=": "bitwise",
                "<<=": "bitwise",
                ">>=": "bitwise",
            }
            compound_op = compound_map.get(node.op)
            if compound_op is not None:
                if node.op == "*=" and self.is_constant_multiplication(node.lvalue, node.rvalue):
                    compound_op = "mul_const"
                if node.op == "/=" and self.is_constant_division(node.lvalue, node.rvalue):
                    compound_op = "div_const"
                self.bump(compound_op, multiplier, width)

            self.analyze_expr(node.lvalue, multiplier, suppress_cmp=suppress_cmp)
            self.analyze_expr(node.rvalue, multiplier, suppress_cmp=suppress_cmp)
            if isinstance(node.lvalue, c_ast.ID) and node.op == "=":
                const_value = self.eval_const_expr(node.rvalue)
                if const_value is not None:
                    self.env[node.lvalue.name] = const_value
            return
        if isinstance(node, c_ast.FuncCall):
            self._record_call(node, multiplier)
            return
        if isinstance(node, c_ast.ExprList):
            for expr in node.exprs:
                self.analyze_expr(expr, multiplier, suppress_cmp=suppress_cmp)
            return
        if isinstance(node, c_ast.Cast):
            self.analyze_expr(node.expr, multiplier, suppress_cmp=suppress_cmp)
            return
        if isinstance(node, c_ast.ArrayRef):
            self.analyze_expr(node.name, multiplier, suppress_cmp=suppress_cmp)
            self.analyze_expr(node.subscript, multiplier, suppress_cmp=suppress_cmp)
            return
        if isinstance(node, c_ast.TernaryOp):
            self.bump("if", multiplier, "int1")
            self.analyze_expr(node.cond, multiplier, suppress_cmp=suppress_cmp)
            self.analyze_expr(node.iftrue, multiplier, suppress_cmp=suppress_cmp)
            self.analyze_expr(node.iffalse, multiplier, suppress_cmp=suppress_cmp)
            return

        for _, child in node.children():
            self.analyze_expr(child, multiplier, suppress_cmp=suppress_cmp)

    def _record_call(self, node: Any, multiplier: int) -> None:
        from pycparser import c_ast  # type: ignore

        if multiplier <= 0:
            return
        self.bump("call", multiplier, "unknown")
        if isinstance(node.name, c_ast.ID):
            self.callees.add(node.name.name)
        if node.args is not None:
            self.analyze_expr(node.args, multiplier)

    def _extract_for_components(self, for_node: Any) -> tuple[str | None, int | None, str | None, Any, int | None]:
        from pycparser import c_ast  # type: ignore

        loop_var: str | None = None
        start_val: int | None = None

        init = for_node.init
        if isinstance(init, c_ast.Assignment) and isinstance(init.lvalue, c_ast.ID):
            loop_var = init.lvalue.name
            evaluated = self.eval_const_expr(init.rvalue)
            if evaluated is not None:
                start_val = int(evaluated)
        elif isinstance(init, c_ast.DeclList) and init.decls:
            decl = init.decls[0]
            loop_var = decl.name
            if decl.init is not None:
                evaluated = self.eval_const_expr(decl.init)
                if evaluated is not None:
                    start_val = int(evaluated)

        cond_op: str | None = None
        cond_bound: Any = None
        if isinstance(for_node.cond, c_ast.BinaryOp):
            cond_op = for_node.cond.op
            if isinstance(for_node.cond.left, c_ast.ID):
                if loop_var is None:
                    loop_var = for_node.cond.left.name
                cond_bound = for_node.cond.right
            elif isinstance(for_node.cond.right, c_ast.ID):
                if loop_var is None:
                    loop_var = for_node.cond.right.name
                cond_bound = for_node.cond.left

        step: int | None = None
        nxt = for_node.next
        if isinstance(nxt, c_ast.UnaryOp) and isinstance(nxt.expr, c_ast.ID):
            if nxt.op in {"p++", "++"}:
                step = 1
            elif nxt.op in {"p--", "--"}:
                step = -1
        elif isinstance(nxt, c_ast.Assignment) and isinstance(nxt.lvalue, c_ast.ID):
            val = self.eval_const_expr(nxt.rvalue)
            if val is not None:
                if nxt.op == "+=":
                    step = int(val)
                elif nxt.op == "-=":
                    step = -int(val)
                elif nxt.op == "=":
                    maybe_next = int(val)
                    if start_val is not None:
                        step = maybe_next - start_val

        return loop_var, start_val, cond_op, cond_bound, step

    def _compute_iterations(self, start: int, op: str, bound: int, step: int) -> int:
        if step == 0:
            return 0
        if op == "<":
            if step <= 0:
                return 0
            return max(0, math.ceil((bound - start) / step))
        if op == "<=":
            if step <= 0:
                return 0
            return max(0, math.floor((bound - start) / step) + 1)
        if op == ">":
            if step >= 0:
                return 0
            return max(0, math.ceil((start - bound) / abs(step)))
        if op == ">=":
            if step >= 0:
                return 0
            return max(0, math.floor((start - bound) / abs(step)) + 1)
        return 0

    def analyze_for(self, node: Any, multiplier: int, function_name: str) -> None:
        from pycparser import c_ast  # type: ignore

        if node.init is not None:
            if isinstance(node.init, (c_ast.Assignment, c_ast.ExprList, c_ast.FuncCall)):
                self.analyze_expr(node.init, multiplier)
            else:
                self.analyze_stmt(node.init, multiplier, function_name)

        loop_var, start_val, cond_op, cond_bound_expr, step = self._extract_for_components(node)
        iterations: int | None = None
        if loop_var and start_val is not None and cond_op is not None and step is not None:
            bound_val = self.eval_const_expr(cond_bound_expr)
            if bound_val is not None:
                iterations = self._compute_iterations(start_val, cond_op, int(bound_val), step)

        # Loop indices are runtime-varying values across iterations, so they must not
        # remain in the constant environment used for mul/div const classification.
        if loop_var is not None:
            self.env.pop(loop_var, None)

        if iterations is None:
            message = f"{function_name}: unresolved loop bound"
            self.unresolved_loops.append(message)
            if self.strict_static:
                raise StaticCountingError(message)
            iterations = 0

        self.bump("loop_for", multiplier * iterations, "int32")

        if node.cond is not None:
            cond_checks = iterations + 1
            self.analyze_expr(node.cond, multiplier * cond_checks, suppress_cmp=True)

        # The loop update expression is loop-control bookkeeping (i++, i+=1, i=i+1).
        # We model loop progress via loop_for and do not charge arithmetic metrics here.

        self.analyze_stmt(node.stmt, multiplier * iterations, function_name)

    def analyze_stmt(self, node: Any, multiplier: int, function_name: str) -> None:
        from pycparser import c_ast  # type: ignore

        if node is None or multiplier <= 0:
            return
        if isinstance(node, c_ast.Compound):
            for stmt in node.block_items or []:
                self.analyze_stmt(stmt, multiplier, function_name)
            return
        if isinstance(node, c_ast.Decl):
            if node.name:
                self.var_widths[node.name] = c_type_to_width(node.type)
            if node.init is not None:
                self.bump("assign", multiplier, self.var_widths.get(node.name or "", "unknown"))
                self.analyze_expr(node.init, multiplier)
                if node.name:
                    val = self.eval_const_expr(node.init)
                    if val is not None:
                        self.env[node.name] = val
            return
        if isinstance(node, c_ast.Assignment):
            self.analyze_expr(node, multiplier)
            return
        if isinstance(node, c_ast.FuncCall):
            self._record_call(node, multiplier)
            return
        if isinstance(node, c_ast.For):
            self.analyze_for(node, multiplier, function_name)
            return
        if isinstance(node, c_ast.If):
            self.bump("if", multiplier, "int1")
            self.analyze_expr(node.cond, multiplier)
            self.analyze_stmt(node.iftrue, multiplier, function_name)
            if node.iffalse is not None:
                self.analyze_stmt(node.iffalse, multiplier, function_name)
            return
        if isinstance(node, c_ast.While):
            message = f"{function_name}: unresolved while-loop"
            self.unresolved_loops.append(message)
            if self.strict_static:
                raise StaticCountingError(message)
            return
        if isinstance(node, c_ast.DoWhile):
            message = f"{function_name}: unresolved do-while-loop"
            self.unresolved_loops.append(message)
            if self.strict_static:
                raise StaticCountingError(message)
            return
        if isinstance(node, c_ast.Return):
            self.analyze_expr(node.expr, multiplier)
            return

        for _, child in node.children():
            self.analyze_stmt(child, multiplier, function_name)


def parameter_bindings(funcdef: Any, constants: dict[str, int]) -> dict[str, int]:
    from pycparser import c_ast  # type: ignore

    bindings: dict[str, int] = {}
    params = []
    if isinstance(funcdef.decl.type, c_ast.FuncDecl) and funcdef.decl.type.args is not None:
        params = funcdef.decl.type.args.params
    for param in params:
        if not isinstance(param, c_ast.Decl) or not param.name:
            continue
        candidates = [param.name.upper()]
        if param.name.lower() == "tsteps":
            candidates.append("TSTEPS")
        if param.name.lower() == "tmax":
            candidates.append("TMAX")
        for key in candidates:
            if key in constants:
                bindings[param.name] = constants[key]
                break
    return bindings


def analyze_translation_unit(
    c_file: Path,
    source: str,
    constants: dict[str, int],
    strict_static: bool,
) -> tuple[list[FunctionReport], list[str]]:
    from pycparser import c_ast, c_parser  # type: ignore

    parser = c_parser.CParser()
    ast = parser.parse(source, filename=str(c_file))

    reports: list[FunctionReport] = []
    unresolved: list[str] = []
    for ext in ast.ext:
        if not isinstance(ext, c_ast.FuncDef):
            continue
        counter = StaticCounter(constants, strict_static)
        bindings = parameter_bindings(ext, constants)
        counter.env.update(bindings)

        params = []
        if ext.decl.type.args is not None:
            params = ext.decl.type.args.params
        for param in params:
            if isinstance(param, c_ast.Decl) and param.name:
                counter.var_widths[param.name] = c_type_to_width(param.type)

        counter.analyze_stmt(ext.body, 1, ext.decl.name)
        report = FunctionReport(
            name=ext.decl.name,
            counts=counter.counts,
            width_counts=counter.width_counts,
            callees=counter.callees,
            unresolved_loops=counter.unresolved_loops,
        )
        reports.append(report)
        unresolved.extend(counter.unresolved_loops)

    return reports, unresolved


def aggregate_counts(functions: list[FunctionReport]) -> Counter:
    totals: Counter = Counter()
    for fn in functions:
        totals.update(fn.counts)
    return totals


def aggregate_width_counts(functions: list[FunctionReport]) -> dict[str, Counter]:
    totals: dict[str, Counter] = defaultdict(Counter)
    for fn in functions:
        for op, widths in fn.width_counts.items():
            totals[op].update(widths)
    return totals


def run_llvm_validation(
    c_file: Path,
    repo_root: Path,
    dataset_name: str,
) -> Counter:
    if shutil_which("clang") is None:
        return Counter()

    dataset_flag = DATASET_FLAG_BY_NAME[dataset_name]
    cmd = [
        "clang",
        "-S",
        "-emit-llvm",
        f"-I{repo_root / 'utilities'}",
        f"-I{c_file.parent}",
        f"-D{dataset_flag}",
        "-DPOLYBENCH_USE_SCALAR_LB",
        "-o",
        "-",
        str(c_file),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        return Counter()

    opcode_map = {
        "add": "add",
        "fadd": "add",
        "sub": "sub",
        "fsub": "sub",
        "mul": "mul",
        "fmul": "mul",
        "sdiv": "div",
        "udiv": "div",
        "fdiv": "div",
        "srem": "mod",
        "urem": "mod",
        "icmp": "cmp",
        "fcmp": "cmp",
        "call": "call",
    }
    counts: Counter = Counter()
    for line in proc.stdout.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(";"):
            continue
        match = re.search(r"\b([a-z]+)\b", stripped)
        if not match:
            continue
        opcode = match.group(1)
        mapped = opcode_map.get(opcode)
        if mapped:
            counts[mapped] += 1
    return counts


def render_operation_table(counts: Counter) -> str:
    lines = ["| Operation | Count |", "|---|---:|"]
    for op in OPERATION_ORDER:
        value = counts.get(op, 0)
        lines.append(f"| {op} | {value} |")
    return "\n".join(lines)


def render_operation_matrix_table(
    labels: list[str],
    per_label_counts: dict[str, Counter],
) -> str:
    header = "| Operation | " + " | ".join(labels) + " |"
    separator = "|---|" + "|".join(["---:"] * len(labels)) + "|"
    lines = [header, separator]
    for op in OPERATION_ORDER:
        values = [str(per_label_counts.get(label, Counter()).get(op, 0)) for label in labels]
        lines.append("| " + op + " | " + " | ".join(values) + " |")
    return "\n".join(lines)


def render_operation_matrix_tables(
    per_label_counts: dict[str, Counter],
    max_data_columns: int = 6,
) -> list[str]:
    if max_data_columns < 1:
        raise ValueError("max_data_columns must be at least 1")

    labels = list(per_label_counts.keys())
    if not labels:
        return []

    tables: list[str] = []
    for idx in range(0, len(labels), max_data_columns):
        chunk = labels[idx : idx + max_data_columns]
        tables.append(render_operation_matrix_table(chunk, per_label_counts))
    return tables


def select_primary_function_for_master(report: FileReport) -> FunctionReport | None:
    if not report.functions:
        return None

    kernel_named = [fn for fn in report.functions if fn.name.startswith("kernel")]
    candidates = kernel_named if kernel_named else report.functions

    # Prefer the most operation-heavy function for stable comparison values.
    return max(candidates, key=lambda fn: (sum(fn.counts.values()), fn.name))


def render_width_table(width_counts: dict[str, Counter]) -> str:
    lines = ["| Operation | Width | Count |", "|---|---|---:|"]
    for op in OPERATION_ORDER:
        for width, count in sorted(width_counts.get(op, Counter()).items()):
            lines.append(f"| {op} | {width} | {count} |")
    if len(lines) == 2:
        lines.append("| - | - | 0 |")
    return "\n".join(lines)


def render_function_section(functions: list[FunctionReport]) -> str:
    chunks: list[str] = []
    for fn in functions:
        chunks.append(f"### Function `{fn.name}`")
        chunks.append("")
        chunks.append("#### Operation Counts")
        chunks.append(render_operation_table(fn.counts))
        chunks.append("")
        chunks.append("#### Width Breakdown")
        chunks.append(render_width_table(fn.width_counts))
        chunks.append("")
        if fn.callees:
            chunks.append("#### Calls")
            chunks.extend([f"- {name}" for name in sorted(fn.callees)])
            chunks.append("")
        if fn.unresolved_loops:
            chunks.append("#### Static Warnings")
            chunks.extend([f"- {item}" for item in fn.unresolved_loops])
            chunks.append("")
    return "\n".join(chunks)


def parse_pipe_row(row: str) -> list[str]:
    line = row.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_markdown_table_separator(row: str) -> bool:
    cells = parse_pipe_row(row)
    if not cells:
        return False
    for cell in cells:
        token = cell.replace(" ", "")
        if not re.fullmatch(r":?-{3,}:?", token):
            return False
    return True


def markdown_inline_to_reportlab(text: str) -> str:
    rendered = escape(text)
    rendered = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", rendered)
    rendered = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', rendered)

    def replace_markdown_link(match: re.Match[str]) -> str:
        label = match.group(1).strip()
        target = match.group(2).strip()
        if label == target:
            return label
        return f"{label} ({target})"

    rendered = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_markdown_link, rendered)
    return rendered


def markdown_to_pdf(markdown_text: str, output_pdf: Path) -> None:
    from reportlab.lib import colors  # type: ignore
    from reportlab.lib.pagesizes import A4  # type: ignore
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet  # type: ignore
    from reportlab.lib.units import inch  # type: ignore
    from reportlab.platypus import (  # type: ignore
        ListFlowable,
        ListItem,
        Paragraph,
        Preformatted,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )

    dense_mode = len(markdown_text.splitlines()) > 190

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        leftMargin=(0.3 if dense_mode else 0.35) * inch,
        rightMargin=(0.3 if dense_mode else 0.35) * inch,
        topMargin=(0.3 if dense_mode else 0.35) * inch,
        bottomMargin=(0.3 if dense_mode else 0.35) * inch,
    )

    styles = getSampleStyleSheet()
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=6 if dense_mode else 7,
        leading=7 if dense_mode else 8,
        spaceAfter=0,
    )
    heading_styles = {
        1: ParagraphStyle(
            "H1",
            parent=styles["Heading1"],
            fontSize=9 if dense_mode else 10,
            leading=10 if dense_mode else 12,
            spaceAfter=1 if dense_mode else 2,
        ),
        2: ParagraphStyle(
            "H2",
            parent=styles["Heading2"],
            fontSize=8 if dense_mode else 9,
            leading=9 if dense_mode else 10,
            spaceAfter=1,
        ),
        3: ParagraphStyle(
            "H3",
            parent=styles["Heading3"],
            fontSize=7 if dense_mode else 8,
            leading=8 if dense_mode else 9,
            spaceAfter=1,
        ),
        4: ParagraphStyle(
            "H4",
            parent=styles["Heading4"],
            fontSize=6 if dense_mode else 7,
            leading=7 if dense_mode else 8,
            spaceAfter=1,
        ),
    }
    code_style = ParagraphStyle(
        "Code",
        parent=body_style,
        fontName="Courier",
        fontSize=5 if dense_mode else 6,
        leading=6 if dense_mode else 7,
        leftIndent=6,
    )
    table_header_style = ParagraphStyle(
        "TableHeader",
        parent=body_style,
        fontName="Helvetica-Bold",
        fontSize=5 if dense_mode else 6,
        leading=6 if dense_mode else 7,
        spaceBefore=0,
        spaceAfter=0,
    )
    table_cell_style = ParagraphStyle(
        "TableCell",
        parent=body_style,
        fontSize=5 if dense_mode else 6,
        leading=6 if dense_mode else 7,
        spaceBefore=0,
        spaceAfter=0,
    )

    story: list[Any] = []
    lines = markdown_text.splitlines()
    i = 0
    paragraph_buffer: list[str] = []
    list_buffer: list[str] = []
    in_code_block = False
    code_buffer: list[str] = []

    def flush_paragraph() -> None:
        if not paragraph_buffer:
            return
        paragraph = " ".join(chunk.strip() for chunk in paragraph_buffer if chunk.strip()).strip()
        paragraph_buffer.clear()
        if paragraph:
            story.append(Paragraph(markdown_inline_to_reportlab(paragraph), body_style))
            story.append(Spacer(1, 0.5))

    def flush_list() -> None:
        if not list_buffer:
            return
        items = [
            ListItem(Paragraph(markdown_inline_to_reportlab(item), body_style), leftIndent=0)
            for item in list_buffer
        ]
        list_buffer.clear()
        story.append(ListFlowable(items, bulletType="bullet", leftIndent=10))
        story.append(Spacer(1, 0))

    def flush_code() -> None:
        if not code_buffer:
            return
        story.append(Preformatted("\n".join(code_buffer), style=code_style))
        code_buffer.clear()
        story.append(Spacer(1, 0))

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            flush_list()
            if in_code_block:
                flush_code()
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        if stripped and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if "|" in line and "|" in next_line and is_markdown_table_separator(next_line):
                flush_paragraph()
                flush_list()

                header = parse_pipe_row(line)
                align_row = parse_pipe_row(next_line)
                data_rows: list[list[str]] = []
                i += 2
                while i < len(lines):
                    row_line = lines[i]
                    if not row_line.strip() or "|" not in row_line:
                        break
                    data_rows.append(parse_pipe_row(row_line))
                    i += 1

                column_count = max(len(header), *(len(row) for row in data_rows)) if data_rows else len(header)
                header = header + [""] * (column_count - len(header))
                align_row = align_row + ["---"] * (column_count - len(align_row))
                normalized_rows = [row + [""] * (column_count - len(row)) for row in data_rows]

                table_data: list[list[Any]] = [
                    [Paragraph(markdown_inline_to_reportlab(cell), table_header_style) for cell in header]
                ]
                table_data.extend(
                    [Paragraph(markdown_inline_to_reportlab(cell), table_cell_style) for cell in row]
                    for row in normalized_rows
                )

                if column_count == 1:
                    col_widths = [doc.width]
                else:
                    first_col = min(doc.width * 0.24, 1.35 * inch)
                    remaining = max(doc.width - first_col, 0.1 * inch)
                    other_col = remaining / (column_count - 1)
                    col_widths = [first_col] + [other_col] * (column_count - 1)

                table = Table(table_data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
                table_style_commands: list[tuple[Any, ...]] = [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7EDF5")),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#8A97A8")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 2),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
                for col_idx, align_cell in enumerate(align_row):
                    marker = align_cell.replace(" ", "")
                    if marker.startswith(":") and marker.endswith(":"):
                        align = "CENTER"
                    elif marker.endswith(":"):
                        align = "RIGHT"
                    else:
                        align = "LEFT"
                    table_style_commands.append(("ALIGN", (col_idx, 1), (col_idx, -1), align))

                table.setStyle(TableStyle(table_style_commands))
                story.append(table)
                story.append(Spacer(1, 1))
                continue

        if not stripped:
            flush_paragraph()
            flush_list()
            i += 1
            continue

        heading_match = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading_match:
            flush_paragraph()
            flush_list()
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2)
            story.append(Paragraph(markdown_inline_to_reportlab(heading_text), heading_styles[level]))
            i += 1
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            list_buffer.append(stripped[2:].strip())
            i += 1
            continue

        flush_list()
        paragraph_buffer.append(stripped)
        i += 1

    flush_paragraph()
    flush_list()
    flush_code()

    if not story:
        story.append(Paragraph("(empty report)", body_style))

    doc.build(story)


def write_per_file_report(
    report: FileReport,
    dataset: str,
    generated_at: str,
    root: Path,
    llvm_enabled: bool,
) -> str:
    benchmark_name = report.c_path.stem
    function_counts = {fn.name: fn.counts for fn in report.functions}
    function_tables = render_operation_matrix_tables(function_counts, max_data_columns=6)

    lines = [
        f"# Static Operation Report: {benchmark_name}",
        "",
        f"Generated: {generated_at}",
        f"Dataset mode: {dataset}",
        f"Functions analyzed: {len(report.functions)}",
        "",
        "## File Totals",
        "",
        render_operation_table(report.totals),
        "",
        "## Width Totals",
        "",
        render_width_table(report.width_totals),
        "",
        "## Function Operation Matrices",
        "",
    ]

    if function_tables:
        for idx, table in enumerate(function_tables, start=1):
            if len(function_tables) > 1:
                lines.extend([f"### Function Table {idx}", ""])
            lines.extend([table, ""])
    else:
        lines.extend(["No functions found.", ""])

    if llvm_enabled:
        lines.extend([
            "## LLVM Validation (Optional)",
            "",
            render_operation_table(report.llvm_counts),
            "",
            "Note: LLVM counts are a non-fatal cross-check and may differ by lowering details.",
            "",
        ])

    if report.unresolved:
        lines.extend([
            "## Static Resolution Warnings",
            "",
            *[f"- {item}" for item in report.unresolved],
            "",
        ])

    markdown = "\n".join(lines)
    report.report_md.write_text(markdown)
    markdown_to_pdf(markdown, report.report_pdf)
    primary_function = select_primary_function_for_master(report)
    benchmark_counts = primary_function.counts if primary_function else report.totals
    write_operation_matrix_csv(report.report_csv, {benchmark_name: benchmark_counts})
    return markdown


def write_master_report(
    root: Path,
    reports: list[FileReport],
    generated_at: str,
    dataset: str,
    output_name: str,
) -> tuple[Path, Path, Path]:
    master_md = root / output_name
    master_pdf = master_md.with_suffix(".pdf")
    master_csv = master_md.with_suffix(".csv")

    global_counts: Counter = Counter()
    global_width: dict[str, Counter] = defaultdict(Counter)
    for report in reports:
        global_counts.update(report.totals)
        for op, widths in report.width_totals.items():
            global_width[op].update(widths)

    sorted_reports = sorted(reports, key=lambda rep: rep.c_path.relative_to(root).as_posix())
    per_file_counts: dict[str, Counter] = {}
    for report in sorted_reports:
        label = report.c_path.stem
        primary_function = select_primary_function_for_master(report)
        per_file_counts[label] = primary_function.counts if primary_function else Counter()
    file_tables = render_operation_matrix_tables(per_file_counts, max_data_columns=6)

    lines = [
        "# Master Static Operation Report",
        "",
        f"Generated: {generated_at}",
        f"Root directory: {root}",
        f"Dataset mode: {dataset}",
        f"C files analyzed: {len(reports)}",
        f"Functions analyzed: {sum(len(r.functions) for r in reports)}",
        "",
        "## Global Totals",
        "",
        render_operation_table(global_counts),
        "",
        "## Global Width Totals",
        "",
        render_width_table(global_width),
        "",
        "## Per-File Kernel Operation Matrices",
        "",
    ]

    if file_tables:
        for idx, table in enumerate(file_tables, start=1):
            if len(file_tables) > 1:
                lines.extend([f"### File Table {idx}", ""])
            lines.extend([table, ""])

    lines.extend([
        "## Function Matrices By File",
        "",
    ])

    for report in sorted_reports:
        lines.extend([f"### Functions for {report.c_path.stem}", ""])
        function_counts = {fn.name: fn.counts for fn in report.functions}
        function_tables = render_operation_matrix_tables(function_counts, max_data_columns=6)
        if function_tables:
            for idx, table in enumerate(function_tables, start=1):
                if len(function_tables) > 1:
                    lines.extend([f"#### Function Table {idx}", ""])
                lines.extend([table, ""])
        else:
            lines.extend(["No functions found.", ""])

    lines.extend([
        "## Per-File Reports",
        "",
    ])

    for report in sorted_reports:
        rel_c = report.c_path.relative_to(root).as_posix()
        rel_md = report.report_md.relative_to(root).as_posix()
        rel_pdf = report.report_pdf.relative_to(root).as_posix()
        lines.append(f"- {report.c_path.stem}: [{rel_md}]({rel_md}), [{rel_pdf}]({rel_pdf})")

    markdown = "\n".join(lines) + "\n"
    master_md.write_text(markdown)
    markdown_to_pdf(markdown, master_pdf)
    write_operation_matrix_csv(master_csv, per_file_counts)
    return master_md, master_pdf, master_csv


def write_operation_matrix_csv(output_csv: Path, per_label_counts: dict[str, Counter]) -> None:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["benchmark", *OPERATION_ORDER])
        for label in sorted(per_label_counts):
            counts = per_label_counts[label]
            writer.writerow([label, *[counts.get(op, 0) for op in OPERATION_ORDER]])


def add_dataset_to_name(filename: str, dataset: str) -> str:
    path = Path(filename)
    if path.suffix:
        return f"{path.stem}.{dataset}{path.suffix}"
    return f"{filename}.{dataset}"


def collect_json_config_paths(
    json_config: Path | None,
    json_dir: Path | None,
) -> list[Path]:
    if (json_config is None and json_dir is None) or (json_config is not None and json_dir is not None):
        raise RuntimeError("Provide exactly one of -j/--json-config or -jdir/--json-dir.")

    if json_config is not None:
        return [json_config.resolve()]

    assert json_dir is not None
    if not json_dir.exists() or not json_dir.is_dir():
        raise RuntimeError(f"JSON config directory not found: {json_dir}")

    config_paths = sorted(path.resolve() for path in json_dir.iterdir() if path.is_file() and path.suffix.lower() == ".json")
    if not config_paths:
        raise RuntimeError(f"No JSON config files found in directory: {json_dir}")

    return config_paths


def load_config_from_json(config_path: Path) -> dict[str, Any]:
    if not config_path.exists():
        raise RuntimeError(f"JSON config file not found: {config_path}")

    try:
        raw = json.loads(config_path.read_text())
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in config file {config_path}: {exc}") from exc

    if not isinstance(raw, dict):
        raise RuntimeError("JSON config must be an object (key-value map).")

    unknown_keys = sorted(set(raw.keys()) - CONFIG_ALLOWED_KEYS)
    if unknown_keys:
        joined = ", ".join(unknown_keys)
        raise RuntimeError(f"Unknown config keys: {joined}")

    missing_required = sorted(key for key in CONFIG_REQUIRED_KEYS if key not in raw)
    if missing_required:
        joined = ", ".join(missing_required)
        raise RuntimeError(f"Missing required config keys: {joined}")

    config = {**DEFAULT_REPORTER_CONFIG, **raw}

    if not isinstance(config["target"], str) or not config["target"].strip():
        raise RuntimeError("Config key 'target' must be a non-empty string.")

    if not isinstance(config["dataset"], str) or config["dataset"] not in DATASET_FLAG_BY_NAME:
        allowed = ", ".join(sorted(DATASET_FLAG_BY_NAME.keys()))
        raise RuntimeError(f"Config key 'dataset' must be one of: {allowed}")

    for key in ["master_name", "suffix", "requirements_file"]:
        if not isinstance(config[key], str) or not config[key].strip():
            raise RuntimeError(f"Config key '{key}' must be a non-empty string.")

    for key in ["strict_static", "llvm_validate", "no_auto_install"]:
        if not isinstance(config[key], bool):
            raise RuntimeError(f"Config key '{key}' must be true/false.")

    return config


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Static operation reporter for C files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-j",
        "--json-config",
        help="Path to JSON config file containing all run options",
    )
    group.add_argument(
        "-jdir",
        "--json-dir",
        help="Path to directory containing JSON config files; all will be executed",
    )
    return parser


def make_file_report_paths(c_path: Path, suffix: str, dataset: str) -> tuple[Path, Path, Path]:
    md_path = c_path.with_suffix(f".{suffix}.{dataset}.md")
    pdf_path = c_path.with_suffix(f".{suffix}.{dataset}.pdf")
    csv_path = c_path.with_suffix(f".{suffix}.{dataset}.csv")
    return md_path, pdf_path, csv_path


def main(argv: list[str] | None = None) -> int:
    parser = build_argument_parser()
    args = parser.parse_args(argv)

    json_config = Path(args.json_config) if args.json_config else None
    json_dir = Path(args.json_dir) if args.json_dir else None
    try:
        config_paths = collect_json_config_paths(json_config=json_config, json_dir=json_dir)
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        return 1

    overall_exit = 0

    for config_path in config_paths:
        try:
            config = load_config_from_json(config_path)
        except Exception as exc:  # noqa: BLE001
            print(str(exc), file=sys.stderr)
            overall_exit = 1
            continue

        config_dir = config_path.parent

        target_path = Path(config["target"])
        if not target_path.is_absolute():
            target_path = config_dir / target_path
        target = target_path.resolve()

        repo_root = detect_repo_root(target)

        if not target.exists() or not target.is_dir():
            print(f"Target directory not found: {target}", file=sys.stderr)
            overall_exit = 1
            continue

        requirements_path = Path(config["requirements_file"])
        if not requirements_path.is_absolute():
            requirements_path = (config_dir / requirements_path).resolve()

        try:
            ensure_runtime_dependencies(requirements_path, auto_install=not config["no_auto_install"])
        except Exception as exc:  # noqa: BLE001
            print(str(exc), file=sys.stderr)
            overall_exit = 1
            continue

        cpp_tool = pick_cpp_tool()
        c_files = discover_c_files(target)
        if not c_files:
            print("No C files found under target directory.")
            continue

        generated_at = datetime.now().isoformat(timespec="seconds")
        reports: list[FileReport] = []
        dataset = config["dataset"]

        for c_file in c_files:
            try:
                source = preprocess_source(c_file, repo_root, dataset, cpp_tool)
                constants = dump_numeric_macros(c_file, repo_root, dataset, cpp_tool)
                functions, unresolved = analyze_translation_unit(
                    c_file=c_file,
                    source=source,
                    constants=constants,
                    strict_static=config["strict_static"],
                )
                totals = aggregate_counts(functions)
                width_totals = aggregate_width_counts(functions)
                report_md, report_pdf, report_csv = make_file_report_paths(c_file, config["suffix"], dataset)
                llvm_counts = (
                    run_llvm_validation(c_file, repo_root, dataset)
                    if config["llvm_validate"]
                    else Counter()
                )
                report = FileReport(
                    c_path=c_file,
                    report_md=report_md,
                    report_pdf=report_pdf,
                    report_csv=report_csv,
                    functions=functions,
                    totals=totals,
                    width_totals=width_totals,
                    unresolved=unresolved,
                    llvm_counts=llvm_counts,
                )
                write_per_file_report(
                    report=report,
                    dataset=dataset,
                    generated_at=generated_at,
                    root=target,
                    llvm_enabled=config["llvm_validate"],
                )
                reports.append(report)
                print(f"[ok] {c_file.relative_to(target)}")
            except Exception as exc:  # noqa: BLE001
                print(f"[error] {c_file.relative_to(target)}: {exc}", file=sys.stderr)
                overall_exit = 1
                if config["strict_static"]:
                    break

        if not reports:
            continue

        master_name = add_dataset_to_name(config["master_name"], dataset)
        master_md, master_pdf, master_csv = write_master_report(
            root=target,
            reports=reports,
            generated_at=generated_at,
            dataset=dataset,
            output_name=master_name,
        )

        print(f"Generated per-file reports: {len(reports)}")
        print(f"Master report: {master_md}")
        print(f"Master PDF: {master_pdf}")
        print(f"Master CSV: {master_csv}")

    return overall_exit


if __name__ == "__main__":
    raise SystemExit(main())
