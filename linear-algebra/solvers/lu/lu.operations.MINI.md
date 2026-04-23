# Static Operation Report: lu

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 69169 |
| add | 65644 |
| sub | 0 |
| mul | 64000 |
| mul_const | 1602 |
| div | 0 |
| div_const | 0 |
| mod | 1600 |
| cmp | 1601 |
| logical | 1 |
| bitwise | 0 |
| unary | 67206 |
| if | 1601 |
| loop_for | 70640 |
| call | 3212 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1640 |
| assign | int32 | 1927 |
| assign | ptr64 | 65602 |
| add | int32 | 1644 |
| add | ptr64 | 64000 |
| mul | float64 | 64000 |
| mul_const | int32 | 1602 |
| mod | int32 | 1600 |
| cmp | int32 | 1601 |
| logical | int32 | 1 |
| unary | ptr64 | 67203 |
| unary | unknown | 3 |
| if | int1 | 1601 |
| loop_for | int32 | 70640 |
| call | unknown | 3212 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 69045 | 41 | 81 | 2 |
| add | 64042 | 1600 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000 | 0 | 0 | 0 |
| mul_const | 1 | 1600 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 1600 | 0 | 0 |
| cmp | 0 | 1600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 67201 | 0 | 0 | 5 |
| if | 0 | 1600 | 0 | 1 |
| loop_for | 68960 | 1640 | 40 | 0 |
| call | 2 | 3204 | 0 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_lu: unresolved loop bound
- kernel_lu: unresolved loop bound
