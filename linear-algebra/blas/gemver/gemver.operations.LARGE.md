# Static Operation Report: gemver

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 16026019 |
| add | 16012010 |
| sub | 0 |
| mul | 28000000 |
| mul_const | 1 |
| div | 0 |
| div_const | 4020000 |
| mod | 4002000 |
| cmp | 2001 |
| logical | 1 |
| bitwise | 0 |
| unary | 33 |
| if | 2001 |
| loop_for | 16012000 |
| call | 4026 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 16018001 |
| assign | int32 | 8007 |
| assign | ptr64 | 11 |
| add | float64 | 16002000 |
| add | int32 | 10010 |
| mul | float64 | 24000000 |
| mul | int32 | 4000000 |
| mul_const | int32 | 1 |
| div_const | float64 | 4020000 |
| mod | int32 | 4002000 |
| cmp | int32 | 2001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 21 |
| unary | unknown | 10 |
| if | int1 | 2001 |
| loop_for | int32 | 16012000 |
| call | unknown | 4026 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 4018004 | 1 | 12008004 | 10 |
| add | 10000 | 0 | 16002000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4000000 | 0 | 24000000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4020000 | 0 | 0 | 0 |
| mod | 4000000 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 4002000 | 2000 | 12008000 | 0 |
| call | 0 | 4004 | 0 | 22 |
