# Static Operation Report: durbin

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 16002 |
| add | 4001 |
| sub | 3999 |
| mul | 1999 |
| mul_const | 1999 |
| div | 0 |
| div_const | 1999 |
| mod | 2000 |
| cmp | 2001 |
| logical | 1 |
| bitwise | 0 |
| unary | 2008 |
| if | 2001 |
| loop_for | 5999 |
| call | 4012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 9999 |
| assign | int32 | 6001 |
| assign | ptr64 | 2 |
| add | float64 | 1999 |
| add | int32 | 2002 |
| sub | float64 | 1999 |
| sub | int32 | 2000 |
| mul | float64 | 1999 |
| mul_const | float64 | 1999 |
| div_const | float64 | 1999 |
| mod | int32 | 2000 |
| cmp | int32 | 2001 |
| logical | int32 | 1 |
| unary | float64 | 2001 |
| unary | ptr64 | 4 |
| unary | unknown | 3 |
| if | int1 | 2001 |
| loop_for | int32 | 5999 |
| call | unknown | 4012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 2001 | 1 | 13997 | 3 |
| add | 2000 | 0 | 1999 | 2 |
| sub | 2000 | 0 | 1999 | 0 |
| mul | 0 | 0 | 1999 | 0 |
| mul_const | 0 | 0 | 1999 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 1999 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 2001 | 7 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 2000 | 2000 | 1999 | 0 |
| call | 0 | 4004 | 0 | 8 |

## Static Resolution Warnings

- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
- kernel_durbin: unresolved loop bound
