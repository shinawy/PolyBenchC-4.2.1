# Static Operation Report: 3mm

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 21637134420 |
| add | 21628800014 |
| sub | 0 |
| mul | 21616400000 |
| mul_const | 19920007 |
| div | 0 |
| div_const | 16400000 |
| mod | 19920000 |
| cmp | 3520001 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 3520001 |
| loop_for | 21630294400 |
| call | 7040022 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 21626760000 |
| assign | int32 | 10374413 |
| assign | ptr64 | 7 |
| add | float64 | 21600000000 |
| add | int32 | 28800014 |
| mul | float64 | 21600000000 |
| mul | int32 | 16400000 |
| mul_const | int32 | 19920007 |
| div_const | float64 | 16400000 |
| mod | int32 | 19920000 |
| cmp | int32 | 3520001 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 8 |
| if | int1 | 3520001 |
| loop_for | int32 | 21630294400 |
| call | unknown | 7040022 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 16407804 | 1601 | 21620725003 | 12 |
| add | 25280000 | 3520000 | 21600000000 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16400000 | 0 | 21600000000 | 0 |
| mul_const | 16400000 | 3520000 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16400000 | 0 | 0 | 0 |
| mod | 16400000 | 3520000 | 0 | 0 |
| cmp | 0 | 3520000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 3520000 | 0 | 1 |
| loop_for | 16407800 | 3521600 | 21610365000 | 0 |
| call | 0 | 7040004 | 0 | 18 |
