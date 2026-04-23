# Static Operation Report: jacobi-2d

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 15678891607 |
| add | 93984848004 |
| sub | 46984018000 |
| mul | 15680000 |
| mul_const | 15665448002 |
| div | 0 |
| div_const | 15680000 |
| mod | 7840000 |
| cmp | 7840001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 7840001 |
| loop_for | 15678890600 |
| call | 15680012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 15673288000 |
| assign | int32 | 5603605 |
| assign | ptr64 | 2 |
| add | float64 | 62646112000 |
| add | int32 | 31338736004 |
| sub | int32 | 46984018000 |
| mul | float64 | 15680000 |
| mul_const | float64 | 15657608000 |
| mul_const | int32 | 7840002 |
| div_const | float64 | 15680000 |
| mod | int32 | 7840000 |
| cmp | int32 | 7840001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 7840001 |
| loop_for | int32 | 15678890600 |
| call | unknown | 15680012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 15682801 | 2801 | 15663206001 | 4 |
| add | 31360000 | 7840000 | 93945648000 | 4 |
| sub | 0 | 0 | 46984018000 | 0 |
| mul | 15680000 | 0 | 0 | 0 |
| mul_const | 0 | 7840000 | 15657608000 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15680000 | 0 | 0 | 0 |
| mod | 0 | 7840000 | 0 | 0 |
| cmp | 0 | 7840000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 7840000 | 0 | 1 |
| loop_for | 7842800 | 7842800 | 15663205000 | 0 |
| call | 0 | 15680004 | 0 | 8 |
