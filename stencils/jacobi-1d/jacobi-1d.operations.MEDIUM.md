# Static Operation Report: jacobi-1d

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 80607 |
| add | 239602 |
| sub | 159400 |
| mul | 0 |
| mul_const | 79600 |
| div | 0 |
| div_const | 800 |
| mod | 400 |
| cmp | 401 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 401 |
| loop_for | 80500 |
| call | 812 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 80400 |
| assign | int32 | 205 |
| assign | ptr64 | 2 |
| add | float64 | 160000 |
| add | int32 | 79602 |
| sub | int32 | 159400 |
| mul_const | float64 | 79600 |
| div_const | float64 | 800 |
| mod | int32 | 400 |
| cmp | int32 | 401 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 401 |
| loop_for | int32 | 80500 |
| call | unknown | 812 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 801 | 1 | 79801 | 4 |
| add | 800 | 0 | 238800 | 2 |
| sub | 0 | 0 | 159400 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 79600 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 800 | 0 | 0 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 400 | 400 | 79700 | 0 |
| call | 0 | 804 | 0 | 8 |
