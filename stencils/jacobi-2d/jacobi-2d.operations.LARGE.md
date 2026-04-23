# Static Operation Report: jacobi-2d

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1689485607 |
| add | 10117274004 |
| sub | 5057009000 |
| mul | 3380000 |
| mul_const | 1686494002 |
| div | 0 |
| div_const | 3380000 |
| mod | 1690000 |
| cmp | 1690001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 1690001 |
| loop_for | 1689485100 |
| call | 3380012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1688184000 |
| assign | int32 | 1301605 |
| assign | ptr64 | 2 |
| add | float64 | 6742596000 |
| add | int32 | 3374678004 |
| sub | int32 | 5057009000 |
| mul | float64 | 3380000 |
| mul_const | float64 | 1684804000 |
| mul_const | int32 | 1690002 |
| div_const | float64 | 3380000 |
| mod | int32 | 1690000 |
| cmp | int32 | 1690001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 1690001 |
| loop_for | int32 | 1689485100 |
| call | unknown | 3380012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 3381301 | 1301 | 1686103001 | 4 |
| add | 6760000 | 1690000 | 10108824000 | 4 |
| sub | 0 | 0 | 5057009000 | 0 |
| mul | 3380000 | 0 | 0 | 0 |
| mul_const | 0 | 1690000 | 1684804000 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3380000 | 0 | 0 | 0 |
| mod | 0 | 1690000 | 0 | 0 |
| cmp | 0 | 1690000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 1690000 | 0 | 1 |
| loop_for | 1691300 | 1691300 | 1686102500 | 0 |
| call | 0 | 3380004 | 0 | 8 |
