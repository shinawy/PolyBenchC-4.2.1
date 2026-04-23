# Static Operation Report: covariance

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 23419011 |
| add | 14560005 |
| sub | 7800000 |
| mul | 7800000 |
| mul_const | 6760002 |
| div | 2600 |
| div_const | 7800000 |
| mod | 6760000 |
| cmp | 6760001 |
| logical | 1 |
| bitwise | 0 |
| unary | 11 |
| if | 6760001 |
| loop_for | 30173800 |
| call | 13520014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 23405200 |
| assign | int32 | 13807 |
| assign | ptr64 | 4 |
| add | float64 | 7800000 |
| add | int32 | 6760005 |
| sub | float64 | 7800000 |
| mul | float64 | 7800000 |
| mul_const | int32 | 6760002 |
| div | float64 | 2600 |
| div_const | float64 | 7800000 |
| mod | int32 | 6760000 |
| cmp | int32 | 6760001 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 6760001 |
| loop_for | int32 | 30173800 |
| call | unknown | 13520014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 7803002 | 2601 | 15613403 | 5 |
| add | 0 | 6760000 | 7800000 | 5 |
| sub | 0 | 0 | 7800000 | 0 |
| mul | 7800000 | 0 | 0 | 0 |
| mul_const | 0 | 6760000 | 0 | 2 |
| div | 0 | 0 | 2600 | 0 |
| div_const | 7800000 | 0 | 0 | 0 |
| mod | 0 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 6760000 | 0 | 1 |
| loop_for | 7803000 | 6762600 | 15608200 | 0 |
| call | 0 | 13520004 | 0 | 10 |

## Static Resolution Warnings

- kernel_covariance: unresolved loop bound
