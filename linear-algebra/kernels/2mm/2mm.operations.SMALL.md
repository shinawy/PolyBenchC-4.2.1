# Static Operation Report: 2mm

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 324238 |
| add | 320710 |
| sub | 0 |
| mul | 456700 |
| mul_const | 3205 |
| div | 0 |
| div_const | 13500 |
| mod | 16700 |
| cmp | 3201 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 3201 |
| loop_for | 322220 |
| call | 6418 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 318700 |
| assign | int32 | 5531 |
| assign | ptr64 | 7 |
| add | float64 | 300000 |
| add | int32 | 20710 |
| mul | float64 | 443200 |
| mul | int32 | 13500 |
| mul_const | int32 | 3205 |
| div_const | float64 | 13500 |
| mod | int32 | 16700 |
| cmp | int32 | 3201 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 3201 |
| loop_for | int32 | 322220 |
| call | unknown | 6418 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 13706 | 41 | 310482 | 9 |
| add | 17500 | 3200 | 300000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 13500 | 0 | 443200 | 0 |
| mul_const | 0 | 3200 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 13500 | 0 | 0 | 0 |
| mod | 13500 | 3200 | 0 | 0 |
| cmp | 0 | 3200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 3200 | 0 | 1 |
| loop_for | 13700 | 3240 | 305280 | 0 |
| call | 0 | 6404 | 0 | 14 |
