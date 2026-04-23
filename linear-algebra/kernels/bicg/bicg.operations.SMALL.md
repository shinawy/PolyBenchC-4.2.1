# Static Operation Report: bicg

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 43893 |
| add | 43158 |
| sub | 0 |
| mul | 43152 |
| mul_const | 1 |
| div | 0 |
| div_const | 14624 |
| mod | 14864 |
| cmp | 241 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 241 |
| loop_for | 29488 |
| call | 500 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 43632 |
| assign | int32 | 256 |
| assign | ptr64 | 5 |
| add | float64 | 28768 |
| add | int32 | 14390 |
| mul | float64 | 28768 |
| mul | int32 | 14384 |
| mul_const | int32 | 1 |
| div_const | float64 | 14624 |
| mod | int32 | 14864 |
| cmp | int32 | 241 |
| logical | int32 | 1 |
| unary | ptr64 | 10 |
| unary | unknown | 6 |
| if | int1 | 241 |
| loop_for | int32 | 29488 |
| call | unknown | 500 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 14750 | 2 | 29134 | 7 |
| add | 14384 | 0 | 28768 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14384 | 0 | 28768 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14624 | 0 | 0 | 0 |
| mod | 14624 | 240 | 0 | 0 |
| cmp | 0 | 240 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 240 | 0 | 1 |
| loop_for | 14624 | 240 | 14624 | 0 |
| call | 0 | 486 | 0 | 14 |
