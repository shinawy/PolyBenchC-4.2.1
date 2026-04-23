# Static Operation Report: syrk

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 3846010 |
| add | 4080004 |
| sub | 0 |
| mul | 2640000 |
| mul_const | 1440002 |
| div | 0 |
| div_const | 2640000 |
| mod | 4080000 |
| cmp | 1440001 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 1440001 |
| loop_for | 5284800 |
| call | 2880012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2640000 |
| assign | int32 | 1206006 |
| assign | ptr64 | 4 |
| add | int32 | 4080004 |
| mul | int32 | 2640000 |
| mul_const | int32 | 1440002 |
| div_const | float64 | 2640000 |
| mod | int32 | 4080000 |
| cmp | int32 | 1440001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 7 |
| unary | unknown | 3 |
| if | int1 | 1440001 |
| loop_for | int32 | 5284800 |
| call | unknown | 2880012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 2642404 | 1201 | 1202401 | 4 |
| add | 2640000 | 1440000 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 2640000 | 0 | 0 | 0 |
| mul_const | 0 | 1440000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2640000 | 0 | 0 | 0 |
| mod | 2640000 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 1440000 | 0 | 1 |
| loop_for | 2642400 | 1441200 | 1201200 | 0 |
| call | 0 | 2880004 | 0 | 8 |

## Static Resolution Warnings

- kernel_syrk: unresolved loop bound
- kernel_syrk: unresolved loop bound
