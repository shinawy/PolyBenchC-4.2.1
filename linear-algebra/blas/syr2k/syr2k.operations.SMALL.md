# Static Operation Report: syr2k

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 21211 |
| add | 22406 |
| sub | 0 |
| mul | 16000 |
| mul_const | 6403 |
| div | 0 |
| div_const | 16000 |
| mod | 22400 |
| cmp | 6401 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 6401 |
| loop_for | 22720 |
| call | 12814 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 16000 |
| assign | int32 | 5206 |
| assign | ptr64 | 5 |
| add | int32 | 22406 |
| mul | int32 | 16000 |
| mul_const | int32 | 6403 |
| div_const | float64 | 16000 |
| mod | int32 | 22400 |
| cmp | int32 | 6401 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 6401 |
| loop_for | int32 | 22720 |
| call | unknown | 12814 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 16164 | 81 | 4961 | 5 |
| add | 16000 | 6400 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16000 | 0 | 0 | 0 |
| mul_const | 0 | 6400 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16000 | 0 | 0 | 0 |
| mod | 16000 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 6400 | 0 | 1 |
| loop_for | 11360 | 6480 | 4880 | 0 |
| call | 0 | 12804 | 0 | 10 |

## Static Resolution Warnings

- kernel_syr2k: unresolved loop bound
- kernel_syr2k: unresolved loop bound
