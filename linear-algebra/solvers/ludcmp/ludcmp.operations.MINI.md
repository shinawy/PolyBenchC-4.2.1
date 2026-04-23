# Static Operation Report: ludcmp

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 69496 |
| add | 64167 |
| sub | 1 |
| mul | 64000 |
| mul_const | 2 |
| div | 40 |
| div_const | 80 |
| mod | 40 |
| cmp | 41 |
| logical | 1 |
| bitwise | 0 |
| unary | 67215 |
| if | 41 |
| loop_for | 69160 |
| call | 98 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1921 |
| assign | int32 | 1970 |
| assign | ptr64 | 65605 |
| add | float64 | 40 |
| add | int32 | 127 |
| add | ptr64 | 64000 |
| sub | int32 | 1 |
| mul | float64 | 64000 |
| mul_const | int32 | 2 |
| div | float64 | 40 |
| div_const | float64 | 80 |
| mod | int32 | 40 |
| cmp | int32 | 41 |
| logical | int32 | 1 |
| unary | ptr64 | 67209 |
| unary | unknown | 6 |
| if | int1 | 41 |
| loop_for | int32 | 69160 |
| call | unknown | 98 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 69167 | 1 | 323 | 5 |
| add | 64122 | 0 | 40 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 64000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 40 | 0 |
| div_const | 80 | 0 | 0 | 0 |
| mod | 0 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 67201 | 0 | 0 | 14 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 69000 | 40 | 120 | 0 |
| call | 2 | 84 | 0 | 12 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
