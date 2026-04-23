# Static Operation Report: durbin

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 322 |
| add | 81 |
| sub | 79 |
| mul | 39 |
| mul_const | 39 |
| div | 0 |
| div_const | 39 |
| mod | 40 |
| cmp | 41 |
| logical | 1 |
| bitwise | 0 |
| unary | 48 |
| if | 41 |
| loop_for | 119 |
| call | 92 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 199 |
| assign | int32 | 121 |
| assign | ptr64 | 2 |
| add | float64 | 39 |
| add | int32 | 42 |
| sub | float64 | 39 |
| sub | int32 | 40 |
| mul | float64 | 39 |
| mul_const | float64 | 39 |
| div_const | float64 | 39 |
| mod | int32 | 40 |
| cmp | int32 | 41 |
| logical | int32 | 1 |
| unary | float64 | 41 |
| unary | ptr64 | 4 |
| unary | unknown | 3 |
| if | int1 | 41 |
| loop_for | int32 | 119 |
| call | unknown | 92 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 41 | 1 | 277 | 3 |
| add | 40 | 0 | 39 | 2 |
| sub | 40 | 0 | 39 | 0 |
| mul | 0 | 0 | 39 | 0 |
| mul_const | 0 | 0 | 39 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 39 | 0 |
| mod | 0 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 41 | 7 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 40 | 40 | 39 | 0 |
| call | 0 | 84 | 0 | 8 |

## Static Resolution Warnings

- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
