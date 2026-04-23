# Static Operation Report: gesummv

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 32951 |
| add | 32497 |
| sub | 0 |
| mul | 32580 |
| mul_const | 2 |
| div | 0 |
| div_const | 16290 |
| mod | 16380 |
| cmp | 91 |
| logical | 1 |
| bitwise | 0 |
| unary | 19 |
| if | 91 |
| loop_for | 16470 |
| call | 198 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 32760 |
| assign | int32 | 184 |
| assign | ptr64 | 7 |
| add | float64 | 16290 |
| add | int32 | 16207 |
| mul | float64 | 16380 |
| mul | int32 | 16200 |
| mul_const | int32 | 2 |
| div_const | float64 | 16290 |
| mod | int32 | 16380 |
| cmp | int32 | 91 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 11 |
| unary | unknown | 6 |
| if | int1 | 91 |
| loop_for | int32 | 16470 |
| call | unknown | 198 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 16383 | 1 | 16561 | 6 |
| add | 16200 | 0 | 16290 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16200 | 0 | 16380 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16290 | 0 | 0 | 0 |
| mod | 16290 | 90 | 0 | 0 |
| cmp | 0 | 90 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 90 | 0 | 1 |
| loop_for | 8190 | 90 | 8190 | 0 |
| call | 0 | 184 | 0 | 14 |
