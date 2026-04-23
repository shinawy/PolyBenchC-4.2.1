# Static Operation Report: gramschmidt

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 251690 |
| add | 201846 |
| sub | 0 |
| mul | 96000 |
| mul_const | 153603 |
| div | 48000 |
| div_const | 48000 |
| mod | 153600 |
| cmp | 105601 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 105601 |
| loop_for | 308320 |
| call | 211456 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 250080 |
| assign | int32 | 1607 |
| assign | ptr64 | 3 |
| add | float64 | 96000 |
| add | int32 | 105846 |
| mul | float64 | 48000 |
| mul | int32 | 48000 |
| mul_const | float64 | 48000 |
| mul_const | int32 | 105603 |
| div | float64 | 48000 |
| div_const | float64 | 48000 |
| mod | int32 | 153600 |
| cmp | int32 | 105601 |
| logical | int32 | 1 |
| unary | ptr64 | 9 |
| unary | unknown | 4 |
| if | int1 | 105601 |
| loop_for | int32 | 308320 |
| call | unknown | 211456 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 154042 | 442 | 97201 | 5 |
| add | 48000 | 105600 | 48240 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 48000 | 0 | 48000 | 0 |
| mul_const | 48000 | 105600 | 0 | 3 |
| div | 0 | 0 | 48000 | 0 |
| div_const | 48000 | 0 | 0 | 0 |
| mod | 48000 | 105600 | 0 | 0 |
| cmp | 0 | 105600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 105600 | 0 | 1 |
| loop_for | 106040 | 106040 | 96240 | 0 |
| call | 0 | 211206 | 240 | 10 |

## Static Resolution Warnings

- kernel_gramschmidt: unresolved loop bound
