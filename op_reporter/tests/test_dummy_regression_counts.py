from __future__ import annotations

import json
from pathlib import Path

import pytest

from op_reporter import report_ops

REPO_ROOT = Path(__file__).resolve().parents[2]
DUMMY_ROOT = REPO_ROOT / "dummy_tests"
EXPECTED_PATH = DUMMY_ROOT / "expected_counts.json"

if not EXPECTED_PATH.exists():
    pytestmark = pytest.mark.skip(reason="dummy_tests/expected_counts.json not found")
    EXPECTED_COUNTS: dict[str, dict[str, int]] = {}
else:
    EXPECTED_COUNTS = json.loads(EXPECTED_PATH.read_text())

try:
    CPP_TOOL = report_ops.pick_cpp_tool()
except RuntimeError as exc:  # pragma: no cover - environment dependent
    pytestmark = pytest.mark.skip(reason=str(exc))
    CPP_TOOL = ""


@pytest.mark.parametrize(
    ("relative_c_path", "expected_ops"),
    sorted(EXPECTED_COUNTS.items()),
    ids=[item[0] for item in sorted(EXPECTED_COUNTS.items())],
)
def test_dummy_case_operation_counts(
    relative_c_path: str,
    expected_ops: dict[str, int],
) -> None:
    c_file = DUMMY_ROOT / relative_c_path
    assert c_file.exists(), f"Missing dummy source: {c_file}"

    preprocessed = report_ops.preprocess_source(
        c_file=c_file,
        repo_root=REPO_ROOT,
        dataset_name="MEDIUM",
        cpp_tool=CPP_TOOL,
    )
    constants = report_ops.dump_numeric_macros(
        c_file=c_file,
        repo_root=REPO_ROOT,
        dataset_name="MEDIUM",
        cpp_tool=CPP_TOOL,
    )
    functions, unresolved = report_ops.analyze_translation_unit(
        c_file=c_file,
        source=preprocessed,
        constants=constants,
        strict_static=True,
    )

    assert not unresolved, f"Unresolved static bounds in {relative_c_path}: {unresolved}"

    file_totals = report_ops.aggregate_counts(functions)
    for op_name, expected_count in expected_ops.items():
        actual_count = file_totals[op_name]
        assert actual_count == expected_count, (
            f"{relative_c_path}: expected {op_name}={expected_count}, "
            f"got {actual_count}"
        )
