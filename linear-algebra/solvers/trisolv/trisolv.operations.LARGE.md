# Static Operation Report: trisolv

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 12007 |
| add | 4 |
| sub | 0 |
| mul | 0 |
| mul_const | 1 |
| div | 2000 |
| div_const | 0 |
| mod | 2000 |
| cmp | 2001 |
| logical | 1 |
| bitwise | 0 |
| unary | 2011 |
| if | 2001 |
| loop_for | 6000 |
| call | 4014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 8000 |
| assign | int32 | 4004 |
| assign | ptr64 | 3 |
| add | int32 | 4 |
| mul_const | int32 | 1 |
| div | float64 | 2000 |
| mod | int32 | 2000 |
| cmp | int32 | 2001 |
| logical | int32 | 1 |
| unary | int32 | 2000 |
| unary | ptr64 | 7 |
| unary | unknown | 4 |
| if | int1 | 2001 |
| loop_for | int32 | 6000 |
| call | unknown | 4014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 6001 | 1 | 6001 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 2000 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2000 | 0 | 0 | 11 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 2000 | 2000 | 2000 | 0 |
| call | 0 | 4004 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trisolv: unresolved loop bound
