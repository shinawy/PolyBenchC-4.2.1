# Static Operation Report: nussinov

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 6260008 |
| add | 5003 |
| sub | 1 |
| mul | 0 |
| mul_const | 1 |
| div | 0 |
| div_const | 0 |
| mod | 2500 |
| cmp | 1 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 1 |
| loop_for | 6260000 |
| call | 12 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | int32 | 6260006 |
| assign | ptr64 | 2 |
| add | int32 | 5003 |
| sub | int32 | 1 |
| mul_const | int32 | 1 |
| mod | int32 | 2500 |
| cmp | int32 | 1 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 1 |
| loop_for | int32 | 6260000 |
| call | unknown | 12 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_nussinov | main |
|---|---:|---:|---:|---:|
| assign | 6255002 | 2502 | 2501 | 3 |
| add | 2500 | 0 | 2500 | 3 |
| sub | 0 | 0 | 1 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 2500 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 6255000 | 2500 | 2500 | 0 |
| call | 0 | 4 | 0 | 8 |

## Static Resolution Warnings

- print_array: unresolved loop bound
- kernel_nussinov: unresolved loop bound
