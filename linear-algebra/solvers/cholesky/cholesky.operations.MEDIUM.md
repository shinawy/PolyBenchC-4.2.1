# Static Operation Report: cholesky

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 64484009 |
| add | 64000404 |
| sub | 0 |
| mul | 64000000 |
| mul_const | 2 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 1 |
| logical | 1 |
| bitwise | 0 |
| unary | 64320006 |
| if | 1 |
| loop_for | 64482400 |
| call | 412 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 160800 |
| assign | int32 | 163207 |
| assign | ptr64 | 64160002 |
| add | int32 | 404 |
| add | ptr64 | 64000000 |
| mul | float64 | 64000000 |
| mul_const | int32 | 2 |
| cmp | int32 | 1 |
| logical | int32 | 1 |
| unary | ptr64 | 64320003 |
| unary | unknown | 3 |
| if | int1 | 1 |
| loop_for | int32 | 64482400 |
| call | unknown | 412 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 64482405 | 401 | 1201 | 2 |
| add | 64000402 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64320001 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 64481600 | 400 | 400 | 0 |
| call | 2 | 4 | 400 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- print_array: unresolved loop bound
- kernel_cholesky: unresolved loop bound
- kernel_cholesky: unresolved loop bound
