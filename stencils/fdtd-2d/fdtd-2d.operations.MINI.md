# Static Operation Report: fdtd-2d

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 37773 |
| add | 36667 |
| sub | 113860 |
| mul | 1800 |
| mul_const | 35823 |
| div | 0 |
| div_const | 1800 |
| mod | 1800 |
| cmp | 1801 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 1801 |
| loop_for | 38300 |
| call | 3620 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 36440 |
| assign | int32 | 1329 |
| assign | ptr64 | 4 |
| add | float64 | 11020 |
| add | int32 | 25647 |
| sub | float64 | 79060 |
| sub | int32 | 34800 |
| mul | float64 | 1800 |
| mul_const | float64 | 34020 |
| mul_const | int32 | 1803 |
| div_const | float64 | 1800 |
| mod | int32 | 1800 |
| cmp | int32 | 1801 |
| logical | int32 | 1 |
| unary | ptr64 | 11 |
| unary | unknown | 5 |
| if | int1 | 1801 |
| loop_for | int32 | 38300 |
| call | unknown | 3620 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 1842 | 63 | 35861 | 7 |
| add | 1800 | 1800 | 33060 | 7 |
| sub | 0 | 0 | 113860 | 0 |
| mul | 1800 | 0 | 0 | 0 |
| mul_const | 0 | 1800 | 34020 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1800 | 0 | 0 | 0 |
| mod | 0 | 1800 | 0 | 0 |
| cmp | 0 | 1800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 1800 | 0 | 1 |
| loop_for | 640 | 1860 | 35800 | 0 |
| call | 0 | 3608 | 0 | 12 |
