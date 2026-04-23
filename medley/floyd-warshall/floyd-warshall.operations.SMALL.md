# Static Operation Report: floyd-warshall

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 5929745 |
| add | 11826002 |
| sub | 0 |
| mul | 32400 |
| mul_const | 32401 |
| div | 0 |
| div_const | 0 |
| mod | 162000 |
| cmp | 5961601 |
| logical | 64801 |
| bitwise | 0 |
| unary | 5 |
| if | 5896801 |
| loop_for | 5929740 |
| call | 64810 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | int32 | 5929744 |
| assign | ptr64 | 1 |
| add | int32 | 11826002 |
| mul | int32 | 32400 |
| mul_const | int32 | 32401 |
| mod | int32 | 162000 |
| cmp | int32 | 5961601 |
| logical | int32 | 64801 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 5896801 |
| loop_for | int32 | 5929740 |
| call | unknown | 64810 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 64981 | 181 | 5864581 | 2 |
| add | 129600 | 32400 | 11664000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 32400 | 0 | 0 | 0 |
| mul_const | 0 | 32400 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 129600 | 32400 | 0 | 0 |
| cmp | 97200 | 32400 | 5832000 | 1 |
| logical | 64800 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 32400 | 32400 | 5832000 | 1 |
| loop_for | 32580 | 32580 | 5864580 | 0 |
| call | 0 | 64804 | 0 | 6 |
