# Static Operation Report: jacobi-2d

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 643027 |
| add | 3757624 |
| sub | 1872720 |
| mul | 16200 |
| mul_const | 627622 |
| div | 0 |
| div_const | 16200 |
| mod | 8100 |
| cmp | 8101 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 8101 |
| loop_for | 642980 |
| call | 16212 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 635720 |
| assign | int32 | 7305 |
| assign | ptr64 | 2 |
| add | float64 | 2494280 |
| add | int32 | 1263344 |
| sub | int32 | 1872720 |
| mul | float64 | 16200 |
| mul_const | float64 | 619520 |
| mul_const | int32 | 8102 |
| div_const | float64 | 16200 |
| mod | int32 | 8100 |
| cmp | int32 | 8101 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 8101 |
| loop_for | int32 | 642980 |
| call | unknown | 16212 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 16291 | 91 | 626641 | 4 |
| add | 32400 | 8100 | 3717120 | 4 |
| sub | 0 | 0 | 1872720 | 0 |
| mul | 16200 | 0 | 0 | 0 |
| mul_const | 0 | 8100 | 619520 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16200 | 0 | 0 | 0 |
| mod | 0 | 8100 | 0 | 0 |
| cmp | 0 | 8100 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 8100 | 0 | 1 |
| loop_for | 8190 | 8190 | 626600 | 0 |
| call | 0 | 16204 | 0 | 8 |
