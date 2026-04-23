# Static Operation Report: syr2k

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 22373011 |
| add | 23920006 |
| sub | 0 |
| mul | 17160000 |
| mul_const | 6760003 |
| div | 0 |
| div_const | 17160000 |
| mod | 23920000 |
| cmp | 6760001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 6760001 |
| loop_for | 23930400 |
| call | 13520014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 17160000 |
| assign | int32 | 5213006 |
| assign | ptr64 | 5 |
| add | int32 | 23920006 |
| mul | int32 | 17160000 |
| mul_const | int32 | 6760003 |
| div_const | float64 | 17160000 |
| mod | int32 | 23920000 |
| cmp | int32 | 6760001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 6760001 |
| loop_for | int32 | 23930400 |
| call | unknown | 13520014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 17165204 | 2601 | 5205201 | 5 |
| add | 17160000 | 6760000 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 17160000 | 0 | 0 | 0 |
| mul_const | 0 | 6760000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 17160000 | 0 | 0 | 0 |
| mod | 17160000 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 6760000 | 0 | 1 |
| loop_for | 11965200 | 6762600 | 5202600 | 0 |
| call | 0 | 13520004 | 0 | 10 |

## Static Resolution Warnings

- kernel_syr2k: unresolved loop bound
- kernel_syr2k: unresolved loop bound
