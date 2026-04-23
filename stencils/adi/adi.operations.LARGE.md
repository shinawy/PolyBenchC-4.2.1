# Static Operation Report: adi

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2995003022 |
| add | 6974028010 |
| sub | 6977021000 |
| mul | 996004000 |
| mul_const | 6973028008 |
| div | 1992008000 |
| div_const | 1000007 |
| mod | 1000000 |
| cmp | 1000001 |
| logical | 1 |
| bitwise | 0 |
| unary | 1992008013 |
| if | 1000001 |
| loop_for | 1995008500 |
| call | 2000016 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2993004013 |
| assign | int32 | 1999005 |
| assign | ptr64 | 4 |
| add | float64 | 4980020002 |
| add | int32 | 1994008008 |
| sub | float64 | 1992008000 |
| sub | int32 | 4985013000 |
| mul | float64 | 996004000 |
| mul_const | float64 | 6972028004 |
| mul_const | int32 | 1000004 |
| div | float64 | 1992008000 |
| div_const | float64 | 1000007 |
| mod | int32 | 1000000 |
| cmp | int32 | 1000001 |
| logical | int32 | 1 |
| unary | float64 | 1992008002 |
| unary | ptr64 | 6 |
| unary | unknown | 5 |
| if | int1 | 1000001 |
| loop_for | int32 | 1995008500 |
| call | unknown | 2000016 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 1001001 | 1001 | 2994001014 | 6 |
| add | 1000000 | 1000000 | 6972028002 | 8 |
| sub | 1000000 | 0 | 6976021000 | 0 |
| mul | 0 | 0 | 996004000 | 0 |
| mul_const | 0 | 1000000 | 6972028004 | 4 |
| div | 0 | 0 | 1992008000 | 0 |
| div_const | 1000000 | 0 | 7 | 0 |
| mod | 0 | 1000000 | 0 | 0 |
| cmp | 0 | 1000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 1992008002 | 11 |
| if | 0 | 1000000 | 0 | 1 |
| loop_for | 1001000 | 1001000 | 1993006500 | 0 |
| call | 0 | 2000004 | 0 | 12 |
