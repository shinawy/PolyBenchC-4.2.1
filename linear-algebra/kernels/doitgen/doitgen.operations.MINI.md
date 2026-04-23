# Static Operation Report: doitgen

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 15876 |
| add | 14406 |
| sub | 0 |
| mul | 12624 |
| mul_const | 2883 |
| div | 0 |
| div_const | 1104 |
| mod | 2064 |
| cmp | 961 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 961 |
| loop_for | 15786 |
| call | 1934 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 14544 |
| assign | int32 | 1329 |
| assign | ptr64 | 3 |
| add | float64 | 11520 |
| add | int32 | 2886 |
| mul | float64 | 11520 |
| mul | int32 | 1104 |
| mul_const | int32 | 2883 |
| div_const | float64 | 1104 |
| mod | int32 | 2064 |
| cmp | int32 | 961 |
| logical | int32 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 961 |
| loop_for | int32 | 15786 |
| call | unknown | 1934 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 1208 | 91 | 14571 | 6 |
| add | 960 | 1920 | 11520 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1104 | 0 | 11520 | 0 |
| mul_const | 0 | 2880 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1104 | 0 | 0 | 0 |
| mod | 1104 | 960 | 0 | 0 |
| cmp | 0 | 960 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 960 | 0 | 1 |
| loop_for | 1206 | 1050 | 13530 | 0 |
| call | 0 | 1924 | 0 | 10 |
