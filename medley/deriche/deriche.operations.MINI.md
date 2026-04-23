# Static Operation Report: deriche

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 87452 |
| add | 65546 |
| sub | 132 |
| mul | 12295 |
| mul_const | 73736 |
| div | 1 |
| div_const | 4096 |
| mod | 8192 |
| cmp | 4097 |
| logical | 1 |
| bitwise | 0 |
| unary | 24 |
| if | 4097 |
| loop_for | 33280 |
| call | 8217 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 86925 |
| assign | int32 | 522 |
| assign | ptr64 | 5 |
| add | float32 | 57346 |
| add | int32 | 8200 |
| sub | float32 | 4 |
| sub | int32 | 128 |
| mul | float32 | 12295 |
| mul_const | float32 | 61444 |
| mul_const | int32 | 12292 |
| div | float32 | 1 |
| div_const | float32 | 4096 |
| mod | int32 | 8192 |
| cmp | int32 | 4097 |
| logical | int32 | 1 |
| unary | float32 | 10 |
| unary | ptr64 | 8 |
| unary | unknown | 6 |
| if | int1 | 4097 |
| loop_for | int32 | 33280 |
| call | unknown | 8217 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_deriche | main |
|---|---:|---:|---:|---:|
| assign | 4162 | 65 | 83219 | 6 |
| add | 4096 | 4096 | 57346 | 8 |
| sub | 0 | 0 | 132 | 0 |
| mul | 0 | 0 | 12295 | 0 |
| mul_const | 8192 | 4096 | 61444 | 4 |
| div | 0 | 0 | 1 | 0 |
| div_const | 4096 | 0 | 0 | 0 |
| mod | 4096 | 4096 | 0 | 0 |
| cmp | 0 | 4096 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 10 | 13 |
| if | 0 | 4096 | 0 | 1 |
| loop_for | 4160 | 4160 | 24960 | 0 |
| call | 0 | 8196 | 9 | 12 |
