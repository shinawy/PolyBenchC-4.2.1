# Static Operation Report: gemver

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 6939 |
| add | 6650 |
| sub | 0 |
| mul | 11200 |
| mul_const | 1 |
| div | 0 |
| div_const | 2000 |
| mod | 1640 |
| cmp | 41 |
| logical | 1 |
| bitwise | 0 |
| unary | 33 |
| if | 41 |
| loop_for | 6640 |
| call | 106 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 6761 |
| assign | int32 | 167 |
| assign | ptr64 | 11 |
| add | float64 | 6440 |
| add | int32 | 210 |
| mul | float64 | 9600 |
| mul | int32 | 1600 |
| mul_const | int32 | 1 |
| div_const | float64 | 2000 |
| mod | int32 | 1640 |
| cmp | int32 | 41 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 21 |
| unary | unknown | 10 |
| if | int1 | 41 |
| loop_for | int32 | 6640 |
| call | unknown | 106 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 1964 | 1 | 4964 | 10 |
| add | 200 | 0 | 6440 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1600 | 0 | 9600 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2000 | 0 | 0 | 0 |
| mod | 1600 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 1640 | 40 | 4960 | 0 |
| call | 0 | 84 | 0 | 22 |
