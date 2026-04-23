# Static Operation Report: cholesky

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 8012020009 |
| add | 8000002004 |
| sub | 0 |
| mul | 8000000000 |
| mul_const | 2 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 1 |
| logical | 1 |
| bitwise | 0 |
| unary | 8008000006 |
| if | 1 |
| loop_for | 8012012000 |
| call | 2012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4004000 |
| assign | int32 | 4016007 |
| assign | ptr64 | 8004000002 |
| add | int32 | 2004 |
| add | ptr64 | 8000000000 |
| mul | float64 | 8000000000 |
| mul_const | int32 | 2 |
| cmp | int32 | 1 |
| logical | int32 | 1 |
| unary | ptr64 | 8008000003 |
| unary | unknown | 3 |
| if | int1 | 1 |
| loop_for | int32 | 8012012000 |
| call | unknown | 2012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 8012012005 | 2001 | 6001 | 2 |
| add | 8000002002 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 8000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 8008000001 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 8012008000 | 2000 | 2000 | 0 |
| call | 2 | 4 | 2000 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- print_array: unresolved loop bound
- kernel_cholesky: unresolved loop bound
- kernel_cholesky: unresolved loop bound
