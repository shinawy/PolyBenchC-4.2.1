# Static Operation Report: jacobi-1d

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 9767 |
| add | 28562 |
| sub | 18960 |
| mul | 0 |
| mul_const | 9440 |
| div | 0 |
| div_const | 240 |
| mod | 120 |
| cmp | 121 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 121 |
| loop_for | 9720 |
| call | 252 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 9680 |
| assign | int32 | 85 |
| assign | ptr64 | 2 |
| add | float64 | 19120 |
| add | int32 | 9442 |
| sub | int32 | 18960 |
| mul_const | float64 | 9440 |
| div_const | float64 | 240 |
| mod | int32 | 120 |
| cmp | int32 | 121 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 121 |
| loop_for | int32 | 9720 |
| call | unknown | 252 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 241 | 1 | 9521 | 4 |
| add | 240 | 0 | 28320 | 2 |
| sub | 0 | 0 | 18960 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 9440 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 240 | 0 | 0 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 120 | 120 | 9480 | 0 |
| call | 0 | 244 | 0 | 8 |
