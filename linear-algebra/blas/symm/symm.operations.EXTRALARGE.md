# Static Operation Report: symm

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 26010011 |
| add | 26002006 |
| sub | 5200000 |
| mul | 15600000 |
| mul_const | 10400003 |
| div | 0 |
| div_const | 10400000 |
| mod | 15600000 |
| cmp | 5200001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 5200001 |
| loop_for | 15608000 |
| call | 10400014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 20800000 |
| assign | int32 | 5210006 |
| assign | ptr64 | 5 |
| add | float64 | 10400000 |
| add | int32 | 15602006 |
| sub | int32 | 5200000 |
| mul | float64 | 15600000 |
| mul_const | float64 | 5200000 |
| mul_const | int32 | 5200003 |
| div_const | float64 | 10400000 |
| mod | int32 | 15600000 |
| cmp | int32 | 5200001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 5200001 |
| loop_for | int32 | 15608000 |
| call | unknown | 10400014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 10406004 | 2001 | 15602001 | 5 |
| add | 10402000 | 5200000 | 10400000 | 6 |
| sub | 5200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 15600000 | 0 |
| mul_const | 0 | 5200000 | 5200000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 10400000 | 0 | 0 | 0 |
| mod | 10400000 | 5200000 | 0 | 0 |
| cmp | 0 | 5200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 5200000 | 0 | 1 |
| loop_for | 5204000 | 5202000 | 5202000 | 0 |
| call | 0 | 10400004 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_symm: unresolved loop bound
