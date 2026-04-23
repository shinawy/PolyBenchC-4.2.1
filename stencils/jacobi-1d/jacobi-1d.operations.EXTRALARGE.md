# Static Operation Report: jacobi-1d

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 8006007 |
| add | 23996002 |
| sub | 15994000 |
| mul | 0 |
| mul_const | 7996000 |
| div | 0 |
| div_const | 8000 |
| mod | 4000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 4001 |
| loop_for | 8005000 |
| call | 8012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 8004000 |
| assign | int32 | 2005 |
| assign | ptr64 | 2 |
| add | float64 | 16000000 |
| add | int32 | 7996002 |
| sub | int32 | 15994000 |
| mul_const | float64 | 7996000 |
| div_const | float64 | 8000 |
| mod | int32 | 4000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 4001 |
| loop_for | int32 | 8005000 |
| call | unknown | 8012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 8001 | 1 | 7998001 | 4 |
| add | 8000 | 0 | 23988000 | 2 |
| sub | 0 | 0 | 15994000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 7996000 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4000 | 4000 | 7997000 | 0 |
| call | 0 | 8004 | 0 | 8 |
