# Static Operation Report: mvt

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 482811 |
| add | 321206 |
| sub | 0 |
| mul | 480000 |
| mul_const | 1 |
| div | 0 |
| div_const | 161600 |
| mod | 162400 |
| cmp | 801 |
| logical | 1 |
| bitwise | 0 |
| unary | 18 |
| if | 801 |
| loop_for | 482000 |
| call | 1620 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 481600 |
| assign | int32 | 1206 |
| assign | ptr64 | 5 |
| add | float64 | 320000 |
| add | int32 | 1206 |
| mul | float64 | 320000 |
| mul | int32 | 160000 |
| mul_const | int32 | 1 |
| div_const | float64 | 161600 |
| mod | int32 | 162400 |
| cmp | int32 | 801 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 801 |
| loop_for | int32 | 482000 |
| call | unknown | 1620 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 162001 | 2 | 320802 | 6 |
| add | 1200 | 0 | 320000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 160000 | 0 | 320000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 161600 | 0 | 0 | 0 |
| mod | 161600 | 800 | 0 | 0 |
| cmp | 0 | 800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 800 | 0 | 1 |
| loop_for | 160400 | 800 | 320800 | 0 |
| call | 0 | 1606 | 0 | 14 |
