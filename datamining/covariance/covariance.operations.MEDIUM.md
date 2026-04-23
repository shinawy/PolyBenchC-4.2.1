# Static Operation Report: covariance

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 188931 |
| add | 120005 |
| sub | 62400 |
| mul | 62400 |
| mul_const | 57602 |
| div | 240 |
| div_const | 62400 |
| mod | 57600 |
| cmp | 57601 |
| logical | 1 |
| bitwise | 0 |
| unary | 11 |
| if | 57601 |
| loop_for | 246040 |
| call | 115214 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 187680 |
| assign | int32 | 1247 |
| assign | ptr64 | 4 |
| add | float64 | 62400 |
| add | int32 | 57605 |
| sub | float64 | 62400 |
| mul | float64 | 62400 |
| mul_const | int32 | 57602 |
| div | float64 | 240 |
| div_const | float64 | 62400 |
| mod | int32 | 57600 |
| cmp | int32 | 57601 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 57601 |
| loop_for | int32 | 246040 |
| call | unknown | 115214 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 62662 | 241 | 126023 | 5 |
| add | 0 | 57600 | 62400 | 5 |
| sub | 0 | 0 | 62400 | 0 |
| mul | 62400 | 0 | 0 | 0 |
| mul_const | 0 | 57600 | 0 | 2 |
| div | 0 | 0 | 240 | 0 |
| div_const | 62400 | 0 | 0 | 0 |
| mod | 0 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 57600 | 0 | 1 |
| loop_for | 62660 | 57840 | 125540 | 0 |
| call | 0 | 115204 | 0 | 10 |

## Static Resolution Warnings

- kernel_covariance: unresolved loop bound
