# Static Operation Report: syrk

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2260 |
| add | 2404 |
| sub | 0 |
| mul | 1500 |
| mul_const | 902 |
| div | 0 |
| div_const | 1500 |
| mod | 2400 |
| cmp | 901 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 901 |
| loop_for | 3120 |
| call | 1812 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1500 |
| assign | int32 | 756 |
| assign | ptr64 | 4 |
| add | int32 | 2404 |
| mul | int32 | 1500 |
| mul_const | int32 | 902 |
| div_const | float64 | 1500 |
| mod | int32 | 2400 |
| cmp | int32 | 901 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 7 |
| unary | unknown | 3 |
| if | int1 | 901 |
| loop_for | int32 | 3120 |
| call | unknown | 1812 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 1564 | 31 | 661 | 4 |
| add | 1500 | 900 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1500 | 0 | 0 | 0 |
| mul_const | 0 | 900 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1500 | 0 | 0 | 0 |
| mod | 1500 | 900 | 0 | 0 |
| cmp | 0 | 900 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 900 | 0 | 1 |
| loop_for | 1560 | 930 | 630 | 0 |
| call | 0 | 1804 | 0 | 8 |

## Static Resolution Warnings

- kernel_syrk: unresolved loop bound
- kernel_syrk: unresolved loop bound
