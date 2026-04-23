# op_reporter

Static operation reporting pipeline for PolyBench C kernels.

## Run

```bash
/home/maco/KAUST/Dropbox/SyncFolder/Benchmarks/PolyBenchC-4.2.1/.venv/bin/python -m op_reporter -j op_reporter/op_reporter_config.json
```

Run multiple JSON configs from a directory:

```bash
/home/maco/KAUST/Dropbox/SyncFolder/Benchmarks/PolyBenchC-4.2.1/.venv/bin/python -m op_reporter -jdir op_reporter/configs
```

## JSON Config

Runtime options are provided through JSON files passed with either `-j` or `-jdir`.

Example keys:

- `target`: directory to scan recursively
- `dataset`: `MEDIUM` (default), `MINI`, `SMALL`, `LARGE`, `EXTRALARGE`
- `strict_static`: fail when a loop bound cannot be statically resolved
- `llvm_validate`: optional clang LLVM IR cross-check
- `suffix`: writes `<file>.<suffix>.md` and `<file>.<suffix>.pdf`
- `suffix`: writes `<file>.<suffix>.md`, `<file>.<suffix>.pdf`, and `<file>.<suffix>.csv`
- `master_name`: master markdown report filename in target root
- `requirements_file`: requirements file to maintain for runtime dependencies
- `no_auto_install`: disable automatic pip install for missing runtime dependencies

See `op_reporter/op_reporter_config.json` for a single-config example.

Dataset-labeled config files are provided in `op_reporter/configs/`:

- `op_reporter_config_MINI.json`
- `op_reporter_config_SMALL.json`
- `op_reporter_config_MEDIUM.json`
- `op_reporter_config_LARGE.json`
- `op_reporter_config_EXTRALARGE.json`

## Output

- Per-file markdown, PDF, and CSV reports next to each analyzed `.c` source (filename includes dataset)
- One master markdown, PDF, and CSV report in the selected root directory (filename includes dataset)
- Function-level operation totals
- Call graph per function
- Separate mul/mul_const and div/div_const counts
- Width breakdown per operation (e.g. `int32`, `float64`)
