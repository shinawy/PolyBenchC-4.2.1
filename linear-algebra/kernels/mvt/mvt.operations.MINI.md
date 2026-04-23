# Static Operation Report: mvt

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 5091 |
| add | 3326 |
| sub | 0 |
| mul | 4800 |
| mul_const | 1 |
| div | 0 |
| div_const | 1760 |
| mod | 1840 |
| cmp | 81 |
| logical | 1 |
| bitwise | 0 |
| unary | 18 |
| if | 81 |
| loop_for | 5000 |
| call | 180 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4960 |
| assign | int32 | 126 |
| assign | ptr64 | 5 |
| add | float64 | 3200 |
| add | int32 | 126 |
| mul | float64 | 3200 |
| mul | int32 | 1600 |
| mul_const | int32 | 1 |
| div_const | float64 | 1760 |
| mod | int32 | 1840 |
| cmp | int32 | 81 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 81 |
| loop_for | int32 | 5000 |
| call | unknown | 180 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 1801 | 2 | 3282 | 6 |
| add | 120 | 0 | 3200 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1600 | 0 | 3200 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1760 | 0 | 0 | 0 |
| mod | 1760 | 80 | 0 | 0 |
| cmp | 0 | 80 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 80 | 0 | 1 |
| loop_for | 1640 | 80 | 3280 | 0 |
| call | 0 | 166 | 0 | 14 |
