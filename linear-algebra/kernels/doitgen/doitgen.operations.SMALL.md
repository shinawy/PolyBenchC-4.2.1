# Static Operation Report: doitgen

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 513015 |
| add | 495006 |
| sub | 0 |
| mul | 465900 |
| mul_const | 45003 |
| div | 0 |
| div_const | 15900 |
| mod | 30900 |
| cmp | 15001 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 15001 |
| loop_for | 512505 |
| call | 30014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 495900 |
| assign | int32 | 17112 |
| assign | ptr64 | 3 |
| add | float64 | 450000 |
| add | int32 | 45006 |
| mul | float64 | 450000 |
| mul | int32 | 15900 |
| mul_const | int32 | 45003 |
| div_const | float64 | 15900 |
| mod | int32 | 30900 |
| cmp | int32 | 15001 |
| logical | int32 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 15001 |
| loop_for | int32 | 512505 |
| call | unknown | 30014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 16457 | 526 | 496026 | 6 |
| add | 15000 | 30000 | 450000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15900 | 0 | 450000 | 0 |
| mul_const | 0 | 45000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15900 | 0 | 0 | 0 |
| mod | 15900 | 15000 | 0 | 0 |
| cmp | 0 | 15000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 15000 | 0 | 1 |
| loop_for | 16455 | 15525 | 480525 | 0 |
| call | 0 | 30004 | 0 | 10 |
