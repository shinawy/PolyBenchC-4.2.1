# Static Operation Report: trmm

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 3605008 |
| add | 3600004 |
| sub | 1200000 |
| mul | 1200000 |
| mul_const | 1200002 |
| div | 0 |
| div_const | 1200000 |
| mod | 2400000 |
| cmp | 1200001 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 1200001 |
| loop_for | 3603000 |
| call | 2400012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2401000 |
| assign | int32 | 1204005 |
| assign | ptr64 | 3 |
| add | int32 | 3600004 |
| sub | int32 | 1200000 |
| mul | float64 | 1200000 |
| mul_const | int32 | 1200002 |
| div_const | float64 | 1200000 |
| mod | int32 | 2400000 |
| cmp | int32 | 1200001 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 3 |
| if | int1 | 1200001 |
| loop_for | int32 | 3603000 |
| call | unknown | 2400012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 1203002 | 1001 | 2401001 | 4 |
| add | 1200000 | 1200000 | 1200000 | 4 |
| sub | 1200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 1200000 | 0 |
| mul_const | 0 | 1200000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1200000 | 0 | 0 | 0 |
| mod | 1200000 | 1200000 | 0 | 0 |
| cmp | 0 | 1200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 1200000 | 0 | 1 |
| loop_for | 1201000 | 1201000 | 1201000 | 0 |
| call | 0 | 2400004 | 0 | 8 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trmm: unresolved loop bound
