# Static Operation Report: fdtd-2d

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1803506013 |
| add | 1803901507 |
| sub | 5993301500 |
| mul | 3600000 |
| mul_const | 1801400503 |
| div | 0 |
| div_const | 3600000 |
| mod | 3600000 |
| cmp | 3600001 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 3600001 |
| loop_for | 1804704500 |
| call | 7200020 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1802001000 |
| assign | int32 | 1505009 |
| assign | ptr64 | 4 |
| add | float64 | 598900500 |
| add | int32 | 1205001007 |
| sub | float64 | 4194501500 |
| sub | int32 | 1798800000 |
| mul | float64 | 3600000 |
| mul_const | float64 | 1797800500 |
| mul_const | int32 | 3600003 |
| div_const | float64 | 3600000 |
| mod | int32 | 3600000 |
| cmp | int32 | 3600001 |
| logical | int32 | 1 |
| unary | ptr64 | 11 |
| unary | unknown | 5 |
| if | int1 | 3600001 |
| loop_for | int32 | 1804704500 |
| call | unknown | 7200020 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 3601502 | 3003 | 1799901501 | 7 |
| add | 3600000 | 3600000 | 1796701500 | 7 |
| sub | 0 | 0 | 5993301500 | 0 |
| mul | 3600000 | 0 | 0 | 0 |
| mul_const | 0 | 3600000 | 1797800500 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3600000 | 0 | 0 | 0 |
| mod | 0 | 3600000 | 0 | 0 |
| cmp | 0 | 3600000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 3600000 | 0 | 1 |
| loop_for | 1201500 | 3603000 | 1799900000 | 0 |
| call | 0 | 7200008 | 0 | 12 |
