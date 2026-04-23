# Static Operation Report: syr2k

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2861 |
| add | 3006 |
| sub | 0 |
| mul | 2100 |
| mul_const | 903 |
| div | 0 |
| div_const | 2100 |
| mod | 3000 |
| cmp | 901 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 901 |
| loop_for | 3120 |
| call | 1814 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2100 |
| assign | int32 | 756 |
| assign | ptr64 | 5 |
| add | int32 | 3006 |
| mul | int32 | 2100 |
| mul_const | int32 | 903 |
| div_const | float64 | 2100 |
| mod | int32 | 3000 |
| cmp | int32 | 901 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 901 |
| loop_for | int32 | 3120 |
| call | unknown | 1814 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 2164 | 31 | 661 | 5 |
| add | 2100 | 900 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 2100 | 0 | 0 | 0 |
| mul_const | 0 | 900 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2100 | 0 | 0 | 0 |
| mod | 2100 | 900 | 0 | 0 |
| cmp | 0 | 900 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 900 | 0 | 1 |
| loop_for | 1560 | 930 | 630 | 0 |
| call | 0 | 1804 | 0 | 10 |

## Static Resolution Warnings

- kernel_syr2k: unresolved loop bound
- kernel_syr2k: unresolved loop bound
