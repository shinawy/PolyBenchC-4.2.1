# Static Operation Report: correlation

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 315173 |
| add | 245045 |
| sub | 187442 |
| mul | 187200 |
| mul_const | 57602 |
| div | 62880 |
| div_const | 62400 |
| mod | 57600 |
| cmp | 57841 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 57841 |
| loop_for | 308679 |
| call | 177856 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 313681 |
| assign | int32 | 1487 |
| assign | ptr64 | 5 |
| add | float64 | 187200 |
| add | int32 | 57845 |
| sub | float64 | 187200 |
| sub | int32 | 242 |
| mul | float64 | 124800 |
| mul | int32 | 62400 |
| mul_const | int32 | 57602 |
| div | float64 | 62880 |
| div_const | float64 | 62400 |
| mod | int32 | 57600 |
| cmp | float64 | 240 |
| cmp | int32 | 57601 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 57841 |
| loop_for | int32 | 308679 |
| call | unknown | 177856 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 62662 | 241 | 252264 | 6 |
| add | 62400 | 57600 | 125039 | 6 |
| sub | 0 | 0 | 187442 | 0 |
| mul | 62400 | 0 | 124800 | 0 |
| mul_const | 0 | 57600 | 0 | 2 |
| div | 0 | 0 | 62880 | 0 |
| div_const | 62400 | 0 | 0 | 0 |
| mod | 0 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 240 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 57600 | 240 | 1 |
| loop_for | 62660 | 57840 | 188179 | 0 |
| call | 0 | 115204 | 62640 | 12 |

## Static Resolution Warnings

- kernel_correlation: unresolved loop bound
