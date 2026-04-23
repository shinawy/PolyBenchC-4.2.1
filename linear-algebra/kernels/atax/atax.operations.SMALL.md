# Static Operation Report: atax

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 43876 |
| add | 43281 |
| sub | 0 |
| mul | 28768 |
| mul_const | 14385 |
| div | 0 |
| div_const | 14508 |
| mod | 14508 |
| cmp | 125 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 125 |
| loop_for | 43756 |
| call | 264 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 43517 |
| assign | int32 | 355 |
| assign | ptr64 | 4 |
| add | float64 | 28892 |
| add | int32 | 14389 |
| mul | float64 | 28768 |
| mul_const | int32 | 14385 |
| div_const | float64 | 14508 |
| mod | int32 | 14508 |
| cmp | int32 | 125 |
| logical | int32 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 125 |
| loop_for | int32 | 43756 |
| call | unknown | 264 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 14627 | 1 | 29242 | 6 |
| add | 14508 | 0 | 28768 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 28768 | 0 |
| mul_const | 14384 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14508 | 0 | 0 | 0 |
| mod | 14384 | 124 | 0 | 0 |
| cmp | 0 | 124 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 124 | 0 | 1 |
| loop_for | 14624 | 124 | 29008 | 0 |
| call | 0 | 252 | 0 | 12 |
