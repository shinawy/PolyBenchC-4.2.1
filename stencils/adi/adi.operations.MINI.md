# Static Operation Report: adi

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 43702 |
| add | 91530 |
| sub | 94040 |
| mul | 12960 |
| mul_const | 91128 |
| div | 25920 |
| div_const | 407 |
| mod | 400 |
| cmp | 401 |
| logical | 1 |
| bitwise | 0 |
| unary | 25933 |
| if | 401 |
| loop_for | 27500 |
| call | 816 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 42173 |
| assign | int32 | 1525 |
| assign | ptr64 | 4 |
| add | float64 | 64802 |
| add | int32 | 26728 |
| sub | float64 | 25920 |
| sub | int32 | 68120 |
| mul | float64 | 12960 |
| mul_const | float64 | 90724 |
| mul_const | int32 | 404 |
| div | float64 | 25920 |
| div_const | float64 | 407 |
| mod | int32 | 400 |
| cmp | int32 | 401 |
| logical | int32 | 1 |
| unary | float64 | 25922 |
| unary | ptr64 | 6 |
| unary | unknown | 5 |
| if | int1 | 401 |
| loop_for | int32 | 27500 |
| call | unknown | 816 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 421 | 21 | 43254 | 6 |
| add | 400 | 400 | 90722 | 8 |
| sub | 400 | 0 | 93640 | 0 |
| mul | 0 | 0 | 12960 | 0 |
| mul_const | 0 | 400 | 90724 | 4 |
| div | 0 | 0 | 25920 | 0 |
| div_const | 400 | 0 | 7 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 25922 | 11 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 420 | 420 | 26660 | 0 |
| call | 0 | 804 | 0 | 12 |
