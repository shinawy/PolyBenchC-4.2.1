# Static Operation Report: gemm

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 11985592613 |
| add | 11980380006 |
| sub | 0 |
| mul | 23940380000 |
| mul_const | 4600003 |
| div | 0 |
| div_const | 15780000 |
| mod | 20380000 |
| cmp | 4600001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 4600001 |
| loop_for | 11990190600 |
| call | 9200014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11980380000 |
| assign | int32 | 5212608 |
| assign | ptr64 | 5 |
| add | float64 | 11960000000 |
| add | int32 | 20380006 |
| mul | float64 | 23924600000 |
| mul | int32 | 15780000 |
| mul_const | int32 | 4600003 |
| div_const | float64 | 15780000 |
| mod | int32 | 20380000 |
| cmp | int32 | 4600001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 4600001 |
| loop_for | int32 | 11990190600 |
| call | unknown | 9200014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemm | main |
|---|---:|---:|---:|---:|
| assign | 15786605 | 2001 | 11969804001 | 6 |
| add | 15780000 | 4600000 | 11960000000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15780000 | 0 | 23924600000 | 0 |
| mul_const | 0 | 4600000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15780000 | 0 | 0 | 0 |
| mod | 15780000 | 4600000 | 0 | 0 |
| cmp | 0 | 4600000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 4600000 | 0 | 1 |
| loop_for | 15786600 | 4602000 | 11969802000 | 0 |
| call | 0 | 9200004 | 0 | 10 |
