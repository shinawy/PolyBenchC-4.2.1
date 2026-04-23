# Static Operation Report: seidel-2d

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 576366 |
| add | 7840642 |
| sub | 3908241 |
| mul | 14400 |
| mul_const | 14401 |
| div | 0 |
| div_const | 571360 |
| mod | 14400 |
| cmp | 14401 |
| logical | 1 |
| bitwise | 0 |
| unary | 5 |
| if | 14401 |
| loop_for | 590760 |
| call | 28810 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 571360 |
| assign | int32 | 5005 |
| assign | ptr64 | 1 |
| add | float64 | 4470080 |
| add | int32 | 3370562 |
| sub | int32 | 3908241 |
| mul | float64 | 14400 |
| mul_const | int32 | 14401 |
| div_const | float64 | 571360 |
| mod | int32 | 14400 |
| cmp | int32 | 14401 |
| logical | int32 | 1 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 14401 |
| loop_for | int32 | 590760 |
| call | unknown | 28810 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 14521 | 121 | 561721 | 3 |
| add | 28800 | 14400 | 7797440 | 2 |
| sub | 0 | 0 | 3908241 | 0 |
| mul | 14400 | 0 | 0 | 0 |
| mul_const | 0 | 14400 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14400 | 0 | 556960 | 0 |
| mod | 0 | 14400 | 0 | 0 |
| cmp | 0 | 14400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 14400 | 0 | 1 |
| loop_for | 14520 | 14520 | 561720 | 0 |
| call | 0 | 28804 | 0 | 6 |
