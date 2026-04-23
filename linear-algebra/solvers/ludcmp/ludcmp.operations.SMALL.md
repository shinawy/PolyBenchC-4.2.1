# Static Operation Report: ludcmp

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1773256 |
| add | 1728487 |
| sub | 1 |
| mul | 1728000 |
| mul_const | 2 |
| div | 120 |
| div_const | 240 |
| mod | 120 |
| cmp | 121 |
| logical | 1 |
| bitwise | 0 |
| unary | 1756815 |
| if | 121 |
| loop_for | 1772280 |
| call | 258 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 15361 |
| assign | int32 | 15490 |
| assign | ptr64 | 1742405 |
| add | float64 | 120 |
| add | int32 | 367 |
| add | ptr64 | 1728000 |
| sub | int32 | 1 |
| mul | float64 | 1728000 |
| mul_const | int32 | 2 |
| div | float64 | 120 |
| div_const | float64 | 240 |
| mod | int32 | 120 |
| cmp | int32 | 121 |
| logical | int32 | 1 |
| unary | ptr64 | 1756809 |
| unary | unknown | 6 |
| if | int1 | 121 |
| loop_for | int32 | 1772280 |
| call | unknown | 258 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 1772287 | 1 | 963 | 5 |
| add | 1728362 | 0 | 120 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 1728000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 120 | 0 |
| div_const | 240 | 0 | 0 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1756801 | 0 | 0 | 14 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 1771800 | 120 | 360 | 0 |
| call | 2 | 244 | 0 | 12 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
