# Static Operation Report: ludcmp

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 64486816 |
| add | 64001607 |
| sub | 1 |
| mul | 64000000 |
| mul_const | 2 |
| div | 400 |
| div_const | 800 |
| mod | 400 |
| cmp | 401 |
| logical | 1 |
| bitwise | 0 |
| unary | 64320015 |
| if | 401 |
| loop_for | 64483600 |
| call | 818 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 163201 |
| assign | int32 | 163610 |
| assign | ptr64 | 64160005 |
| add | float64 | 400 |
| add | int32 | 1207 |
| add | ptr64 | 64000000 |
| sub | int32 | 1 |
| mul | float64 | 64000000 |
| mul_const | int32 | 2 |
| div | float64 | 400 |
| div_const | float64 | 800 |
| mod | int32 | 400 |
| cmp | int32 | 401 |
| logical | int32 | 1 |
| unary | ptr64 | 64320009 |
| unary | unknown | 6 |
| if | int1 | 401 |
| loop_for | int32 | 64483600 |
| call | unknown | 818 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 64483607 | 1 | 3203 | 5 |
| add | 64001202 | 0 | 400 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 64000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 400 | 0 |
| div_const | 800 | 0 | 0 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64320001 | 0 | 0 | 14 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 64482000 | 400 | 1200 | 0 |
| call | 2 | 804 | 0 | 12 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
