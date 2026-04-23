# Static Operation Report: syr2k

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 202811 |
| add | 211206 |
| sub | 0 |
| mul | 153600 |
| mul_const | 57603 |
| div | 0 |
| div_const | 153600 |
| mod | 211200 |
| cmp | 57601 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 57601 |
| loop_for | 212160 |
| call | 115214 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 153600 |
| assign | int32 | 49206 |
| assign | ptr64 | 5 |
| add | int32 | 211206 |
| mul | int32 | 153600 |
| mul_const | int32 | 57603 |
| div_const | float64 | 153600 |
| mod | int32 | 211200 |
| cmp | int32 | 57601 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 57601 |
| loop_for | int32 | 212160 |
| call | unknown | 115214 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 154084 | 241 | 48481 | 5 |
| add | 153600 | 57600 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 153600 | 0 | 0 | 0 |
| mul_const | 0 | 57600 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 153600 | 0 | 0 | 0 |
| mod | 153600 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 57600 | 0 | 1 |
| loop_for | 106080 | 57840 | 48240 | 0 |
| call | 0 | 115204 | 0 | 10 |

## Static Resolution Warnings

- kernel_syr2k: unresolved loop bound
- kernel_syr2k: unresolved loop bound
