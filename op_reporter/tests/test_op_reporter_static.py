from pathlib import Path
from collections import Counter

import pytest

from op_reporter import report_ops


def test_parse_c_int_constant_handles_suffixes() -> None:
    assert report_ops.parse_c_int_constant("42") == 42
    assert report_ops.parse_c_int_constant("0x10UL") == 16
    assert report_ops.parse_c_int_constant("100l") == 100


def test_discover_c_files_skips_internal_dirs(tmp_path: Path) -> None:
    (tmp_path / "kernel").mkdir()
    (tmp_path / "kernel" / "a.c").write_text("int main(){return 0;}\n")
    (tmp_path / "op_reporter").mkdir()
    (tmp_path / "op_reporter" / "b.c").write_text("int x;\n")

    discovered = report_ops.discover_c_files(tmp_path)
    assert discovered == [tmp_path / "kernel" / "a.c"]


def test_operation_counting_mul_vs_mul_const() -> None:
    source = """
    int f(int a, int b) {
      int c = 0;
      c = a * 2;
      c = a * b;
      return c;
    }
    """
    functions, unresolved = report_ops.analyze_translation_unit(
        c_file=Path("inline.c"),
        source=source,
        constants={},
        strict_static=True,
    )

    assert not unresolved
    assert len(functions) == 1
    counts = functions[0].counts
    assert counts["mul_const"] == 1
    assert counts["mul"] == 1


def test_operation_counting_div_vs_div_const() -> None:
        source = """
        int f(int a, int b) {
            int c = 1;
            c = a / 2;
            c = a / b;
            c /= 4;
            c /= b;
            return c;
        }
        """
        functions, unresolved = report_ops.analyze_translation_unit(
                c_file=Path("inline.c"),
                source=source,
                constants={},
                strict_static=True,
        )

        assert not unresolved
        assert len(functions) == 1
        counts = functions[0].counts
        assert counts["div_const"] == 2
        assert counts["div"] == 2


def test_compound_assignment_counts_operation() -> None:
        source = """
        int f(void) {
            int s = 0;
            s += 3;
            return s;
        }
        """
        functions, unresolved = report_ops.analyze_translation_unit(
                c_file=Path("inline.c"),
                source=source,
                constants={},
                strict_static=True,
        )

        assert not unresolved
        assert len(functions) == 1
        counts = functions[0].counts
        assert counts["assign"] == 2
        assert counts["add"] == 1


def test_loop_indices_not_marked_constant_multiplication() -> None:
        source = """
        int f(void) {
            int s = 0;
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 3; j++) {
                    s += i * j;
                }
            }
            return s;
        }
        """
        functions, unresolved = report_ops.analyze_translation_unit(
                c_file=Path("inline.c"),
                source=source,
                constants={},
                strict_static=True,
        )

        assert not unresolved
        counts = functions[0].counts
        assert counts["mul"] == 6
        assert counts["mul_const"] == 0


def test_for_loop_condition_comparisons_not_counted_as_cmp() -> None:
        source = """
        int f(void) {
            int s = 0;
            for (int i = 0; i < 4; i++) {
                s += i;
            }
            if (s > 0) {
                s = s - 1;
            }
            return s;
        }
        """
        functions, unresolved = report_ops.analyze_translation_unit(
                c_file=Path("inline.c"),
                source=source,
                constants={},
                strict_static=True,
        )

        assert not unresolved
        counts = functions[0].counts
        assert counts["cmp"] == 1


def test_for_loop_update_expressions_not_counted_as_add_or_unary() -> None:
        source = """
        int f(void) {
            int sink = 0;
            for (int i = 0; i < 3; i++) {
                sink = sink;
            }
            for (int k = 0; k < 2; k = k + 1) {
                sink = sink;
            }
            return sink;
        }
        """
        functions, unresolved = report_ops.analyze_translation_unit(
                c_file=Path("inline.c"),
                source=source,
                constants={},
                strict_static=True,
        )

        assert not unresolved
        counts = functions[0].counts
        assert counts["add"] == 0
        assert counts["unary"] == 0


