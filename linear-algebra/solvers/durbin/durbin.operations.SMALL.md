# Static Operation Report: durbin

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 962 |
| add | 241 |
| sub | 239 |
| mul | 119 |
| mul_const | 119 |
| div | 0 |
| div_const | 119 |
| mod | 120 |
| cmp | 121 |
| logical | 1 |
| bitwise | 0 |
| unary | 128 |
| if | 121 |
| loop_for | 359 |
| call | 252 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 599 |
| assign | int32 | 361 |
| assign | ptr64 | 2 |
| add | float64 | 119 |
| add | int32 | 122 |
| sub | float64 | 119 |
| sub | int32 | 120 |
| mul | float64 | 119 |
| mul_const | float64 | 119 |
| div_const | float64 | 119 |
| mod | int32 | 120 |
| cmp | int32 | 121 |
| logical | int32 | 1 |
| unary | float64 | 121 |
| unary | ptr64 | 4 |
| unary | unknown | 3 |
| if | int1 | 121 |
| loop_for | int32 | 359 |
| call | unknown | 252 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 121 | 1 | 837 | 3 |
| add | 120 | 0 | 119 | 2 |
| sub | 120 | 0 | 119 | 0 |
| mul | 0 | 0 | 119 | 0 |
| mul_const | 0 | 0 | 119 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 119 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 121 | 7 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 120 | 120 | 119 | 0 |
| call | 0 | 244 | 0 | 8 |

## Static Resolution Warnings

- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
