# Static Operation Report: jacobi-1d

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2003007 |
| add | 5998002 |
| sub | 3997000 |
| mul | 0 |
| mul_const | 1998000 |
| div | 0 |
| div_const | 4000 |
| mod | 2000 |
| cmp | 2001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 2001 |
| loop_for | 2002500 |
| call | 4012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2002000 |
| assign | int32 | 1005 |
| assign | ptr64 | 2 |
| add | float64 | 4000000 |
| add | int32 | 1998002 |
| sub | int32 | 3997000 |
| mul_const | float64 | 1998000 |
| div_const | float64 | 4000 |
| mod | int32 | 2000 |
| cmp | int32 | 2001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 2001 |
| loop_for | int32 | 2002500 |
| call | unknown | 4012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 4001 | 1 | 1999001 | 4 |
| add | 4000 | 0 | 5994000 | 2 |
| sub | 0 | 0 | 3997000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 1998000 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4000 | 0 | 0 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 2000 | 2000 | 1998500 | 0 |
| call | 0 | 4004 | 0 | 8 |
