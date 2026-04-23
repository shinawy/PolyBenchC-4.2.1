# Static Operation Report: covariance

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2903 |
| add | 1685 |
| sub | 896 |
| mul | 896 |
| mul_const | 786 |
| div | 28 |
| div_const | 896 |
| mod | 784 |
| cmp | 785 |
| logical | 1 |
| bitwise | 0 |
| unary | 11 |
| if | 785 |
| loop_for | 3620 |
| call | 1582 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2744 |
| assign | int32 | 155 |
| assign | ptr64 | 4 |
| add | float64 | 896 |
| add | int32 | 789 |
| sub | float64 | 896 |
| mul | float64 | 896 |
| mul_const | int32 | 786 |
| div | float64 | 28 |
| div_const | float64 | 896 |
| mod | int32 | 784 |
| cmp | int32 | 785 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 785 |
| loop_for | int32 | 3620 |
| call | unknown | 1582 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 930 | 29 | 1939 | 5 |
| add | 0 | 784 | 896 | 5 |
| sub | 0 | 0 | 896 | 0 |
| mul | 896 | 0 | 0 | 0 |
| mul_const | 0 | 784 | 0 | 2 |
| div | 0 | 0 | 28 | 0 |
| div_const | 896 | 0 | 0 | 0 |
| mod | 0 | 784 | 0 | 0 |
| cmp | 0 | 784 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 784 | 0 | 1 |
| loop_for | 928 | 812 | 1880 | 0 |
| call | 0 | 1572 | 0 | 10 |

## Static Resolution Warnings

- kernel_covariance: unresolved loop bound
