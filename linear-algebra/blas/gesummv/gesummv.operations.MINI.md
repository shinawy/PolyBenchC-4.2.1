# Static Operation Report: gesummv

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 3791 |
| add | 3637 |
| sub | 0 |
| mul | 3660 |
| mul_const | 2 |
| div | 0 |
| div_const | 1830 |
| mod | 1860 |
| cmp | 31 |
| logical | 1 |
| bitwise | 0 |
| unary | 19 |
| if | 31 |
| loop_for | 1890 |
| call | 78 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 3720 |
| assign | int32 | 64 |
| assign | ptr64 | 7 |
| add | float64 | 1830 |
| add | int32 | 1807 |
| mul | float64 | 1860 |
| mul | int32 | 1800 |
| mul_const | int32 | 2 |
| div_const | float64 | 1830 |
| mod | int32 | 1860 |
| cmp | int32 | 31 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 11 |
| unary | unknown | 6 |
| if | int1 | 31 |
| loop_for | int32 | 1890 |
| call | unknown | 78 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 1863 | 1 | 1921 | 6 |
| add | 1800 | 0 | 1830 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1800 | 0 | 1860 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1830 | 0 | 0 | 0 |
| mod | 1830 | 30 | 0 | 0 |
| cmp | 0 | 30 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 30 | 0 | 1 |
| loop_for | 930 | 30 | 930 | 0 |
| call | 0 | 64 | 0 | 14 |
