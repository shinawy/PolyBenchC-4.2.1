# Static Operation Report: jacobi-2d

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 34387 |
| add | 192664 |
| sub | 96360 |
| mul | 1800 |
| mul_const | 32262 |
| div | 0 |
| div_const | 1800 |
| mod | 900 |
| cmp | 901 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 901 |
| loop_for | 34360 |
| call | 1812 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 33160 |
| assign | int32 | 1225 |
| assign | ptr64 | 2 |
| add | float64 | 127240 |
| add | int32 | 65424 |
| sub | int32 | 96360 |
| mul | float64 | 1800 |
| mul_const | float64 | 31360 |
| mul_const | int32 | 902 |
| div_const | float64 | 1800 |
| mod | int32 | 900 |
| cmp | int32 | 901 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 901 |
| loop_for | int32 | 34360 |
| call | unknown | 1812 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 1831 | 31 | 32521 | 4 |
| add | 3600 | 900 | 188160 | 4 |
| sub | 0 | 0 | 96360 | 0 |
| mul | 1800 | 0 | 0 | 0 |
| mul_const | 0 | 900 | 31360 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1800 | 0 | 0 | 0 |
| mod | 0 | 900 | 0 | 0 |
| cmp | 0 | 900 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 900 | 0 | 1 |
| loop_for | 930 | 930 | 32500 | 0 |
| call | 0 | 1804 | 0 | 8 |
