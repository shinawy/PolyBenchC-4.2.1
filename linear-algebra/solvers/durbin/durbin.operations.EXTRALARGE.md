# Static Operation Report: durbin

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 32002 |
| add | 8001 |
| sub | 7999 |
| mul | 3999 |
| mul_const | 3999 |
| div | 0 |
| div_const | 3999 |
| mod | 4000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 4008 |
| if | 4001 |
| loop_for | 11999 |
| call | 8012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 19999 |
| assign | int32 | 12001 |
| assign | ptr64 | 2 |
| add | float64 | 3999 |
| add | int32 | 4002 |
| sub | float64 | 3999 |
| sub | int32 | 4000 |
| mul | float64 | 3999 |
| mul_const | float64 | 3999 |
| div_const | float64 | 3999 |
| mod | int32 | 4000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | float64 | 4001 |
| unary | ptr64 | 4 |
| unary | unknown | 3 |
| if | int1 | 4001 |
| loop_for | int32 | 11999 |
| call | unknown | 8012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 4001 | 1 | 27997 | 3 |
| add | 4000 | 0 | 3999 | 2 |
| sub | 4000 | 0 | 3999 | 0 |
| mul | 0 | 0 | 3999 | 0 |
| mul_const | 0 | 0 | 3999 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 3999 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 4001 | 7 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4000 | 4000 | 3999 | 0 |
| call | 0 | 8004 | 0 | 8 |

## Static Resolution Warnings

- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
