# Static Operation Report: 2mm

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 16294 |
| add | 15638 |
| sub | 0 |
| mul | 21532 |
| mul_const | 389 |
| div | 0 |
| div_const | 1564 |
| mod | 1948 |
| cmp | 385 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 385 |
| loop_for | 15988 |
| call | 786 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 15484 |
| assign | int32 | 803 |
| assign | ptr64 | 7 |
| add | float64 | 13248 |
| add | int32 | 2390 |
| mul | float64 | 19968 |
| mul | int32 | 1564 |
| mul_const | int32 | 389 |
| div_const | float64 | 1564 |
| mod | int32 | 1948 |
| cmp | int32 | 385 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 385 |
| loop_for | int32 | 15988 |
| call | unknown | 786 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 1642 | 17 | 14626 | 9 |
| add | 1996 | 384 | 13248 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1564 | 0 | 19968 | 0 |
| mul_const | 0 | 384 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1564 | 0 | 0 | 0 |
| mod | 1564 | 384 | 0 | 0 |
| cmp | 0 | 384 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 384 | 0 | 1 |
| loop_for | 1636 | 400 | 13952 | 0 |
| call | 0 | 772 | 0 | 14 |
