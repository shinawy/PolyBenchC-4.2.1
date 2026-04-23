# Static Operation Report: 2mm

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1663276018 |
| add | 1661950010 |
| sub | 0 |
| mul | 2452870000 |
| mul_const | 960005 |
| div | 0 |
| div_const | 3910000 |
| mod | 4870000 |
| cmp | 960001 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 960001 |
| loop_for | 1662556000 |
| call | 1920018 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1661590000 |
| assign | int32 | 1686011 |
| assign | ptr64 | 7 |
| add | float64 | 1656000000 |
| add | int32 | 5950010 |
| mul | float64 | 2448960000 |
| mul | int32 | 3910000 |
| mul_const | int32 | 960005 |
| div_const | float64 | 3910000 |
| mod | int32 | 4870000 |
| cmp | int32 | 960001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 960001 |
| loop_for | int32 | 1662556000 |
| call | unknown | 1920018 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 3913606 | 801 | 1659361602 | 9 |
| add | 4990000 | 960000 | 1656000000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3910000 | 0 | 2448960000 | 0 |
| mul_const | 0 | 960000 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3910000 | 0 | 0 | 0 |
| mod | 3910000 | 960000 | 0 | 0 |
| cmp | 0 | 960000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 960000 | 0 | 1 |
| loop_for | 3913600 | 960800 | 1657681600 | 0 |
| call | 0 | 1920004 | 0 | 14 |
