# Static Operation Report: symm

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 3111 |
| add | 3026 |
| sub | 600 |
| mul | 1800 |
| mul_const | 1203 |
| div | 0 |
| div_const | 1200 |
| mod | 1800 |
| cmp | 601 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 601 |
| loop_for | 1880 |
| call | 1214 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2400 |
| assign | int32 | 706 |
| assign | ptr64 | 5 |
| add | float64 | 1200 |
| add | int32 | 1826 |
| sub | int32 | 600 |
| mul | float64 | 1800 |
| mul_const | float64 | 600 |
| mul_const | int32 | 603 |
| div_const | float64 | 1200 |
| mod | int32 | 1800 |
| cmp | int32 | 601 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 601 |
| loop_for | int32 | 1880 |
| call | unknown | 1214 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 1264 | 21 | 1821 | 5 |
| add | 1220 | 600 | 1200 | 6 |
| sub | 600 | 0 | 0 | 0 |
| mul | 0 | 0 | 1800 | 0 |
| mul_const | 0 | 600 | 600 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1200 | 0 | 0 | 0 |
| mod | 1200 | 600 | 0 | 0 |
| cmp | 0 | 600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 600 | 0 | 1 |
| loop_for | 640 | 620 | 620 | 0 |
| call | 0 | 1204 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_symm: unresolved loop bound
