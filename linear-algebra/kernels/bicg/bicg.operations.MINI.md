# Static Operation Report: bicg

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 5045 |
| add | 4794 |
| sub | 0 |
| mul | 4788 |
| mul_const | 1 |
| div | 0 |
| div_const | 1676 |
| mod | 1756 |
| cmp | 81 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 81 |
| loop_for | 3432 |
| call | 180 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4948 |
| assign | int32 | 92 |
| assign | ptr64 | 5 |
| add | float64 | 3192 |
| add | int32 | 1602 |
| mul | float64 | 3192 |
| mul | int32 | 1596 |
| mul_const | int32 | 1 |
| div_const | float64 | 1676 |
| mod | int32 | 1756 |
| cmp | int32 | 81 |
| logical | int32 | 1 |
| unary | ptr64 | 10 |
| unary | unknown | 6 |
| if | int1 | 81 |
| loop_for | int32 | 3432 |
| call | unknown | 180 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 1720 | 2 | 3316 | 7 |
| add | 1596 | 0 | 3192 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1596 | 0 | 3192 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1676 | 0 | 0 | 0 |
| mod | 1676 | 80 | 0 | 0 |
| cmp | 0 | 80 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 80 | 0 | 1 |
| loop_for | 1676 | 80 | 1676 | 0 |
| call | 0 | 166 | 0 | 14 |
