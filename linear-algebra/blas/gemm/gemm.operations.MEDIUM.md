# Static Operation Report: gemm

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 10798053 |
| add | 10748806 |
| sub | 0 |
| mul | 21308800 |
| mul_const | 44003 |
| div | 0 |
| div_const | 144800 |
| mod | 188800 |
| cmp | 44001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 44001 |
| loop_for | 10841840 |
| call | 88014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 10748800 |
| assign | int32 | 49248 |
| assign | ptr64 | 5 |
| add | float64 | 10560000 |
| add | int32 | 188806 |
| mul | float64 | 21164000 |
| mul | int32 | 144800 |
| mul_const | int32 | 44003 |
| div_const | float64 | 144800 |
| mod | int32 | 188800 |
| cmp | int32 | 44001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 44001 |
| loop_for | int32 | 10841840 |
| call | unknown | 88014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemm | main |
|---|---:|---:|---:|---:|
| assign | 145445 | 201 | 10652401 | 6 |
| add | 144800 | 44000 | 10560000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 144800 | 0 | 21164000 | 0 |
| mul_const | 0 | 44000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 144800 | 0 | 0 | 0 |
| mod | 144800 | 44000 | 0 | 0 |
| cmp | 0 | 44000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 44000 | 0 | 1 |
| loop_for | 145440 | 44200 | 10652200 | 0 |
| call | 0 | 88004 | 0 | 10 |
