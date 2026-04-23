# Static Operation Report: correlation

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 41093 |
| add | 30485 |
| sub | 24082 |
| mul | 24000 |
| mul_const | 6402 |
| div | 8160 |
| div_const | 8000 |
| mod | 6400 |
| cmp | 6481 |
| logical | 1 |
| bitwise | 0 |
| unary | 13 |
| if | 6481 |
| loop_for | 38919 |
| call | 20896 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 40561 |
| assign | int32 | 527 |
| assign | ptr64 | 5 |
| add | float64 | 24000 |
| add | int32 | 6485 |
| sub | float64 | 24000 |
| sub | int32 | 82 |
| mul | float64 | 16000 |
| mul | int32 | 8000 |
| mul_const | int32 | 6402 |
| div | float64 | 8160 |
| div_const | float64 | 8000 |
| mod | int32 | 6400 |
| cmp | float64 | 80 |
| cmp | int32 | 6401 |
| logical | int32 | 1 |
| unary | float64 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 6481 |
| loop_for | int32 | 38919 |
| call | unknown | 20896 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 8102 | 81 | 32904 | 6 |
| add | 8000 | 6400 | 16079 | 6 |
| sub | 0 | 0 | 24082 | 0 |
| mul | 8000 | 0 | 16000 | 0 |
| mul_const | 0 | 6400 | 0 | 2 |
| div | 0 | 0 | 8160 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 80 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 6400 | 80 | 1 |
| loop_for | 8100 | 6480 | 24339 | 0 |
| call | 0 | 12804 | 8080 | 12 |

## Static Resolution Warnings

- kernel_correlation: unresolved loop bound
