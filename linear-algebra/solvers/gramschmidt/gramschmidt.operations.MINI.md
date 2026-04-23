# Static Operation Report: gramschmidt

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 3560 |
| add | 2736 |
| sub | 0 |
| mul | 1200 |
| mul_const | 2103 |
| div | 600 |
| div_const | 600 |
| mod | 2100 |
| cmp | 1501 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 1501 |
| loop_for | 4330 |
| call | 3046 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 3360 |
| assign | int32 | 197 |
| assign | ptr64 | 3 |
| add | float64 | 1200 |
| add | int32 | 1536 |
| mul | float64 | 600 |
| mul | int32 | 600 |
| mul_const | float64 | 600 |
| mul_const | int32 | 1503 |
| div | float64 | 600 |
| div_const | float64 | 600 |
| mod | int32 | 2100 |
| cmp | int32 | 1501 |
| logical | int32 | 1 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 1501 |
| loop_for | int32 | 4330 |
| call | unknown | 3046 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 2152 | 52 | 1351 | 5 |
| add | 600 | 1500 | 630 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 600 | 0 | 600 | 0 |
| mul_const | 600 | 1500 | 0 | 3 |
| div | 0 | 0 | 600 | 0 |
| div_const | 600 | 0 | 0 | 0 |
| mod | 600 | 1500 | 0 | 0 |
| cmp | 0 | 1500 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 1500 | 0 | 1 |
| loop_for | 1550 | 1550 | 1230 | 0 |
| call | 0 | 3006 | 30 | 10 |

## Static Resolution Warnings

- kernel_gramschmidt: unresolved loop bound
