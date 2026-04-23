# Static Operation Report: correlation

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 39034613 |
| add | 30162605 |
| sub | 23402602 |
| mul | 23400000 |
| mul_const | 6760002 |
| div | 7805200 |
| div_const | 7800000 |
| mod | 6760000 |
| cmp | 6762601 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 6762601 |
| loop_for | 37976399 |
| call | 21322616 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 39018201 |
| assign | int32 | 16407 |
| assign | ptr64 | 5 |
| add | float64 | 23400000 |
| add | int32 | 6762605 |
| sub | float64 | 23400000 |
| sub | int32 | 2602 |
| mul | float64 | 15600000 |
| mul | int32 | 7800000 |
| mul_const | int32 | 6760002 |
| div | float64 | 7805200 |
| div_const | float64 | 7800000 |
| mod | int32 | 6760000 |
| cmp | float64 | 2600 |
| cmp | int32 | 6760001 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 6762601 |
| loop_for | int32 | 37976399 |
| call | unknown | 21322616 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 7803002 | 2601 | 31229004 | 6 |
| add | 7800000 | 6760000 | 15602599 | 6 |
| sub | 0 | 0 | 23402602 | 0 |
| mul | 7800000 | 0 | 15600000 | 0 |
| mul_const | 0 | 6760000 | 0 | 2 |
| div | 0 | 0 | 7805200 | 0 |
| div_const | 7800000 | 0 | 0 | 0 |
| mod | 0 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 2600 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 6760000 | 2600 | 1 |
| loop_for | 7803000 | 6762600 | 23410799 | 0 |
| call | 0 | 13520004 | 7802600 | 12 |

## Static Resolution Warnings

- kernel_correlation: unresolved loop bound
