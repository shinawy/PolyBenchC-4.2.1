# Static Operation Report: gramschmidt

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 27582210 |
| add | 22362606 |
| sub | 0 |
| mul | 10400000 |
| mul_const | 17160003 |
| div | 5200000 |
| div_const | 5200000 |
| mod | 17160000 |
| cmp | 11960001 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 11960001 |
| loop_for | 34331800 |
| call | 23922616 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 27565200 |
| assign | int32 | 17007 |
| assign | ptr64 | 3 |
| add | float64 | 10400000 |
| add | int32 | 11962606 |
| mul | float64 | 5200000 |
| mul | int32 | 5200000 |
| mul_const | float64 | 5200000 |
| mul_const | int32 | 11960003 |
| div | float64 | 5200000 |
| div_const | float64 | 5200000 |
| mod | int32 | 17160000 |
| cmp | int32 | 11960001 |
| logical | int32 | 1 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 11960001 |
| loop_for | int32 | 34331800 |
| call | unknown | 23922616 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 17164602 | 4602 | 10413001 | 5 |
| add | 5200000 | 11960000 | 5202600 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 5200000 | 0 | 5200000 | 0 |
| mul_const | 5200000 | 11960000 | 0 | 3 |
| div | 0 | 0 | 5200000 | 0 |
| div_const | 5200000 | 0 | 0 | 0 |
| mod | 5200000 | 11960000 | 0 | 0 |
| cmp | 0 | 11960000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 11960000 | 0 | 1 |
| loop_for | 11964600 | 11964600 | 10402600 | 0 |
| call | 0 | 23920006 | 2600 | 10 |

## Static Resolution Warnings

- kernel_gramschmidt: unresolved loop bound
