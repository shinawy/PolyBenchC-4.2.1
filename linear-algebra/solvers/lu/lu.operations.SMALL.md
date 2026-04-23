# Static Operation Report: lu

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1772289 |
| add | 1742524 |
| sub | 0 |
| mul | 1728000 |
| mul_const | 14402 |
| div | 0 |
| div_const | 0 |
| mod | 14400 |
| cmp | 14401 |
| logical | 1 |
| bitwise | 0 |
| unary | 1756806 |
| if | 14401 |
| loop_for | 1786320 |
| call | 28812 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 14520 |
| assign | int32 | 15367 |
| assign | ptr64 | 1742402 |
| add | int32 | 14524 |
| add | ptr64 | 1728000 |
| mul | float64 | 1728000 |
| mul_const | int32 | 14402 |
| mod | int32 | 14400 |
| cmp | int32 | 14401 |
| logical | int32 | 1 |
| unary | ptr64 | 1756803 |
| unary | unknown | 3 |
| if | int1 | 14401 |
| loop_for | int32 | 1786320 |
| call | unknown | 28812 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 1771925 | 121 | 241 | 2 |
| add | 1728122 | 14400 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1728000 | 0 | 0 | 0 |
| mul_const | 1 | 14400 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 14400 | 0 | 0 |
| cmp | 0 | 14400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1756801 | 0 | 0 | 5 |
| if | 0 | 14400 | 0 | 1 |
| loop_for | 1771680 | 14520 | 120 | 0 |
| call | 2 | 28804 | 0 | 6 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_lu: unresolved loop bound
- kernel_lu: unresolved loop bound
