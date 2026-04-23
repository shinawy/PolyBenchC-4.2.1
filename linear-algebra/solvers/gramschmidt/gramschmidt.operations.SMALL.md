# Static Operation Report: gramschmidt

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 26290 |
| add | 20886 |
| sub | 0 |
| mul | 9600 |
| mul_const | 16003 |
| div | 4800 |
| div_const | 4800 |
| mod | 16000 |
| cmp | 11201 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 11201 |
| loop_for | 32360 |
| call | 22496 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 25760 |
| assign | int32 | 527 |
| assign | ptr64 | 3 |
| add | float64 | 9600 |
| add | int32 | 11286 |
| mul | float64 | 4800 |
| mul | int32 | 4800 |
| mul_const | float64 | 4800 |
| mul_const | int32 | 11203 |
| div | float64 | 4800 |
| div_const | float64 | 4800 |
| mod | int32 | 16000 |
| cmp | int32 | 11201 |
| logical | int32 | 1 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 11201 |
| loop_for | int32 | 32360 |
| call | unknown | 22496 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 16142 | 142 | 10001 | 5 |
| add | 4800 | 11200 | 4880 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4800 | 0 | 4800 | 0 |
| mul_const | 4800 | 11200 | 0 | 3 |
| div | 0 | 0 | 4800 | 0 |
| div_const | 4800 | 0 | 0 | 0 |
| mod | 4800 | 11200 | 0 | 0 |
| cmp | 0 | 11200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 11200 | 0 | 1 |
| loop_for | 11340 | 11340 | 9680 | 0 |
| call | 0 | 22406 | 80 | 10 |

## Static Resolution Warnings

- kernel_gramschmidt: unresolved loop bound
