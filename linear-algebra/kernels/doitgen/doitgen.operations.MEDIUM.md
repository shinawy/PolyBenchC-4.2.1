# Static Operation Report: doitgen

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 7691820 |
| add | 7560006 |
| sub | 0 |
| mul | 7323600 |
| mul_const | 360003 |
| div | 0 |
| div_const | 123600 |
| mod | 243600 |
| cmp | 120001 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 120001 |
| loop_for | 7689810 |
| call | 240014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 7563600 |
| assign | int32 | 128217 |
| assign | ptr64 | 3 |
| add | float64 | 7200000 |
| add | int32 | 360006 |
| mul | float64 | 7200000 |
| mul | int32 | 123600 |
| mul_const | int32 | 360003 |
| div_const | float64 | 123600 |
| mod | int32 | 243600 |
| cmp | int32 | 120001 |
| logical | int32 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 4 |
| if | int1 | 120001 |
| loop_for | int32 | 7689810 |
| call | unknown | 240014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 125712 | 2051 | 7564051 | 6 |
| add | 120000 | 240000 | 7200000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 123600 | 0 | 7200000 | 0 |
| mul_const | 0 | 360000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 123600 | 0 | 0 | 0 |
| mod | 123600 | 120000 | 0 | 0 |
| cmp | 0 | 120000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 120000 | 0 | 1 |
| loop_for | 125710 | 122050 | 7442050 | 0 |
| call | 0 | 240004 | 0 | 10 |
