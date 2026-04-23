# Static Operation Report: trmm

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1908 |
| add | 1804 |
| sub | 600 |
| mul | 600 |
| mul_const | 602 |
| div | 0 |
| div_const | 600 |
| mod | 1200 |
| cmp | 601 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 601 |
| loop_for | 1860 |
| call | 1212 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1220 |
| assign | int32 | 685 |
| assign | ptr64 | 3 |
| add | int32 | 1804 |
| sub | int32 | 600 |
| mul | float64 | 600 |
| mul_const | int32 | 602 |
| div_const | float64 | 600 |
| mod | int32 | 1200 |
| cmp | int32 | 601 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 3 |
| if | int1 | 601 |
| loop_for | int32 | 1860 |
| call | unknown | 1212 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 662 | 21 | 1221 | 4 |
| add | 600 | 600 | 600 | 4 |
| sub | 600 | 0 | 0 | 0 |
| mul | 0 | 0 | 600 | 0 |
| mul_const | 0 | 600 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 600 | 0 | 0 | 0 |
| mod | 600 | 600 | 0 | 0 |
| cmp | 0 | 600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 600 | 0 | 1 |
| loop_for | 620 | 620 | 620 | 0 |
| call | 0 | 1204 | 0 | 8 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trmm: unresolved loop bound