def test_markdown_table_separator_detection() -> None:
    assert report_ops.is_markdown_table_separator("|---|---:|")
    assert report_ops.is_markdown_table_separator("|:---:|---|")
    assert not report_ops.is_markdown_table_separator("| Operation | Count |")


def test_markdown_to_pdf_renders_table(tmp_path: Path) -> None:
    markdown = """
    # Demo

    | Operation | Count |
    |---|---:|
    | add | 3 |
    | mul | 4 |

    - entry one
    - entry two
    """
    output_pdf = tmp_path / "demo.pdf"

    report_ops.markdown_to_pdf(markdown, output_pdf)

    assert output_pdf.exists()
    assert output_pdf.stat().st_size > 0


def test_markdown_inline_link_same_label_and_target_not_duplicated() -> None:
    text = "[adi/adi.operations.md](adi/adi.operations.md)"
    rendered = report_ops.markdown_inline_to_reportlab(text)

    assert rendered == "adi/adi.operations.md"


def test_load_config_from_json_applies_defaults(tmp_path: Path) -> None:
    config_path = tmp_path / "config.json"
    config_path.write_text('{"target": "stencils"}')

    config = report_ops.load_config_from_json(config_path)

    assert config["target"] == "stencils"
    assert config["dataset"] == "MEDIUM"
    assert config["suffix"] == "operations"
    assert config["master_name"] == "op_reporter_master_report.md"
    assert config["requirements_file"] == "op_reporter/requirements.txt"
    assert config["strict_static"] is False
    assert config["llvm_validate"] is False
    assert config["no_auto_install"] is False


def test_load_config_from_json_rejects_unknown_keys(tmp_path: Path) -> None:
    config_path = tmp_path / "config.json"
    config_path.write_text('{"target": "stencils", "unexpected": 1}')

    with pytest.raises(RuntimeError):
        report_ops.load_config_from_json(config_path)


def test_parser_requires_json_config_flag() -> None:
    parser = report_ops.build_argument_parser()

    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_parser_accepts_json_dir_flag() -> None:
    parser = report_ops.build_argument_parser()
    args = parser.parse_args(["-jdir", "configs"])

    assert args.json_dir == "configs"
    assert args.json_config is None


def test_make_file_report_paths_include_dataset_name() -> None:
    c_path = Path("kernel.c")

    md_path, pdf_path, _ = report_ops.make_file_report_paths(c_path, "operations", "MINI")

    assert md_path.name == "kernel.operations.MINI.md"
    assert pdf_path.name == "kernel.operations.MINI.pdf"


def test_add_dataset_to_name_keeps_extension() -> None:
    output_name = report_ops.add_dataset_to_name("op_reporter_master_report.md", "SMALL")

    assert output_name == "op_reporter_master_report.SMALL.md"


def test_collect_json_config_paths_from_dir_sorted(tmp_path: Path) -> None:
    config_dir = tmp_path / "configs"
    config_dir.mkdir()
    (config_dir / "b.json").write_text("{}")
    (config_dir / "a.json").write_text("{}")
    (config_dir / "note.txt").write_text("ignore")

    config_paths = report_ops.collect_json_config_paths(json_config=None, json_dir=config_dir)

    assert [item.name for item in config_paths] == ["a.json", "b.json"]


def test_collect_json_config_paths_rejects_empty_dir(tmp_path: Path) -> None:
    config_dir = tmp_path / "configs"
    config_dir.mkdir()

    with pytest.raises(RuntimeError):
        report_ops.collect_json_config_paths(json_config=None, json_dir=config_dir)


