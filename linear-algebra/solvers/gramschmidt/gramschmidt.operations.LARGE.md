# Static Operation Report: gramschmidt

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 6250410 |
| add | 5041206 |
| sub | 0 |
| mul | 2400000 |
| mul_const | 3840003 |
| div | 1200000 |
| div_const | 1200000 |
| mod | 3840000 |
| cmp | 2640001 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 2640001 |
| loop_for | 7685600 |
| call | 5281216 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 6242400 |
| assign | int32 | 8007 |
| assign | ptr64 | 3 |
| add | float64 | 2400000 |
| add | int32 | 2641206 |
| mul | float64 | 1200000 |
| mul | int32 | 1200000 |
| mul_const | float64 | 1200000 |
| mul_const | int32 | 2640003 |
| div | float64 | 1200000 |
| div_const | float64 | 1200000 |
| mod | int32 | 3840000 |
| cmp | int32 | 2640001 |
| logical | int32 | 1 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 2640001 |
| loop_for | int32 | 7685600 |
| call | unknown | 5281216 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 3842202 | 2202 | 2406001 | 5 |
| add | 1200000 | 2640000 | 1201200 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1200000 | 0 | 1200000 | 0 |
| mul_const | 1200000 | 2640000 | 0 | 3 |
| div | 0 | 0 | 1200000 | 0 |
| div_const | 1200000 | 0 | 0 | 0 |
| mod | 1200000 | 2640000 | 0 | 0 |
| cmp | 0 | 2640000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 2640000 | 0 | 1 |
| loop_for | 2642200 | 2642200 | 2401200 | 0 |
| call | 0 | 5280006 | 1200 | 10 |

## Static Resolution Warnings

- kernel_gramschmidt: unresolved loop bound
