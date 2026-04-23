# Static Operation Report: gemver

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 59179 |
| add | 58330 |
| sub | 0 |
| mul | 100800 |
| mul_const | 1 |
| div | 0 |
| div_const | 15600 |
| mod | 14520 |
| cmp | 121 |
| logical | 1 |
| bitwise | 0 |
| unary | 33 |
| if | 121 |
| loop_for | 58320 |
| call | 266 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 58681 |
| assign | int32 | 487 |
| assign | ptr64 | 11 |
| add | float64 | 57720 |
| add | int32 | 610 |
| mul | float64 | 86400 |
| mul | int32 | 14400 |
| mul_const | int32 | 1 |
| div_const | float64 | 15600 |
| mod | int32 | 14520 |
| cmp | int32 | 121 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 21 |
| unary | unknown | 10 |
| if | int1 | 121 |
| loop_for | int32 | 58320 |
| call | unknown | 266 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 15484 | 1 | 43684 | 10 |
| add | 600 | 0 | 57720 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14400 | 0 | 86400 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15600 | 0 | 0 | 0 |
| mod | 14400 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 14520 | 120 | 43680 | 0 |
| call | 0 | 244 | 0 | 22 |
