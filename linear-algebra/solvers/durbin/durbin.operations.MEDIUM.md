# Static Operation Report: durbin

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 3202 |
| add | 801 |
| sub | 799 |
| mul | 399 |
| mul_const | 399 |
| div | 0 |
| div_const | 399 |
| mod | 400 |
| cmp | 401 |
| logical | 1 |
| bitwise | 0 |
| unary | 408 |
| if | 401 |
| loop_for | 1199 |
| call | 812 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1999 |
| assign | int32 | 1201 |
| assign | ptr64 | 2 |
| add | float64 | 399 |
| add | int32 | 402 |
| sub | float64 | 399 |
| sub | int32 | 400 |
| mul | float64 | 399 |
| mul_const | float64 | 399 |
| div_const | float64 | 399 |
| mod | int32 | 400 |
| cmp | int32 | 401 |
| logical | int32 | 1 |
| unary | float64 | 401 |
| unary | ptr64 | 4 |
| unary | unknown | 3 |
| if | int1 | 401 |
| loop_for | int32 | 1199 |
| call | unknown | 812 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 401 | 1 | 2797 | 3 |
| add | 400 | 0 | 399 | 2 |
| sub | 400 | 0 | 399 | 0 |
| mul | 0 | 0 | 399 | 0 |
| mul_const | 0 | 0 | 399 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 399 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 401 | 7 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 400 | 400 | 399 | 0 |
| call | 0 | 804 | 0 | 8 |

## Static Resolution Warnings

- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
