# Static Operation Report: trisolv

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2407 |
| add | 4 |
| sub | 0 |
| mul | 0 |
| mul_const | 1 |
| div | 400 |
| div_const | 0 |
| mod | 400 |
| cmp | 401 |
| logical | 1 |
| bitwise | 0 |
| unary | 411 |
| if | 401 |
| loop_for | 1200 |
| call | 814 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1600 |
| assign | int32 | 804 |
| assign | ptr64 | 3 |
| add | int32 | 4 |
| mul_const | int32 | 1 |
| div | float64 | 400 |
| mod | int32 | 400 |
| cmp | int32 | 401 |
| logical | int32 | 1 |
| unary | int32 | 400 |
| unary | ptr64 | 7 |
| unary | unknown | 4 |
| if | int1 | 401 |
| loop_for | int32 | 1200 |
| call | unknown | 814 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 1201 | 1 | 1201 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 400 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 400 | 0 | 0 | 11 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 400 | 400 | 400 | 0 |
| call | 0 | 804 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trisolv: unresolved loop bound
