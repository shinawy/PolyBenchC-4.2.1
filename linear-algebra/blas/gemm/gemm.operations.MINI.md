# Static Operation Report: gemm

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 18093 |
| add | 17356 |
| sub | 0 |
| mul | 32350 |
| mul_const | 503 |
| div | 0 |
| div_const | 1850 |
| mod | 2350 |
| cmp | 501 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 501 |
| loop_for | 18560 |
| call | 1014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 17350 |
| assign | int32 | 738 |
| assign | ptr64 | 5 |
| add | float64 | 15000 |
| add | int32 | 2356 |
| mul | float64 | 30500 |
| mul | int32 | 1850 |
| mul_const | int32 | 503 |
| div_const | float64 | 1850 |
| mod | int32 | 2350 |
| cmp | int32 | 501 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 501 |
| loop_for | int32 | 18560 |
| call | unknown | 1014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemm | main |
|---|---:|---:|---:|---:|
| assign | 1925 | 21 | 16141 | 6 |
| add | 1850 | 500 | 15000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1850 | 0 | 30500 | 0 |
| mul_const | 0 | 500 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1850 | 0 | 0 | 0 |
| mod | 1850 | 500 | 0 | 0 |
| cmp | 0 | 500 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 500 | 0 | 1 |
| loop_for | 1920 | 520 | 16120 | 0 |
| call | 0 | 1004 | 0 | 10 |
