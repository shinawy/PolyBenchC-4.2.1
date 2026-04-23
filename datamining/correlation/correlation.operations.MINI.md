# Static Operation Report: correlation

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 4865 |
| add | 3505 |
| sub | 2718 |
| mul | 2688 |
| mul_const | 786 |
| div | 952 |
| div_const | 896 |
| mod | 784 |
| cmp | 813 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 813 |
| loop_for | 4543 |
| call | 2508 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4677 |
| assign | int32 | 183 |
| assign | ptr64 | 5 |
| add | float64 | 2688 |
| add | int32 | 817 |
| sub | float64 | 2688 |
| sub | int32 | 30 |
| mul | float64 | 1792 |
| mul | int32 | 896 |
| mul_const | int32 | 786 |
| div | float64 | 952 |
| div_const | float64 | 896 |
| mod | int32 | 784 |
| cmp | float64 | 28 |
| cmp | int32 | 785 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 813 |
| loop_for | int32 | 4543 |
| call | unknown | 2508 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 930 | 29 | 3900 | 6 |
| add | 896 | 784 | 1819 | 6 |
| sub | 0 | 0 | 2718 | 0 |
| mul | 896 | 0 | 1792 | 0 |
| mul_const | 0 | 784 | 0 | 2 |
| div | 0 | 0 | 952 | 0 |
| div_const | 896 | 0 | 0 | 0 |
| mod | 0 | 784 | 0 | 0 |
| cmp | 0 | 784 | 28 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 784 | 28 | 1 |
| loop_for | 928 | 812 | 2803 | 0 |
| call | 0 | 1572 | 924 | 12 |

## Static Resolution Warnings

- kernel_correlation: unresolved loop bound
