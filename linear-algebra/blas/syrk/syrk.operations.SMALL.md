# Static Operation Report: syrk

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 16410 |
| add | 17604 |
| sub | 0 |
| mul | 11200 |
| mul_const | 6402 |
| div | 0 |
| div_const | 11200 |
| mod | 17600 |
| cmp | 6401 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 6401 |
| loop_for | 22720 |
| call | 12812 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11200 |
| assign | int32 | 5206 |
| assign | ptr64 | 4 |
| add | int32 | 17604 |
| mul | int32 | 11200 |
| mul_const | int32 | 6402 |
| div_const | float64 | 11200 |
| mod | int32 | 17600 |
| cmp | int32 | 6401 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 7 |
| unary | unknown | 3 |
| if | int1 | 6401 |
| loop_for | int32 | 22720 |
| call | unknown | 12812 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 11364 | 81 | 4961 | 4 |
| add | 11200 | 6400 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 11200 | 0 | 0 | 0 |
| mul_const | 0 | 6400 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 11200 | 0 | 0 | 0 |
| mod | 11200 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 6400 | 0 | 1 |
| loop_for | 11360 | 6480 | 4880 | 0 |
| call | 0 | 12804 | 0 | 8 |

## Static Resolution Warnings

- kernel_syrk: unresolved loop bound
- kernel_syrk: unresolved loop bound
