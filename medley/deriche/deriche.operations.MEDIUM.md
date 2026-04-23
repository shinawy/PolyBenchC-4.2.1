# Static Operation Report: deriche

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 7271308 |
| add | 5529610 |
| sub | 1204 |
| mul | 1036807 |
| mul_const | 6220808 |
| div | 1 |
| div_const | 345600 |
| mod | 691200 |
| cmp | 345601 |
| logical | 1 |
| bitwise | 0 |
| unary | 24 |
| if | 345601 |
| loop_for | 2770080 |
| call | 691225 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 7266013 |
| assign | int32 | 5290 |
| assign | ptr64 | 5 |
| add | float32 | 4838402 |
| add | int32 | 691208 |
| sub | float32 | 4 |
| sub | int32 | 1200 |
| mul | float32 | 1036807 |
| mul_const | float32 | 5184004 |
| mul_const | int32 | 1036804 |
| div | float32 | 1 |
| div_const | float32 | 345600 |
| mod | int32 | 691200 |
| cmp | int32 | 345601 |
| logical | int32 | 1 |
| unary | float32 | 10 |
| unary | ptr64 | 8 |
| unary | unknown | 6 |
| if | int1 | 345601 |
| loop_for | int32 | 2770080 |
| call | unknown | 691225 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_deriche | main |
|---|---:|---:|---:|---:|
| assign | 346322 | 721 | 6924259 | 6 |
| add | 345600 | 345600 | 4838402 | 8 |
| sub | 0 | 0 | 1204 | 0 |
| mul | 0 | 0 | 1036807 | 0 |
| mul_const | 691200 | 345600 | 5184004 | 4 |
| div | 0 | 0 | 1 | 0 |
| div_const | 345600 | 0 | 0 | 0 |
| mod | 345600 | 345600 | 0 | 0 |
| cmp | 0 | 345600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 10 | 13 |
| if | 0 | 345600 | 0 | 1 |
| loop_for | 346320 | 346320 | 2077440 | 0 |
| call | 0 | 691204 | 9 | 12 |
