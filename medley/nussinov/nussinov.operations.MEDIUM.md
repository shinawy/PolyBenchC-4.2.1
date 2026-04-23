# Static Operation Report: nussinov

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 252008 |
| add | 1003 |
| sub | 1 |
| mul | 0 |
| mul_const | 1 |
| div | 0 |
| div_const | 0 |
| mod | 500 |
| cmp | 1 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 1 |
| loop_for | 252000 |
| call | 12 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | int32 | 252006 |
| assign | ptr64 | 2 |
| add | int32 | 1003 |
| sub | int32 | 1 |
| mul_const | int32 | 1 |
| mod | int32 | 500 |
| cmp | int32 | 1 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 1 |
| loop_for | int32 | 252000 |
| call | unknown | 12 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_nussinov | main |
|---|---:|---:|---:|---:|
| assign | 251002 | 502 | 501 | 3 |
| add | 500 | 0 | 500 | 3 |
| sub | 0 | 0 | 1 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 500 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 251000 | 500 | 500 | 0 |
| call | 0 | 4 | 0 | 8 |

## Static Resolution Warnings

- print_array: unresolved loop bound
- kernel_nussinov: unresolved loop bound
