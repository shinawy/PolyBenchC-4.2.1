# Static Operation Report: symm

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 24311 |
| add | 24066 |
| sub | 4800 |
| mul | 14400 |
| mul_const | 9603 |
| div | 0 |
| div_const | 9600 |
| mod | 14400 |
| cmp | 4801 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 4801 |
| loop_for | 14640 |
| call | 9614 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 19200 |
| assign | int32 | 5106 |
| assign | ptr64 | 5 |
| add | float64 | 9600 |
| add | int32 | 14466 |
| sub | int32 | 4800 |
| mul | float64 | 14400 |
| mul_const | float64 | 4800 |
| mul_const | int32 | 4803 |
| div_const | float64 | 9600 |
| mod | int32 | 14400 |
| cmp | int32 | 4801 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 4801 |
| loop_for | int32 | 14640 |
| call | unknown | 9614 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 9784 | 61 | 14461 | 5 |
| add | 9660 | 4800 | 9600 | 6 |
| sub | 4800 | 0 | 0 | 0 |
| mul | 0 | 0 | 14400 | 0 |
| mul_const | 0 | 4800 | 4800 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 9600 | 0 | 0 | 0 |
| mod | 9600 | 4800 | 0 | 0 |
| cmp | 0 | 4800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 4800 | 0 | 1 |
| loop_for | 4920 | 4860 | 4860 | 0 |
| call | 0 | 9604 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_symm: unresolved loop bound