def test_per_file_report_uses_function_matrix_table(tmp_path: Path) -> None:
    function_a = report_ops.FunctionReport(
        name="f_alpha",
        counts=Counter({"add": 3, "mul": 1}),
        width_counts={},
        callees=set(),
    )
    function_b = report_ops.FunctionReport(
        name="f_beta",
        counts=Counter({"add": 2, "sub": 4}),
        width_counts={},
        callees=set(),
    )
    report = report_ops.FileReport(
        c_path=tmp_path / "kernel.c",
        report_md=tmp_path / "kernel.operations.md",
        report_pdf=tmp_path / "kernel.operations.pdf",
        report_csv=tmp_path / "kernel.operations.csv",
        functions=[function_a, function_b],
        totals=Counter({"add": 5, "mul": 1, "sub": 4}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )

    markdown = report_ops.write_per_file_report(
        report=report,
        dataset="MEDIUM",
        generated_at="2026-04-09T12:00:00",
        root=tmp_path,
        llvm_enabled=False,
    )

    assert "## Function Operation Matrices" in markdown
    assert "| Operation | f_alpha | f_beta |" in markdown
    assert "### Function `f_alpha`" not in markdown


def test_master_report_includes_inline_file_and_function_tables(tmp_path: Path) -> None:
    report_a = report_ops.FileReport(
        c_path=tmp_path / "bench_a.c",
        report_md=tmp_path / "bench_a.operations.md",
        report_pdf=tmp_path / "bench_a.operations.pdf",
        report_csv=tmp_path / "bench_a.operations.csv",
        functions=[
            report_ops.FunctionReport(
                name="kernel_a",
                counts=Counter({"add": 3, "mul": 2}),
                width_counts={},
                callees=set(),
            )
        ],
        totals=Counter({"add": 3, "mul": 2}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )
    report_b = report_ops.FileReport(
        c_path=tmp_path / "bench_b.c",
        report_md=tmp_path / "bench_b.operations.md",
        report_pdf=tmp_path / "bench_b.operations.pdf",
        report_csv=tmp_path / "bench_b.operations.csv",
        functions=[
            report_ops.FunctionReport(
                name="kernel_b",
                counts=Counter({"add": 1, "sub": 5}),
                width_counts={},
                callees=set(),
            )
        ],
        totals=Counter({"add": 1, "sub": 5}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )

    master_md, _, _ = report_ops.write_master_report(
        root=tmp_path,
        reports=[report_a, report_b],
        generated_at="2026-04-09T12:00:00",
        dataset="MEDIUM",
        output_name="master.md",
    )

    content = master_md.read_text()
    assert "## Per-File Kernel Operation Matrices" in content
    assert "| Operation | bench_a | bench_b |" in content
    assert "### Functions for bench_a" in content
    assert "### Functions for bench_b" in content
    assert "| Operation | kernel_a |" in content
    assert "| Operation | kernel_b |" in content


def test_render_operation_matrix_tables_splits_wide_columns() -> None:
    per_label_counts = {
        f"bench_{i}": Counter({"add": i, "mul": i * 2})
        for i in range(1, 9)
    }

    tables = report_ops.render_operation_matrix_tables(
        per_label_counts=per_label_counts,
        max_data_columns=3,
    )

    assert len(tables) == 3
    assert all(table.startswith("| Operation |") for table in tables)


def test_make_file_report_paths_returns_csv_with_dataset_name() -> None:
    c_path = Path("bench.c")

    md_path, pdf_path, csv_path = report_ops.make_file_report_paths(c_path, "operations", "MINI")

    assert md_path.name == "bench.operations.MINI.md"
    assert pdf_path.name == "bench.operations.MINI.pdf"
    assert csv_path.name == "bench.operations.MINI.csv"


def test_write_per_file_report_writes_csv_operation_matrix(tmp_path: Path) -> None:
    report = report_ops.FileReport(
        c_path=tmp_path / "bench.c",
        report_md=tmp_path / "bench.operations.MINI.md",
        report_pdf=tmp_path / "bench.operations.MINI.pdf",
        report_csv=tmp_path / "bench.operations.MINI.csv",
        functions=[
            report_ops.FunctionReport(
                name="kernel_main",
                counts=Counter({"add": 5, "mul": 2}),
                width_counts={},
                callees=set(),
            )
        ],
        totals=Counter({"add": 5, "mul": 2}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )

    report_ops.write_per_file_report(
        report=report,
        dataset="MINI",
        generated_at="2026-04-10T10:00:00",
        root=tmp_path,
        llvm_enabled=False,
    )

    csv_content = report.report_csv.read_text().splitlines()
    assert csv_content[0].startswith("benchmark,assign,add")
    assert any(line.startswith("bench,") for line in csv_content)


def test_write_master_report_writes_csv_for_primary_kernels(tmp_path: Path) -> None:
    report_a = report_ops.FileReport(
        c_path=tmp_path / "a.c",
        report_md=tmp_path / "a.operations.MINI.md",
        report_pdf=tmp_path / "a.operations.MINI.pdf",
        report_csv=tmp_path / "a.operations.MINI.csv",
        functions=[
            report_ops.FunctionReport(
                name="kernel_a",
                counts=Counter({"add": 3, "mul": 1}),
                width_counts={},
                callees=set(),
            )
        ],
        totals=Counter({"add": 3, "mul": 1}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )
    report_b = report_ops.FileReport(
        c_path=tmp_path / "b.c",
        report_md=tmp_path / "b.operations.MINI.md",
        report_pdf=tmp_path / "b.operations.MINI.pdf",
        report_csv=tmp_path / "b.operations.MINI.csv",
        functions=[
            report_ops.FunctionReport(
                name="kernel_b",
                counts=Counter({"sub": 4, "mul_const": 2}),
                width_counts={},
                callees=set(),
            )
        ],
        totals=Counter({"sub": 4, "mul_const": 2}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )

    master_md, master_pdf, master_csv = report_ops.write_master_report(
        root=tmp_path,
        reports=[report_a, report_b],
        generated_at="2026-04-10T10:00:00",
        dataset="MINI",
        output_name="op_reporter_master_report.MINI.md",
    )

    assert master_md.exists()
    assert master_pdf.exists()
    assert master_csv.exists()

    csv_content = master_csv.read_text().splitlines()
    assert csv_content[0].startswith("benchmark,assign,add")
    assert any(line.startswith("a,") for line in csv_content)
    assert any(line.startswith("b,") for line in csv_content)


def test_master_comparison_uses_kernel_function_counts_not_file_totals(tmp_path: Path) -> None:
    report_a = report_ops.FileReport(
        c_path=tmp_path / "bench_a.c",
        report_md=tmp_path / "bench_a.operations.md",
        report_pdf=tmp_path / "bench_a.operations.pdf",
        report_csv=tmp_path / "bench_a.operations.csv",
        functions=[
            report_ops.FunctionReport(
                name="init_array",
                counts=Counter({"add": 100}),
                width_counts={},
                callees=set(),
            ),
            report_ops.FunctionReport(
                name="kernel_a",
                counts=Counter({"add": 3, "mul": 2}),
                width_counts={},
                callees=set(),
            ),
        ],
        totals=Counter({"add": 103, "mul": 2}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )
    report_b = report_ops.FileReport(
        c_path=tmp_path / "bench_b.c",
        report_md=tmp_path / "bench_b.operations.md",
        report_pdf=tmp_path / "bench_b.operations.pdf",
        report_csv=tmp_path / "bench_b.operations.csv",
        functions=[
            report_ops.FunctionReport(
                name="kernel_b",
                counts=Counter({"add": 1, "sub": 5}),
                width_counts={},
                callees=set(),
            )
        ],
        totals=Counter({"add": 1, "sub": 5}),
        width_totals={},
        unresolved=[],
        llvm_counts=Counter(),
    )

    master_md, _, _ = report_ops.write_master_report(
        root=tmp_path,
        reports=[report_a, report_b],
        generated_at="2026-04-09T12:00:00",
        dataset="MEDIUM",
        output_name="master.md",
    )

    content = master_md.read_text()
    assert "| add | 3 | 1 |" in content
    assert "| add | 103 | 1 |" not in content
