# Static Operation Report: 3mm

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 25476 |
| add | 24494 |
| sub | 0 |
| mul | 23240 |
| mul_const | 1999 |
| div | 0 |
| div_const | 1640 |
| mod | 1992 |
| cmp | 353 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 353 |
| loop_for | 24772 |
| call | 726 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 24276 |
| assign | int32 | 1193 |
| assign | ptr64 | 7 |
| add | float64 | 21600 |
| add | int32 | 2894 |
| mul | float64 | 21600 |
| mul | int32 | 1640 |
| mul_const | int32 | 1999 |
| div_const | float64 | 1640 |
| mod | int32 | 1992 |
| cmp | int32 | 353 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 8 |
| if | int1 | 353 |
| loop_for | int32 | 24772 |
| call | unknown | 726 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 1722 | 17 | 23725 | 12 |
| add | 2528 | 352 | 21600 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1640 | 0 | 21600 | 0 |
| mul_const | 1640 | 352 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1640 | 0 | 0 | 0 |
| mod | 1640 | 352 | 0 | 0 |
| cmp | 0 | 352 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 352 | 0 | 1 |
| loop_for | 1718 | 368 | 22686 | 0 |
| call | 0 | 708 | 0 | 18 |
