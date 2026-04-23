# Static Operation Report: gesummv

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 6767811 |
| add | 6761307 |
| sub | 0 |
| mul | 6762600 |
| mul_const | 2 |
| div | 0 |
| div_const | 3381300 |
| mod | 3382600 |
| cmp | 1301 |
| logical | 1 |
| bitwise | 0 |
| unary | 19 |
| if | 1301 |
| loop_for | 3383900 |
| call | 2618 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 6765200 |
| assign | int32 | 2604 |
| assign | ptr64 | 7 |
| add | float64 | 3381300 |
| add | int32 | 3380007 |
| mul | float64 | 3382600 |
| mul | int32 | 3380000 |
| mul_const | int32 | 2 |
| div_const | float64 | 3381300 |
| mod | int32 | 3382600 |
| cmp | int32 | 1301 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 11 |
| unary | unknown | 6 |
| if | int1 | 1301 |
| loop_for | int32 | 3383900 |
| call | unknown | 2618 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 3382603 | 1 | 3385201 | 6 |
| add | 3380000 | 0 | 3381300 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3380000 | 0 | 3382600 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3381300 | 0 | 0 | 0 |
| mod | 3381300 | 1300 | 0 | 0 |
| cmp | 0 | 1300 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 1300 | 0 | 1 |
| loop_for | 1691300 | 1300 | 1691300 | 0 |
| call | 0 | 2604 | 0 | 14 |
