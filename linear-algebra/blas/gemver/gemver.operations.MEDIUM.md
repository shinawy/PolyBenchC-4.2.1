# Static Operation Report: gemver

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 645219 |
| add | 642410 |
| sub | 0 |
| mul | 1120000 |
| mul_const | 1 |
| div | 0 |
| div_const | 164000 |
| mod | 160400 |
| cmp | 401 |
| logical | 1 |
| bitwise | 0 |
| unary | 33 |
| if | 401 |
| loop_for | 642400 |
| call | 826 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 643601 |
| assign | int32 | 1607 |
| assign | ptr64 | 11 |
| add | float64 | 640400 |
| add | int32 | 2010 |
| mul | float64 | 960000 |
| mul | int32 | 160000 |
| mul_const | int32 | 1 |
| div_const | float64 | 164000 |
| mod | int32 | 160400 |
| cmp | int32 | 401 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 21 |
| unary | unknown | 10 |
| if | int1 | 401 |
| loop_for | int32 | 642400 |
| call | unknown | 826 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 163604 | 1 | 481604 | 10 |
| add | 2000 | 0 | 640400 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 160000 | 0 | 960000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 164000 | 0 | 0 | 0 |
| mod | 160000 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 160400 | 400 | 481600 | 0 |
| call | 0 | 804 | 0 | 22 |
