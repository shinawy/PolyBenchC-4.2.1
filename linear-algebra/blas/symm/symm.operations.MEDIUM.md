# Static Operation Report: symm

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 241011 |
| add | 240206 |
| sub | 48000 |
| mul | 144000 |
| mul_const | 96003 |
| div | 0 |
| div_const | 96000 |
| mod | 144000 |
| cmp | 48001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15 |
| if | 48001 |
| loop_for | 144800 |
| call | 96014 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 192000 |
| assign | int32 | 49006 |
| assign | ptr64 | 5 |
| add | float64 | 96000 |
| add | int32 | 144206 |
| sub | int32 | 48000 |
| mul | float64 | 144000 |
| mul_const | float64 | 48000 |
| mul_const | int32 | 48003 |
| div_const | float64 | 96000 |
| mod | int32 | 144000 |
| cmp | int32 | 48001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 48001 |
| loop_for | int32 | 144800 |
| call | unknown | 96014 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 96604 | 201 | 144201 | 5 |
| add | 96200 | 48000 | 96000 | 6 |
| sub | 48000 | 0 | 0 | 0 |
| mul | 0 | 0 | 144000 | 0 |
| mul_const | 0 | 48000 | 48000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 96000 | 0 | 0 | 0 |
| mod | 96000 | 48000 | 0 | 0 |
| cmp | 0 | 48000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 48000 | 0 | 1 |
| loop_for | 48400 | 48200 | 48200 | 0 |
| call | 0 | 96004 | 0 | 10 |

## Static Resolution Warnings

- init_array: unresolved loop bound
- init_array: unresolved loop bound
- kernel_symm: unresolved loop bound
