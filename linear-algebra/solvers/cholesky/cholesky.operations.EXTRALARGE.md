# Static Operation Report: cholesky

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 64048040009 |
| add | 64000004004 |
| sub | 0 |
| mul | 64000000000 |
| mul_const | 2 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 1 |
| logical | 1 |
| bitwise | 0 |
| unary | 64032000006 |
| if | 1 |
| loop_for | 64048024000 |
| call | 4012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 16008000 |
| assign | int32 | 16032007 |
| assign | ptr64 | 64016000002 |
| add | int32 | 4004 |
| add | ptr64 | 64000000000 |
| mul | float64 | 64000000000 |
| mul_const | int32 | 2 |
| cmp | int32 | 1 |
| logical | int32 | 1 |
| unary | ptr64 | 64032000003 |
| unary | unknown | 3 |
| if | int1 | 1 |
| loop_for | int32 | 64048024000 |
| call | unknown | 4012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 64048024005 | 4001 | 12001 | 2 |
| add | 64000004002 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64032000001 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 64048016000 | 4000 | 4000 | 0 |
| call | 2 | 4 | 4000 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- print_array: unresolved loop bound
- kernel_cholesky: unresolved loop bound
- kernel_cholesky: unresolved loop bound
