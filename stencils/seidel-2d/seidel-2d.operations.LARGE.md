# Static Operation Report: seidel-2d

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2001005506 |
| add | 27956028002 |
| sub | 13974013001 |
| mul | 4000000 |
| mul_const | 4000001 |
| div | 0 |
| div_const | 2000002000 |
| mod | 4000000 |
| cmp | 4000001 |
| logical | 1 |
| bitwise | 0 |
| unary | 5 |
| if | 4000001 |
| loop_for | 2005005500 |
| call | 8000010 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2000002000 |
| assign | int32 | 1003505 |
| assign | ptr64 | 1 |
| add | float64 | 15972016000 |
| add | int32 | 11984012002 |
| sub | int32 | 13974013001 |
| mul | float64 | 4000000 |
| mul_const | int32 | 4000001 |
| div_const | float64 | 2000002000 |
| mod | int32 | 4000000 |
| cmp | int32 | 4000001 |
| logical | int32 | 1 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 4000001 |
| loop_for | int32 | 2005005500 |
| call | unknown | 8000010 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 4002001 | 2001 | 1997001501 | 3 |
| add | 8000000 | 4000000 | 27944028000 | 2 |
| sub | 0 | 0 | 13974013001 | 0 |
| mul | 4000000 | 0 | 0 | 0 |
| mul_const | 0 | 4000000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4000000 | 0 | 1996002000 | 0 |
| mod | 0 | 4000000 | 0 | 0 |
| cmp | 0 | 4000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 4000000 | 0 | 1 |
| loop_for | 4002000 | 4002000 | 1997001500 | 0 |
| call | 0 | 8000004 | 0 | 6 |
