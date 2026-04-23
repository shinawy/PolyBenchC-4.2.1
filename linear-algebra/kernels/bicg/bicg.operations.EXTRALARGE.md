# Static Operation Report: bicg

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 11892413 |
| add | 11880006 |
| sub | 0 |
| mul | 11880000 |
| mul_const | 1 |
| div | 0 |
| div_const | 3964000 |
| mod | 3968000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 4001 |
| loop_for | 7932000 |
| call | 8020 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11888000 |
| assign | int32 | 4408 |
| assign | ptr64 | 5 |
| add | float64 | 7920000 |
| add | int32 | 3960006 |
| mul | float64 | 7920000 |
| mul | int32 | 3960000 |
| mul_const | int32 | 1 |
| div_const | float64 | 3964000 |
| mod | int32 | 3968000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | ptr64 | 10 |
| unary | unknown | 6 |
| if | int1 | 4001 |
| loop_for | int32 | 7932000 |
| call | unknown | 8020 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 3966202 | 2 | 7926202 | 7 |
| add | 3960000 | 0 | 7920000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3960000 | 0 | 7920000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3964000 | 0 | 0 | 0 |
| mod | 3964000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 3964000 | 4000 | 3964000 | 0 |
| call | 0 | 8006 | 0 | 14 |
