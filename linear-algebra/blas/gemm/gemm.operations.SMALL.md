# Static Operation Report: gemm

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 359993 |
| add | 354806 |
| sub | 0 |
| mul | 690800 |
| mul_const | 4203 |
| div | 0 |
| div_const | 14600 |
| mod | 18800 |
| cmp | 4201 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 4201 |
| loop_for | 364120 |
| call | 8414 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 354800 |
| assign | int32 | 5188 |
| assign | ptr64 | 5 |
| add | float64 | 336000 |
| add | int32 | 18806 |
| mul | float64 | 676200 |
| mul | int32 | 14600 |
| mul_const | int32 | 4203 |
| div_const | float64 | 14600 |
| mod | int32 | 18800 |
| cmp | int32 | 4201 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 4201 |
| loop_for | int32 | 364120 |
| call | unknown | 8414 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemm | main |
|---|---:|---:|---:|---:|
| assign | 14805 | 61 | 345121 | 6 |
| add | 14600 | 4200 | 336000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14600 | 0 | 676200 | 0 |
| mul_const | 0 | 4200 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14600 | 0 | 0 | 0 |
| mod | 14600 | 4200 | 0 | 0 |
| cmp | 0 | 4200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 4200 | 0 | 1 |
| loop_for | 14800 | 4260 | 345060 | 0 |
| call | 0 | 8404 | 0 | 10 |
