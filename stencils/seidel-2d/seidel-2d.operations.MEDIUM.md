# Static Operation Report: seidel-2d

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 16041106 |
| add | 222245602 |
| sub | 110962601 |
| mul | 160000 |
| mul_const | 160001 |
| div | 0 |
| div_const | 16000400 |
| mod | 160000 |
| cmp | 160001 |
| logical | 1 |
| bitwise | 0 |
| unary | 5 |
| if | 160001 |
| loop_for | 16201100 |
| call | 320010 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 16000400 |
| assign | int32 | 40705 |
| assign | ptr64 | 1 |
| add | float64 | 126883200 |
| add | int32 | 95362402 |
| sub | int32 | 110962601 |
| mul | float64 | 160000 |
| mul_const | int32 | 160001 |
| div_const | float64 | 16000400 |
| mod | int32 | 160000 |
| cmp | int32 | 160001 |
| logical | int32 | 1 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 160001 |
| loop_for | int32 | 16201100 |
| call | unknown | 320010 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 160401 | 401 | 15880301 | 3 |
| add | 320000 | 160000 | 221765600 | 2 |
| sub | 0 | 0 | 110962601 | 0 |
| mul | 160000 | 0 | 0 | 0 |
| mul_const | 0 | 160000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 160000 | 0 | 15840400 | 0 |
| mod | 0 | 160000 | 0 | 0 |
| cmp | 0 | 160000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 160000 | 0 | 1 |
| loop_for | 160400 | 160400 | 15880300 | 0 |
| call | 0 | 320004 | 0 | 6 |
