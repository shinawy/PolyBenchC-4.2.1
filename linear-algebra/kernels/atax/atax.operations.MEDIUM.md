# Static Operation Report: atax

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 482092 |
| add | 480115 |
| sub | 0 |
| mul | 319800 |
| mul_const | 159901 |
| div | 0 |
| div_const | 160310 |
| mod | 160310 |
| cmp | 411 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 411 |
| loop_for | 481710 |
| call | 836 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 480911 |
| assign | int32 | 1177 |
| assign | ptr64 | 4 |
| add | float64 | 320210 |
| add | int32 | 159905 |
| mul | float64 | 319800 |
| mul_const | int32 | 159901 |
| div_const | float64 | 160310 |
| mod | int32 | 160310 |
| cmp | int32 | 411 |
| logical | int32 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 411 |
| loop_for | int32 | 481710 |
| call | unknown | 836 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 160703 | 1 | 321382 | 6 |
| add | 160310 | 0 | 319800 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 319800 | 0 |
| mul_const | 159900 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 160310 | 0 | 0 | 0 |
| mod | 159900 | 410 | 0 | 0 |
| cmp | 0 | 410 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 410 | 0 | 1 |
| loop_for | 160700 | 410 | 320600 | 0 |
| call | 0 | 824 | 0 | 12 |
