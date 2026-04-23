# Static Operation Report: mvt

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 12014011 |
| add | 8006006 |
| sub | 0 |
| mul | 12000000 |
| mul_const | 1 |
| div | 0 |
| div_const | 4008000 |
| mod | 4012000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 18 |
| if | 4001 |
| loop_for | 12010000 |
| call | 8020 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 12008000 |
| assign | int32 | 6006 |
| assign | ptr64 | 5 |
| add | float64 | 8000000 |
| add | int32 | 6006 |
| mul | float64 | 8000000 |
| mul | int32 | 4000000 |
| mul_const | int32 | 1 |
| div_const | float64 | 4008000 |
| mod | int32 | 4012000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 4001 |
| loop_for | int32 | 12010000 |
| call | unknown | 8020 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 4010001 | 2 | 8004002 | 6 |
| add | 6000 | 0 | 8000000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4000000 | 0 | 8000000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4008000 | 0 | 0 | 0 |
| mod | 4008000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4002000 | 4000 | 8004000 | 0 |
| call | 0 | 8006 | 0 | 14 |
