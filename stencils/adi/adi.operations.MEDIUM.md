# Static Operation Report: adi

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 23800622 |
| add | 54965610 |
| sub | 55084200 |
| mul | 7840800 |
| mul_const | 54925608 |
| div | 15681600 |
| div_const | 40007 |
| mod | 40000 |
| cmp | 40001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15681613 |
| if | 40001 |
| loop_for | 15801700 |
| call | 80016 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 23720813 |
| assign | int32 | 79805 |
| assign | ptr64 | 4 |
| add | float64 | 39204002 |
| add | int32 | 15761608 |
| sub | float64 | 15681600 |
| sub | int32 | 39402600 |
| mul | float64 | 7840800 |
| mul_const | float64 | 54885604 |
| mul_const | int32 | 40004 |
| div | float64 | 15681600 |
| div_const | float64 | 40007 |
| mod | int32 | 40000 |
| cmp | int32 | 40001 |
| logical | int32 | 1 |
| unary | float64 | 15681602 |
| unary | ptr64 | 6 |
| unary | unknown | 5 |
| if | int1 | 40001 |
| loop_for | int32 | 15801700 |
| call | unknown | 80016 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 40201 | 201 | 23760214 | 6 |
| add | 40000 | 40000 | 54885602 | 8 |
| sub | 40000 | 0 | 55044200 | 0 |
| mul | 0 | 0 | 7840800 | 0 |
| mul_const | 0 | 40000 | 54885604 | 4 |
| div | 0 | 0 | 15681600 | 0 |
| div_const | 40000 | 0 | 7 | 0 |
| mod | 0 | 40000 | 0 | 0 |
| cmp | 0 | 40000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 15681602 | 11 |
| if | 0 | 40000 | 0 | 1 |
| loop_for | 40200 | 40200 | 15721300 | 0 |
| call | 0 | 80004 | 0 | 12 |
