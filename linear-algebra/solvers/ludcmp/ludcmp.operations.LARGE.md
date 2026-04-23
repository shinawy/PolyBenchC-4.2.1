# Static Operation Report: ludcmp

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 8012034016 |
| add | 8000008007 |
| sub | 1 |
| mul | 8000000000 |
| mul_const | 2 |
| div | 2000 |
| div_const | 4000 |
| mod | 2000 |
| cmp | 2001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8008000015 |
| if | 2001 |
| loop_for | 8012018000 |
| call | 4018 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4016001 |
| assign | int32 | 4018010 |
| assign | ptr64 | 8004000005 |
| add | float64 | 2000 |
| add | int32 | 6007 |
| add | ptr64 | 8000000000 |
| sub | int32 | 1 |
| mul | float64 | 8000000000 |
| mul_const | int32 | 2 |
| div | float64 | 2000 |
| div_const | float64 | 4000 |
| mod | int32 | 2000 |
| cmp | int32 | 2001 |
| logical | int32 | 1 |
| unary | ptr64 | 8008000009 |
| unary | unknown | 6 |
| if | int1 | 2001 |
| loop_for | int32 | 8012018000 |
| call | unknown | 4018 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 8012018007 | 1 | 16003 | 5 |
| add | 8000006002 | 0 | 2000 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 8000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 2000 | 0 |
| div_const | 4000 | 0 | 0 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 8008000001 | 0 | 0 | 14 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 8012010000 | 2000 | 6000 | 0 |
| call | 2 | 4004 | 0 | 12 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
