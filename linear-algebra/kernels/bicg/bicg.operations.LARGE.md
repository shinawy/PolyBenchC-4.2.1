# Static Operation Report: bicg

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 11982213 |
| add | 11970006 |
| sub | 0 |
| mul | 11970000 |
| mul_const | 1 |
| div | 0 |
| div_const | 3994000 |
| mod | 3998000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 4001 |
| loop_for | 7992000 |
| call | 8020 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11978000 |
| assign | int32 | 4208 |
| assign | ptr64 | 5 |
| add | float64 | 7980000 |
| add | int32 | 3990006 |
| mul | float64 | 7980000 |
| mul | int32 | 3990000 |
| mul_const | int32 | 1 |
| div_const | float64 | 3994000 |
| mod | int32 | 3998000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | ptr64 | 10 |
| unary | unknown | 6 |
| if | int1 | 4001 |
| loop_for | int32 | 7992000 |
| call | unknown | 8020 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 3996102 | 2 | 7986102 | 7 |
| add | 3990000 | 0 | 7980000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3990000 | 0 | 7980000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3994000 | 0 | 0 | 0 |
| mod | 3994000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 3994000 | 4000 | 3994000 | 0 |
| call | 0 | 8006 | 0 | 14 |
