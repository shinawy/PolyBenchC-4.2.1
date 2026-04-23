# Static Operation Report: bicg

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 482133 |
| add | 479706 |
| sub | 0 |
| mul | 479700 |
| mul_const | 1 |
| div | 0 |
| div_const | 160700 |
| mod | 161500 |
| cmp | 801 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 801 |
| loop_for | 322200 |
| call | 1620 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 481300 |
| assign | int32 | 828 |
| assign | ptr64 | 5 |
| add | float64 | 319800 |
| add | int32 | 159906 |
| mul | float64 | 319800 |
| mul | int32 | 159900 |
| mul_const | int32 | 1 |
| div_const | float64 | 160700 |
| mod | int32 | 161500 |
| cmp | int32 | 801 |
| logical | int32 | 1 |
| unary | ptr64 | 10 |
| unary | unknown | 6 |
| if | int1 | 801 |
| loop_for | int32 | 322200 |
| call | unknown | 1620 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 161112 | 2 | 321012 | 7 |
| add | 159900 | 0 | 319800 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 159900 | 0 | 319800 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 160700 | 0 | 0 | 0 |
| mod | 160700 | 800 | 0 | 0 |
| cmp | 0 | 800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 800 | 0 | 1 |
| loop_for | 160700 | 800 | 160700 | 0 |
| call | 0 | 1606 | 0 | 14 |
