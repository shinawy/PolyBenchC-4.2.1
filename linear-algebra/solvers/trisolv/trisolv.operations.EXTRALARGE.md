# Static Operation Report: trisolv

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 24007 |
| add | 4 |
| sub | 0 |
| mul | 0 |
| mul_const | 1 |
| div | 4000 |
| div_const | 0 |
| mod | 4000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 4011 |
| if | 4001 |
| loop_for | 12000 |
| call | 8014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 16000 |
| assign | int32 | 8004 |
| assign | ptr64 | 3 |
| add | int32 | 4 |
| mul_const | int32 | 1 |
| div | float64 | 4000 |
| mod | int32 | 4000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | int32 | 4000 |
| unary | ptr64 | 7 |
| unary | unknown | 4 |
| if | int1 | 4001 |
| loop_for | int32 | 12000 |
| call | unknown | 8014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 12001 | 1 | 12001 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 4000 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 4000 | 0 | 0 | 11 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4000 | 4000 | 4000 | 0 |
| call | 0 | 8004 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trisolv: unresolved loop bound
