# Static Operation Report: seidel-2d

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 31346 |
| add | 409122 |
| sub | 203721 |
| mul | 1600 |
| mul_const | 1601 |
| div | 0 |
| div_const | 30480 |
| mod | 1600 |
| cmp | 1601 |
| logical | 1 |
| bitwise | 0 |
| unary | 5 |
| if | 1601 |
| loop_for | 32940 |
| call | 3210 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 30480 |
| assign | int32 | 865 |
| assign | ptr64 | 1 |
| add | float64 | 232640 |
| add | int32 | 176482 |
| sub | int32 | 203721 |
| mul | float64 | 1600 |
| mul_const | int32 | 1601 |
| div_const | float64 | 30480 |
| mod | int32 | 1600 |
| cmp | int32 | 1601 |
| logical | int32 | 1 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 1601 |
| loop_for | int32 | 32940 |
| call | unknown | 3210 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 1641 | 41 | 29661 | 3 |
| add | 3200 | 1600 | 404320 | 2 |
| sub | 0 | 0 | 203721 | 0 |
| mul | 1600 | 0 | 0 | 0 |
| mul_const | 0 | 1600 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1600 | 0 | 28880 | 0 |
| mod | 0 | 1600 | 0 | 0 |
| cmp | 0 | 1600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 1600 | 0 | 1 |
| loop_for | 1640 | 1640 | 29660 | 0 |
| call | 0 | 3204 | 0 | 6 |
