# Static Operation Report: symm

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 6005011 |
| add | 6001006 |
| sub | 1200000 |
| mul | 3600000 |
| mul_const | 2400003 |
| div | 0 |
| div_const | 2400000 |
| mod | 3600000 |
| cmp | 1200001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 1200001 |
| loop_for | 3604000 |
| call | 2400014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 4800000 |
| assign | int32 | 1205006 |
| assign | ptr64 | 5 |
| add | float64 | 2400000 |
| add | int32 | 3601006 |
| sub | int32 | 1200000 |
| mul | float64 | 3600000 |
| mul_const | float64 | 1200000 |
| mul_const | int32 | 1200003 |
| div_const | float64 | 2400000 |
| mod | int32 | 3600000 |
| cmp | int32 | 1200001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 1200001 |
| loop_for | int32 | 3604000 |
| call | unknown | 2400014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 2403004 | 1001 | 3601001 | 5 |
| add | 2401000 | 1200000 | 2400000 | 6 |
| sub | 1200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 3600000 | 0 |
| mul_const | 0 | 1200000 | 1200000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2400000 | 0 | 0 | 0 |
| mod | 2400000 | 1200000 | 0 | 0 |
| cmp | 0 | 1200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 1200000 | 0 | 1 |
| loop_for | 1202000 | 1201000 | 1201000 | 0 |
| call | 0 | 2400004 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_symm: unresolved loop bound
