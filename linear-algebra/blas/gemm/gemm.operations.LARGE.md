# Static Operation Report: gemm

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1325926213 |
| add | 1324720006 |
| sub | 0 |
| mul | 2644720000 |
| mul_const | 1100003 |
| div | 0 |
| div_const | 3620000 |
| mod | 4720000 |
| cmp | 1100001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 1100001 |
| loop_for | 1327025200 |
| call | 2200014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1324720000 |
| assign | int32 | 1206208 |
| assign | ptr64 | 5 |
| add | float64 | 1320000000 |
| add | int32 | 4720006 |
| mul | float64 | 2641100000 |
| mul | int32 | 3620000 |
| mul_const | int32 | 1100003 |
| div_const | float64 | 3620000 |
| mod | int32 | 4720000 |
| cmp | int32 | 1100001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 1100001 |
| loop_for | int32 | 1327025200 |
| call | unknown | 2200014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemm | main |
|---|---:|---:|---:|---:|
| assign | 3623205 | 1001 | 1322302001 | 6 |
| add | 3620000 | 1100000 | 1320000000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3620000 | 0 | 2641100000 | 0 |
| mul_const | 0 | 1100000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3620000 | 0 | 0 | 0 |
| mod | 3620000 | 1100000 | 0 | 0 |
| cmp | 0 | 1100000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 1100000 | 0 | 1 |
| loop_for | 3623200 | 1101000 | 1322301000 | 0 |
| call | 0 | 2200004 | 0 | 10 |
