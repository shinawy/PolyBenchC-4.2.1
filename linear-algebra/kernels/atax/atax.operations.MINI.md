# Static Operation Report: atax

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 5036 |
| add | 4835 |
| sub | 0 |
| mul | 3192 |
| mul_const | 1597 |
| div | 0 |
| div_const | 1638 |
| mod | 1638 |
| cmp | 43 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 43 |
| loop_for | 4990 |
| call | 100 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4911 |
| assign | int32 | 121 |
| assign | ptr64 | 4 |
| add | float64 | 3234 |
| add | int32 | 1601 |
| mul | float64 | 3192 |
| mul_const | int32 | 1597 |
| div_const | float64 | 1638 |
| mod | int32 | 1638 |
| cmp | int32 | 43 |
| logical | int32 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 43 |
| loop_for | int32 | 4990 |
| call | unknown | 100 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 1679 | 1 | 3350 | 6 |
| add | 1638 | 0 | 3192 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 3192 | 0 |
| mul_const | 1596 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1638 | 0 | 0 | 0 |
| mod | 1596 | 42 | 0 | 0 |
| cmp | 0 | 42 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 42 | 0 | 1 |
| loop_for | 1676 | 42 | 3272 | 0 |
| call | 0 | 88 | 0 | 12 |
