# Static Operation Report: lu

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 64483609 |
| add | 64160404 |
| sub | 0 |
| mul | 64000000 |
| mul_const | 160002 |
| div | 0 |
| div_const | 0 |
| mod | 160000 |
| cmp | 160001 |
| logical | 1 |
| bitwise | 0 |
| unary | 64320006 |
| if | 160001 |
| loop_for | 64642400 |
| call | 320012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 160400 |
| assign | int32 | 163207 |
| assign | ptr64 | 64160002 |
| add | int32 | 160404 |
| add | ptr64 | 64000000 |
| mul | float64 | 64000000 |
| mul_const | int32 | 160002 |
| mod | int32 | 160000 |
| cmp | int32 | 160001 |
| logical | int32 | 1 |
| unary | ptr64 | 64320003 |
| unary | unknown | 3 |
| if | int1 | 160001 |
| loop_for | int32 | 64642400 |
| call | unknown | 320012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 64482405 | 401 | 801 | 2 |
| add | 64000402 | 160000 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000000 | 0 | 0 | 0 |
| mul_const | 1 | 160000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 160000 | 0 | 0 |
| cmp | 0 | 160000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64320001 | 0 | 0 | 5 |
| if | 0 | 160000 | 0 | 1 |
| loop_for | 64481600 | 160400 | 400 | 0 |
| call | 2 | 320004 | 0 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_lu: unresolved loop bound
- kernel_lu: unresolved loop bound
