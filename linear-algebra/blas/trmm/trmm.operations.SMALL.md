# Static Operation Report: trmm

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 14708 |
| add | 14404 |
| sub | 4800 |
| mul | 4800 |
| mul_const | 4802 |
| div | 0 |
| div_const | 4800 |
| mod | 9600 |
| cmp | 4801 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 4801 |
| loop_for | 14580 |
| call | 9612 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 9660 |
| assign | int32 | 5045 |
| assign | ptr64 | 3 |
| add | int32 | 14404 |
| sub | int32 | 4800 |
| mul | float64 | 4800 |
| mul_const | int32 | 4802 |
| div_const | float64 | 4800 |
| mod | int32 | 9600 |
| cmp | int32 | 4801 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 3 |
| if | int1 | 4801 |
| loop_for | int32 | 14580 |
| call | unknown | 9612 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 4982 | 61 | 9661 | 4 |
| add | 4800 | 4800 | 4800 | 4 |
| sub | 4800 | 0 | 0 | 0 |
| mul | 0 | 0 | 4800 | 0 |
| mul_const | 0 | 4800 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4800 | 0 | 0 | 0 |
| mod | 4800 | 4800 | 0 | 0 |
| cmp | 0 | 4800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 4800 | 0 | 1 |
| loop_for | 4860 | 4860 | 4860 | 0 |
| call | 0 | 9604 | 0 | 8 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trmm: unresolved loop bound
