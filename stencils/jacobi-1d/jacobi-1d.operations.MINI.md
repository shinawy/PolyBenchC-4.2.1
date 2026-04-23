# Static Operation Report: jacobi-1d

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1227 |
| add | 3422 |
| sub | 2280 |
| mul | 0 |
| mul_const | 1120 |
| div | 0 |
| div_const | 60 |
| mod | 30 |
| cmp | 31 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 31 |
| loop_for | 1200 |
| call | 72 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1180 |
| assign | int32 | 45 |
| assign | ptr64 | 2 |
| add | float64 | 2300 |
| add | int32 | 1122 |
| sub | int32 | 2280 |
| mul_const | float64 | 1120 |
| div_const | float64 | 60 |
| mod | int32 | 30 |
| cmp | int32 | 31 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 31 |
| loop_for | int32 | 1200 |
| call | unknown | 72 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 61 | 1 | 1161 | 4 |
| add | 60 | 0 | 3360 | 2 |
| sub | 0 | 0 | 2280 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 1120 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 60 | 0 | 0 | 0 |
| mod | 0 | 30 | 0 | 0 |
| cmp | 0 | 30 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 30 | 0 | 1 |
| loop_for | 30 | 30 | 1140 | 0 |
| call | 0 | 64 | 0 | 8 |
