# Static Operation Report: 2mm

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 13277092018 |
| add | 13271800010 |
| sub | 0 |
| mul | 19603480000 |
| mul_const | 3840005 |
| div | 0 |
| div_const | 15640000 |
| mod | 19480000 |
| cmp | 3840001 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 3840001 |
| loop_for | 13274212000 |
| call | 7680018 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 13270360000 |
| assign | int32 | 6732011 |
| assign | ptr64 | 7 |
| add | float64 | 13248000000 |
| add | int32 | 23800010 |
| mul | float64 | 19587840000 |
| mul | int32 | 15640000 |
| mul_const | int32 | 3840005 |
| div_const | float64 | 15640000 |
| mod | int32 | 19480000 |
| cmp | int32 | 3840001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 3840001 |
| loop_for | int32 | 13274212000 |
| call | unknown | 7680018 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 15647206 | 1601 | 13261443202 | 9 |
| add | 19960000 | 3840000 | 13248000000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15640000 | 0 | 19587840000 | 0 |
| mul_const | 0 | 3840000 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15640000 | 0 | 0 | 0 |
| mod | 15640000 | 3840000 | 0 | 0 |
| cmp | 0 | 3840000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 3840000 | 0 | 1 |
| loop_for | 15647200 | 3841600 | 13254723200 | 0 |
| call | 0 | 7680004 | 0 | 14 |
