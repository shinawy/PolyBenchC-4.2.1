# Static Operation Report: syrk

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 17173010 |
| add | 18720004 |
| sub | 0 |
| mul | 11960000 |
| mul_const | 6760002 |
| div | 0 |
| div_const | 11960000 |
| mod | 18720000 |
| cmp | 6760001 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 6760001 |
| loop_for | 23930400 |
| call | 13520012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11960000 |
| assign | int32 | 5213006 |
| assign | ptr64 | 4 |
| add | int32 | 18720004 |
| mul | int32 | 11960000 |
| mul_const | int32 | 6760002 |
| div_const | float64 | 11960000 |
| mod | int32 | 18720000 |
| cmp | int32 | 6760001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 7 |
| unary | unknown | 3 |
| if | int1 | 6760001 |
| loop_for | int32 | 23930400 |
| call | unknown | 13520012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 11965204 | 2601 | 5205201 | 4 |
| add | 11960000 | 6760000 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 11960000 | 0 | 0 | 0 |
| mul_const | 0 | 6760000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 11960000 | 0 | 0 | 0 |
| mod | 11960000 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 6760000 | 0 | 1 |
| loop_for | 11965200 | 6762600 | 5202600 | 0 |
| call | 0 | 13520004 | 0 | 8 |

## Static Resolution Warnings

- kernel_syrk: unresolved loop bound
- kernel_syrk: unresolved loop bound
