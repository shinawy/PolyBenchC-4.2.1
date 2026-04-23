# Static Operation Report: fdtd-2d

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 15615012013 |
| add | 15617403007 |
| sub | 51971803000 |
| mul | 15600000 |
| mul_const | 15606401003 |
| div | 0 |
| div_const | 15600000 |
| mod | 15600000 |
| cmp | 15600001 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 15600001 |
| loop_for | 15620209000 |
| call | 31200020 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 15609002000 |
| assign | int32 | 6010009 |
| assign | ptr64 | 4 |
| add | float64 | 5195401000 |
| add | int32 | 10422002007 |
| sub | float64 | 36377003000 |
| sub | int32 | 15594800000 |
| mul | float64 | 15600000 |
| mul_const | float64 | 15590801000 |
| mul_const | int32 | 15600003 |
| div_const | float64 | 15600000 |
| mod | int32 | 15600000 |
| cmp | int32 | 15600001 |
| logical | int32 | 1 |
| unary | ptr64 | 11 |
| unary | unknown | 5 |
| if | int1 | 15600001 |
| loop_for | int32 | 15620209000 |
| call | unknown | 31200020 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 15603002 | 6003 | 15599403001 | 7 |
| add | 15600000 | 15600000 | 15586203000 | 7 |
| sub | 0 | 0 | 51971803000 | 0 |
| mul | 15600000 | 0 | 0 | 0 |
| mul_const | 0 | 15600000 | 15590801000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15600000 | 0 | 0 | 0 |
| mod | 0 | 15600000 | 0 | 0 |
| cmp | 0 | 15600000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 15600000 | 0 | 1 |
| loop_for | 5203000 | 15606000 | 15599400000 | 0 |
| call | 0 | 31200008 | 0 | 12 |
