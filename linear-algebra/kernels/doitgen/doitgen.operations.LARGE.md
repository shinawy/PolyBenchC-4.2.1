# Static Operation Report: doitgen

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 551150220 |
| add | 547680006 |
| sub | 0 |
| mul | 540985600 |
| mul_const | 10080003 |
| div | 0 |
| div_const | 3385600 |
| mod | 6745600 |
| cmp | 3360001 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 3360001 |
| loop_for | 551129210 |
| call | 6720014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 547705600 |
| assign | int32 | 3444617 |
| assign | ptr64 | 3 |
| add | float64 | 537600000 |
| add | int32 | 10080006 |
| mul | float64 | 537600000 |
| mul | int32 | 3385600 |
| mul_const | int32 | 10080003 |
| div_const | float64 | 3385600 |
| mod | int32 | 6745600 |
| cmp | int32 | 3360001 |
| logical | int32 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 3360001 |
| loop_for | int32 | 551129210 |
| call | unknown | 6720014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 3406912 | 21151 | 547722151 | 6 |
| add | 3360000 | 6720000 | 537600000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3385600 | 0 | 537600000 | 0 |
| mul_const | 0 | 10080000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3385600 | 0 | 0 | 0 |
| mod | 3385600 | 3360000 | 0 | 0 |
| cmp | 0 | 3360000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 3360000 | 0 | 1 |
| loop_for | 3406910 | 3381150 | 544341150 | 0 |
| call | 0 | 6720004 | 0 | 10 |
