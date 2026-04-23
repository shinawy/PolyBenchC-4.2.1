# Static Operation Report: floyd-warshall

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 226985 |
| add | 450002 |
| sub | 0 |
| mul | 3600 |
| mul_const | 3601 |
| div | 0 |
| div_const | 0 |
| mod | 18000 |
| cmp | 230401 |
| logical | 7201 |
| bitwise | 0 |
| unary | 5 |
| if | 223201 |
| loop_for | 226980 |
| call | 7210 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | int32 | 226984 |
| assign | ptr64 | 1 |
| add | int32 | 450002 |
| mul | int32 | 3600 |
| mul_const | int32 | 3601 |
| mod | int32 | 18000 |
| cmp | int32 | 230401 |
| logical | int32 | 7201 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 223201 |
| loop_for | int32 | 226980 |
| call | unknown | 7210 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 7261 | 61 | 219661 | 2 |
| add | 14400 | 3600 | 432000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3600 | 0 | 0 | 0 |
| mul_const | 0 | 3600 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 14400 | 3600 | 0 | 0 |
| cmp | 10800 | 3600 | 216000 | 1 |
| logical | 7200 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 3600 | 3600 | 216000 | 1 |
| loop_for | 3660 | 3660 | 219660 | 0 |
| call | 0 | 7204 | 0 | 6 |
