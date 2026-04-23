# Static Operation Report: trisolv

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 247 |
| add | 4 |
| sub | 0 |
| mul | 0 |
| mul_const | 1 |
| div | 40 |
| div_const | 0 |
| mod | 40 |
| cmp | 41 |
| logical | 1 |
| bitwise | 0 |
| unary | 51 |
| if | 41 |
| loop_for | 120 |
| call | 94 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 160 |
| assign | int32 | 84 |
| assign | ptr64 | 3 |
| add | int32 | 4 |
| mul_const | int32 | 1 |
| div | float64 | 40 |
| mod | int32 | 40 |
| cmp | int32 | 41 |
| logical | int32 | 1 |
| unary | int32 | 40 |
| unary | ptr64 | 7 |
| unary | unknown | 4 |
| if | int1 | 41 |
| loop_for | int32 | 120 |
| call | unknown | 94 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 121 | 1 | 121 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 40 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 40 | 0 | 0 | 11 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 40 | 40 | 40 | 0 |
| call | 0 | 84 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trisolv: unresolved loop bound
