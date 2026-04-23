# Static Operation Report: gesummv

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 251511 |
| add | 250257 |
| sub | 0 |
| mul | 250500 |
| mul_const | 2 |
| div | 0 |
| div_const | 125250 |
| mod | 125500 |
| cmp | 251 |
| logical | 1 |
| bitwise | 0 |
| unary | 19 |
| if | 251 |
| loop_for | 125750 |
| call | 518 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 251000 |
| assign | int32 | 504 |
| assign | ptr64 | 7 |
| add | float64 | 125250 |
| add | int32 | 125007 |
| mul | float64 | 125500 |
| mul | int32 | 125000 |
| mul_const | int32 | 2 |
| div_const | float64 | 125250 |
| mod | int32 | 125500 |
| cmp | int32 | 251 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 11 |
| unary | unknown | 6 |
| if | int1 | 251 |
| loop_for | int32 | 125750 |
| call | unknown | 518 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 125503 | 1 | 126001 | 6 |
| add | 125000 | 0 | 125250 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 125000 | 0 | 125500 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 125250 | 0 | 0 | 0 |
| mod | 125250 | 250 | 0 | 0 |
| cmp | 0 | 250 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 250 | 0 | 1 |
| loop_for | 62750 | 250 | 62750 | 0 |
| call | 0 | 504 | 0 | 14 |
