# Static Operation Report: 2mm

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 15014018 |
| add | 14946510 |
| sub | 0 |
| mul | 22086700 |
| mul_const | 39605 |
| div | 0 |
| div_const | 159100 |
| mod | 198700 |
| cmp | 39601 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 39601 |
| loop_for | 14979800 |
| call | 79218 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 14938900 |
| assign | int32 | 75111 |
| assign | ptr64 | 7 |
| add | float64 | 14706000 |
| add | int32 | 240510 |
| mul | float64 | 21927600 |
| mul | int32 | 159100 |
| mul_const | int32 | 39605 |
| div_const | float64 | 159100 |
| mod | int32 | 198700 |
| cmp | int32 | 39601 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 39601 |
| loop_for | int32 | 14979800 |
| call | unknown | 79218 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 159866 | 181 | 14853962 | 9 |
| add | 200900 | 39600 | 14706000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 159100 | 0 | 21927600 | 0 |
| mul_const | 0 | 39600 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 159100 | 0 | 0 | 0 |
| mod | 159100 | 39600 | 0 | 0 |
| cmp | 0 | 39600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 39600 | 0 | 1 |
| loop_for | 159860 | 39780 | 14780160 | 0 |
| call | 0 | 79204 | 0 | 14 |
