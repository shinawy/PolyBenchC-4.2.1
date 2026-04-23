# Static Operation Report: adi

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 839022 |
| add | 1891050 |
| sub | 1906080 |
| mul | 269120 |
| mul_const | 1887448 |
| div | 538240 |
| div_const | 3607 |
| mod | 3600 |
| cmp | 3601 |
| logical | 1 |
| bitwise | 0 |
| unary | 538253 |
| if | 3601 |
| loop_for | 550240 |
| call | 7216 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 829533 |
| assign | int32 | 9485 |
| assign | ptr64 | 4 |
| add | float64 | 1345602 |
| add | int32 | 545448 |
| sub | float64 | 538240 |
| sub | int32 | 1367840 |
| mul | float64 | 269120 |
| mul_const | float64 | 1883844 |
| mul_const | int32 | 3604 |
| div | float64 | 538240 |
| div_const | float64 | 3607 |
| mod | int32 | 3600 |
| cmp | int32 | 3601 |
| logical | int32 | 1 |
| unary | float64 | 538242 |
| unary | ptr64 | 6 |
| unary | unknown | 5 |
| if | int1 | 3601 |
| loop_for | int32 | 550240 |
| call | unknown | 7216 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 3661 | 61 | 835294 | 6 |
| add | 3600 | 3600 | 1883842 | 8 |
| sub | 3600 | 0 | 1902480 | 0 |
| mul | 0 | 0 | 269120 | 0 |
| mul_const | 0 | 3600 | 1883844 | 4 |
| div | 0 | 0 | 538240 | 0 |
| div_const | 3600 | 0 | 7 | 0 |
| mod | 0 | 3600 | 0 | 0 |
| cmp | 0 | 3600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 538242 | 11 |
| if | 0 | 3600 | 0 | 1 |
| loop_for | 3660 | 3660 | 542920 | 0 |
| call | 0 | 7204 | 0 | 12 |
