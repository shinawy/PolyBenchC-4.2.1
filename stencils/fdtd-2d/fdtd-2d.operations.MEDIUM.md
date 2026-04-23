# Static Operation Report: fdtd-2d

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 14541213 |
| add | 14556307 |
| sub | 47732300 |
| mul | 144000 |
| mul_const | 14456103 |
| div | 0 |
| div_const | 144000 |
| mod | 144000 |
| cmp | 144001 |
| logical | 1 |
| bitwise | 0 |
| unary | 16 |
| if | 144001 |
| loop_for | 14588900 |
| call | 288020 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 14480200 |
| assign | int32 | 61009 |
| assign | ptr64 | 4 |
| add | float64 | 4756100 |
| add | int32 | 9800207 |
| sub | float64 | 33380300 |
| sub | int32 | 14352000 |
| mul | float64 | 144000 |
| mul_const | float64 | 14312100 |
| mul_const | int32 | 144003 |
| div_const | float64 | 144000 |
| mod | int32 | 144000 |
| cmp | int32 | 144001 |
| logical | int32 | 1 |
| unary | ptr64 | 11 |
| unary | unknown | 5 |
| if | int1 | 144001 |
| loop_for | int32 | 14588900 |
| call | unknown | 288020 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 144302 | 603 | 14396301 | 7 |
| add | 144000 | 144000 | 14268300 | 7 |
| sub | 0 | 0 | 47732300 | 0 |
| mul | 144000 | 0 | 0 | 0 |
| mul_const | 0 | 144000 | 14312100 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 144000 | 0 | 0 | 0 |
| mod | 0 | 144000 | 0 | 0 |
| cmp | 0 | 144000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 144000 | 0 | 1 |
| loop_for | 48300 | 144600 | 14396000 | 0 |
| call | 0 | 288008 | 0 | 12 |
