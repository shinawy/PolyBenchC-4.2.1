# Static Operation Report: floyd-warshall

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 125751505 |
| add | 251250002 |
| sub | 0 |
| mul | 250000 |
| mul_const | 250001 |
| div | 0 |
| div_const | 0 |
| mod | 1250000 |
| cmp | 126000001 |
| logical | 500001 |
| bitwise | 0 |
| unary | 5 |
| if | 125500001 |
| loop_for | 125751500 |
| call | 500010 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | int32 | 125751504 |
| assign | ptr64 | 1 |
| add | int32 | 251250002 |
| mul | int32 | 250000 |
| mul_const | int32 | 250001 |
| mod | int32 | 1250000 |
| cmp | int32 | 126000001 |
| logical | int32 | 500001 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 125500001 |
| loop_for | int32 | 125751500 |
| call | unknown | 500010 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 500501 | 501 | 125250501 | 2 |
| add | 1000000 | 250000 | 250000000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 250000 | 0 | 0 | 0 |
| mul_const | 0 | 250000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 1000000 | 250000 | 0 | 0 |
| cmp | 750000 | 250000 | 125000000 | 1 |
| logical | 500000 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 250000 | 250000 | 125000000 | 1 |
| loop_for | 250500 | 250500 | 125250500 | 0 |
| call | 0 | 500004 | 0 | 6 |
