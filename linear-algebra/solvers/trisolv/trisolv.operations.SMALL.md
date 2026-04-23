# Static Operation Report: trisolv

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 727 |
| add | 4 |
| sub | 0 |
| mul | 0 |
| mul_const | 1 |
| div | 120 |
| div_const | 0 |
| mod | 120 |
| cmp | 121 |
| logical | 1 |
| bitwise | 0 |
| unary | 131 |
| if | 121 |
| loop_for | 360 |
| call | 254 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 480 |
| assign | int32 | 244 |
| assign | ptr64 | 3 |
| add | int32 | 4 |
| mul_const | int32 | 1 |
| div | float64 | 120 |
| mod | int32 | 120 |
| cmp | int32 | 121 |
| logical | int32 | 1 |
| unary | int32 | 120 |
| unary | ptr64 | 7 |
| unary | unknown | 4 |
| if | int1 | 121 |
| loop_for | int32 | 360 |
| call | unknown | 254 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 361 | 1 | 361 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 120 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 120 | 0 | 0 | 11 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 120 | 120 | 120 | 0 |
| call | 0 | 244 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trisolv: unresolved loop bound
