# Static Operation Report: cholesky

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1772409 |
| add | 1728124 |
| sub | 0 |
| mul | 1728000 |
| mul_const | 2 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 1 |
| logical | 1 |
| bitwise | 0 |
| unary | 1756806 |
| if | 1 |
| loop_for | 1771920 |
| call | 132 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 14640 |
| assign | int32 | 15367 |
| assign | ptr64 | 1742402 |
| add | int32 | 124 |
| add | ptr64 | 1728000 |
| mul | float64 | 1728000 |
| mul_const | int32 | 2 |
| cmp | int32 | 1 |
| logical | int32 | 1 |
| unary | ptr64 | 1756803 |
| unary | unknown | 3 |
| if | int1 | 1 |
| loop_for | int32 | 1771920 |
| call | unknown | 132 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 1771925 | 121 | 361 | 2 |
| add | 1728122 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1728000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1756801 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 1771680 | 120 | 120 | 0 |
| call | 2 | 4 | 120 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- print_array: unresolved loop bound
- kernel_cholesky: unresolved loop bound
- kernel_cholesky: unresolved loop bound
