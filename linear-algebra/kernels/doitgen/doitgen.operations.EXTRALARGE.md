# Static Operation Report: doitgen

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 4069193930 |
| add | 4054050006 |
| sub | 0 |
| mul | 4024422900 |
| mul_const | 44550003 |
| div | 0 |
| div_const | 14922900 |
| mod | 29772900 |
| cmp | 14850001 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 14850001 |
| loop_for | 4069138920 |
| call | 29700014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4054122900 |
| assign | int32 | 15071027 |
| assign | ptr64 | 3 |
| add | float64 | 4009500000 |
| add | int32 | 44550006 |
| mul | float64 | 4009500000 |
| mul | int32 | 14922900 |
| mul_const | int32 | 44550003 |
| div_const | float64 | 14922900 |
| mod | int32 | 29772900 |
| cmp | int32 | 14850001 |
| logical | int32 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 14850001 |
| loop_for | int32 | 4069138920 |
| call | unknown | 29700014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 14978422 | 55251 | 4054160251 | 6 |
| add | 14850000 | 29700000 | 4009500000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14922900 | 0 | 4009500000 | 0 |
| mul_const | 0 | 44550000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14922900 | 0 | 0 | 0 |
| mod | 14922900 | 14850000 | 0 | 0 |
| cmp | 0 | 14850000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 14850000 | 0 | 1 |
| loop_for | 14978420 | 14905250 | 4039255250 | 0 |
| call | 0 | 29700004 | 0 | 10 |
