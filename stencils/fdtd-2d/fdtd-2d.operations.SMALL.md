# Static Operation Report: fdtd-2d

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 590013 |
| add | 588127 |
| sub | 1885720 |
| mul | 14400 |
| mul_const | 579243 |
| div | 0 |
| div_const | 14400 |
| mod | 14400 |
| cmp | 14401 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 14401 |
| loop_for | 594680 |
| call | 28820 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 582480 |
| assign | int32 | 7529 |
| assign | ptr64 | 4 |
| add | float64 | 186440 |
| add | int32 | 401687 |
| sub | float64 | 1316120 |
| sub | int32 | 569600 |
| mul | float64 | 14400 |
| mul_const | float64 | 564840 |
| mul_const | int32 | 14403 |
| div_const | float64 | 14400 |
| mod | int32 | 14400 |
| cmp | int32 | 14401 |
| logical | int32 | 1 |
| unary | ptr64 | 11 |
| unary | unknown | 5 |
| if | int1 | 14401 |
| loop_for | int32 | 594680 |
| call | unknown | 28820 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 14502 | 183 | 575321 | 7 |
| add | 14400 | 14400 | 559320 | 7 |
| sub | 0 | 0 | 1885720 | 0 |
| mul | 14400 | 0 | 0 | 0 |
| mul_const | 0 | 14400 | 564840 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14400 | 0 | 0 | 0 |
| mod | 0 | 14400 | 0 | 0 |
| cmp | 0 | 14400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 14400 | 0 | 1 |
| loop_for | 4900 | 14580 | 575200 | 0 |
| call | 0 | 28808 | 0 | 12 |
