# Static Operation Report: trmm

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 15610008 |
| add | 15600004 |
| sub | 5200000 |
| mul | 5200000 |
| mul_const | 5200002 |
| div | 0 |
| div_const | 5200000 |
| mod | 10400000 |
| cmp | 5200001 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 5200001 |
| loop_for | 15606000 |
| call | 10400012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 10402000 |
| assign | int32 | 5208005 |
| assign | ptr64 | 3 |
| add | int32 | 15600004 |
| sub | int32 | 5200000 |
| mul | float64 | 5200000 |
| mul_const | int32 | 5200002 |
| div_const | float64 | 5200000 |
| mod | int32 | 10400000 |
| cmp | int32 | 5200001 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 3 |
| if | int1 | 5200001 |
| loop_for | int32 | 15606000 |
| call | unknown | 10400012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 5206002 | 2001 | 10402001 | 4 |
| add | 5200000 | 5200000 | 5200000 | 4 |
| sub | 5200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 5200000 | 0 |
| mul_const | 0 | 5200000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 5200000 | 0 | 0 | 0 |
| mod | 5200000 | 5200000 | 0 | 0 |
| cmp | 0 | 5200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 5200000 | 0 | 1 |
| loop_for | 5202000 | 5202000 | 5202000 | 0 |
| call | 0 | 10400004 | 0 | 8 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trmm: unresolved loop bound
