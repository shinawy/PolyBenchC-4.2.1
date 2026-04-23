# Static Operation Report: syr2k

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 5046011 |
| add | 5280006 |
| sub | 0 |
| mul | 3840000 |
| mul_const | 1440003 |
| div | 0 |
| div_const | 3840000 |
| mod | 5280000 |
| cmp | 1440001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 1440001 |
| loop_for | 5284800 |
| call | 2880014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 3840000 |
| assign | int32 | 1206006 |
| assign | ptr64 | 5 |
| add | int32 | 5280006 |
| mul | int32 | 3840000 |
| mul_const | int32 | 1440003 |
| div_const | float64 | 3840000 |
| mod | int32 | 5280000 |
| cmp | int32 | 1440001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 1440001 |
| loop_for | int32 | 5284800 |
| call | unknown | 2880014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 3842404 | 1201 | 1202401 | 5 |
| add | 3840000 | 1440000 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3840000 | 0 | 0 | 0 |
| mul_const | 0 | 1440000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3840000 | 0 | 0 | 0 |
| mod | 3840000 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 1440000 | 0 | 1 |
| loop_for | 2642400 | 1441200 | 1201200 | 0 |
| call | 0 | 2880004 | 0 | 10 |

## Static Resolution Warnings

- kernel_syr2k: unresolved loop bound
- kernel_syr2k: unresolved loop bound
