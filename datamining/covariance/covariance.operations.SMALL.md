# Static Operation Report: covariance

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 24611 |
| add | 14405 |
| sub | 8000 |
| mul | 8000 |
| mul_const | 6402 |
| div | 80 |
| div_const | 8000 |
| mod | 6400 |
| cmp | 6401 |
| logical | 1 |
| bitwise | 0 |
| unary | 11 |
| if | 6401 |
| loop_for | 30840 |
| call | 12814 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 24160 |
| assign | int32 | 447 |
| assign | ptr64 | 4 |
| add | float64 | 8000 |
| add | int32 | 6405 |
| sub | float64 | 8000 |
| mul | float64 | 8000 |
| mul_const | int32 | 6402 |
| div | float64 | 80 |
| div_const | float64 | 8000 |
| mod | int32 | 6400 |
| cmp | int32 | 6401 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 6401 |
| loop_for | int32 | 30840 |
| call | unknown | 12814 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 8102 | 81 | 16423 | 5 |
| add | 0 | 6400 | 8000 | 5 |
| sub | 0 | 0 | 8000 | 0 |
| mul | 8000 | 0 | 0 | 0 |
| mul_const | 0 | 6400 | 0 | 2 |
| div | 0 | 0 | 80 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 6400 | 0 | 1 |
| loop_for | 8100 | 6480 | 16260 | 0 |
| call | 0 | 12804 | 0 | 10 |

## Static Resolution Warnings

- kernel_covariance: unresolved loop bound
