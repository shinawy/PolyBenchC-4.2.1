# Static Operation Report: trmm

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 145008 |
| add | 144004 |
| sub | 48000 |
| mul | 48000 |
| mul_const | 48002 |
| div | 0 |
| div_const | 48000 |
| mod | 96000 |
| cmp | 48001 |
| logical | 1 |
| bitwise | 0 |
| unary | 10 |
| if | 48001 |
| loop_for | 144600 |
| call | 96012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 96200 |
| assign | int32 | 48805 |
| assign | ptr64 | 3 |
| add | int32 | 144004 |
| sub | int32 | 48000 |
| mul | float64 | 48000 |
| mul_const | int32 | 48002 |
| div_const | float64 | 48000 |
| mod | int32 | 96000 |
| cmp | int32 | 48001 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 6 |
| unary | unknown | 3 |
| if | int1 | 48001 |
| loop_for | int32 | 144600 |
| call | unknown | 96012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 48602 | 201 | 96201 | 4 |
| add | 48000 | 48000 | 48000 | 4 |
| sub | 48000 | 0 | 0 | 0 |
| mul | 0 | 0 | 48000 | 0 |
| mul_const | 0 | 48000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 48000 | 0 | 0 | 0 |
| mod | 48000 | 48000 | 0 | 0 |
| cmp | 0 | 48000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 48000 | 0 | 1 |
| loop_for | 48200 | 48200 | 48200 | 0 |
| call | 0 | 96004 | 0 | 8 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- kernel_trmm: unresolved loop bound
