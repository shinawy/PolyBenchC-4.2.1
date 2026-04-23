# Static Operation Report: correlation

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 8416013 |
| add | 6481205 |
| sub | 5041202 |
| mul | 5040000 |
| mul_const | 1440002 |
| div | 1682400 |
| div_const | 1680000 |
| mod | 1440000 |
| cmp | 1441201 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 1441201 |
| loop_for | 8167599 |
| call | 4561216 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 8408401 |
| assign | int32 | 7607 |
| assign | ptr64 | 5 |
| add | float64 | 5040000 |
| add | int32 | 1441205 |
| sub | float64 | 5040000 |
| sub | int32 | 1202 |
| mul | float64 | 3360000 |
| mul | int32 | 1680000 |
| mul_const | int32 | 1440002 |
| div | float64 | 1682400 |
| div_const | float64 | 1680000 |
| mod | int32 | 1440000 |
| cmp | float64 | 1200 |
| cmp | int32 | 1440001 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 1441201 |
| loop_for | int32 | 8167599 |
| call | unknown | 4561216 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 1681402 | 1201 | 6733404 | 6 |
| add | 1680000 | 1440000 | 3361199 | 6 |
| sub | 0 | 0 | 5041202 | 0 |
| mul | 1680000 | 0 | 3360000 | 0 |
| mul_const | 0 | 1440000 | 0 | 2 |
| div | 0 | 0 | 1682400 | 0 |
| div_const | 1680000 | 0 | 0 | 0 |
| mod | 0 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 1200 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 1440000 | 1200 | 1 |
| loop_for | 1681400 | 1441200 | 5044999 | 0 |
| call | 0 | 2880004 | 1681200 | 12 |

## Static Resolution Warnings

- kernel_correlation: unresolved loop bound
