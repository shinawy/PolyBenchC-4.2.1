# Static Operation Report: floyd-warshall

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 21975528405 |
| add | 43943200002 |
| sub | 0 |
| mul | 7840000 |
| mul_const | 7840001 |
| div | 0 |
| div_const | 0 |
| mod | 39200000 |
| cmp | 21983360001 |
| logical | 15680001 |
| bitwise | 0 |
| unary | 5 |
| if | 21967680001 |
| loop_for | 21975528400 |
| call | 15680010 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | int32 | 21975528404 |
| assign | ptr64 | 1 |
| add | int32 | 43943200002 |
| mul | int32 | 7840000 |
| mul_const | int32 | 7840001 |
| mod | int32 | 39200000 |
| cmp | int32 | 21983360001 |
| logical | int32 | 15680001 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 21967680001 |
| loop_for | int32 | 21975528400 |
| call | unknown | 15680010 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 15682801 | 2801 | 21959842801 | 2 |
| add | 31360000 | 7840000 | 43904000000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 7840000 | 0 | 0 | 0 |
| mul_const | 0 | 7840000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 31360000 | 7840000 | 0 | 0 |
| cmp | 23520000 | 7840000 | 21952000000 | 1 |
| logical | 15680000 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 7840000 | 7840000 | 21952000000 | 1 |
| loop_for | 7842800 | 7842800 | 21959842800 | 0 |
| call | 0 | 15680004 | 0 | 6 |
