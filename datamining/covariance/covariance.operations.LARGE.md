# Static Operation Report: covariance

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 5048811 |
| add | 3120005 |
| sub | 1680000 |
| mul | 1680000 |
| mul_const | 1440002 |
| div | 1200 |
| div_const | 1680000 |
| mod | 1440000 |
| cmp | 1440001 |
| logical | 1 |
| bitwise | 0 |
| unary | 11 |
| if | 1440001 |
| loop_for | 6486400 |
| call | 2880014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 5042400 |
| assign | int32 | 6407 |
| assign | ptr64 | 4 |
| add | float64 | 1680000 |
| add | int32 | 1440005 |
| sub | float64 | 1680000 |
| mul | float64 | 1680000 |
| mul_const | int32 | 1440002 |
| div | float64 | 1200 |
| div_const | float64 | 1680000 |
| mod | int32 | 1440000 |
| cmp | int32 | 1440001 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 1440001 |
| loop_for | int32 | 6486400 |
| call | unknown | 2880014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 1681402 | 1201 | 3366203 | 5 |
| add | 0 | 1440000 | 1680000 | 5 |
| sub | 0 | 0 | 1680000 | 0 |
| mul | 1680000 | 0 | 0 | 0 |
| mul_const | 0 | 1440000 | 0 | 2 |
| div | 0 | 0 | 1200 | 0 |
| div_const | 1680000 | 0 | 0 | 0 |
| mod | 0 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 1440000 | 0 | 1 |
| loop_for | 1681400 | 1441200 | 3363800 | 0 |
| call | 0 | 2880004 | 0 | 10 |

## Static Resolution Warnings

- kernel_covariance: unresolved loop bound
