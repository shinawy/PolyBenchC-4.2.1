# Static Operation Report: syrk

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 154810 |
| add | 163204 |
| sub | 0 |
| mul | 105600 |
| mul_const | 57602 |
| div | 0 |
| div_const | 105600 |
| mod | 163200 |
| cmp | 57601 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 57601 |
| loop_for | 212160 |
| call | 115212 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 105600 |
| assign | int32 | 49206 |
| assign | ptr64 | 4 |
| add | int32 | 163204 |
| mul | int32 | 105600 |
| mul_const | int32 | 57602 |
| div_const | float64 | 105600 |
| mod | int32 | 163200 |
| cmp | int32 | 57601 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 7 |
| unary | unknown | 3 |
| if | int1 | 57601 |
| loop_for | int32 | 212160 |
| call | unknown | 115212 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 106084 | 241 | 48481 | 4 |
| add | 105600 | 57600 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 105600 | 0 | 0 | 0 |
| mul_const | 0 | 57600 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 105600 | 0 | 0 | 0 |
| mod | 105600 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 57600 | 0 | 1 |
| loop_for | 106080 | 57840 | 48240 | 0 |
| call | 0 | 115204 | 0 | 8 |

## Static Resolution Warnings

- kernel_syrk: unresolved loop bound
- kernel_syrk: unresolved loop bound
