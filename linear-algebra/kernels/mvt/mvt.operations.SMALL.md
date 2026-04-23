# Static Operation Report: mvt

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 44051 |
| add | 29166 |
| sub | 0 |
| mul | 43200 |
| mul_const | 1 |
| div | 0 |
| div_const | 14880 |
| mod | 15120 |
| cmp | 241 |
| logical | 1 |
| bitwise | 0 |
| unary | 18 |
| if | 241 |
| loop_for | 43800 |
| call | 500 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 43680 |
| assign | int32 | 366 |
| assign | ptr64 | 5 |
| add | float64 | 28800 |
| add | int32 | 366 |
| mul | float64 | 28800 |
| mul | int32 | 14400 |
| mul_const | int32 | 1 |
| div_const | float64 | 14880 |
| mod | int32 | 15120 |
| cmp | int32 | 241 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 241 |
| loop_for | int32 | 43800 |
| call | unknown | 500 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 15001 | 2 | 29042 | 6 |
| add | 360 | 0 | 28800 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14400 | 0 | 28800 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14880 | 0 | 0 | 0 |
| mod | 14880 | 240 | 0 | 0 |
| cmp | 0 | 240 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 240 | 0 | 1 |
| loop_for | 14520 | 240 | 29040 | 0 |
| call | 0 | 486 | 0 | 14 |
