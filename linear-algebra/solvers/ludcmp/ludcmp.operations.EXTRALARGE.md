# Static Operation Report: ludcmp

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 64048068016 |
| add | 64000016007 |
| sub | 1 |
| mul | 64000000000 |
| mul_const | 2 |
| div | 4000 |
| div_const | 8000 |
| mod | 4000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 64032000015 |
| if | 4001 |
| loop_for | 64048036000 |
| call | 8018 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 16032001 |
| assign | int32 | 16036010 |
| assign | ptr64 | 64016000005 |
| add | float64 | 4000 |
| add | int32 | 12007 |
| add | ptr64 | 64000000000 |
| sub | int32 | 1 |
| mul | float64 | 64000000000 |
| mul_const | int32 | 2 |
| div | float64 | 4000 |
| div_const | float64 | 8000 |
| mod | int32 | 4000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | ptr64 | 64032000009 |
| unary | unknown | 6 |
| if | int1 | 4001 |
| loop_for | int32 | 64048036000 |
| call | unknown | 8018 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 64048036007 | 1 | 32003 | 5 |
| add | 64000012002 | 0 | 4000 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 64000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 4000 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64032000001 | 0 | 0 | 14 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 64048020000 | 4000 | 12000 | 0 |
| call | 2 | 8004 | 0 | 12 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
- kernel_ludcmp: unresolved loop bound
