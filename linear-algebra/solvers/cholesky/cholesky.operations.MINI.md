# Static Operation Report: cholesky

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 69209 |
| add | 64044 |
| sub | 0 |
| mul | 64000 |
| mul_const | 2 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 1 |
| logical | 1 |
| bitwise | 0 |
| unary | 67206 |
| if | 1 |
| loop_for | 69040 |
| call | 52 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1680 |
| assign | int32 | 1927 |
| assign | ptr64 | 65602 |
| add | int32 | 44 |
| add | ptr64 | 64000 |
| mul | float64 | 64000 |
| mul_const | int32 | 2 |
| cmp | int32 | 1 |
| logical | int32 | 1 |
| unary | ptr64 | 67203 |
| unary | unknown | 3 |
| if | int1 | 1 |
| loop_for | int32 | 69040 |
| call | unknown | 52 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 69045 | 41 | 121 | 2 |
| add | 64042 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 67201 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 68960 | 40 | 40 | 0 |
| call | 2 | 4 | 40 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- print_array: unresolved loop bound
- kernel_cholesky: unresolved loop bound
- kernel_cholesky: unresolved loop bound
