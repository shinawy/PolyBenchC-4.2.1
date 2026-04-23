# Static Operation Report: gemver

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 64052019 |
| add | 64024010 |
| sub | 0 |
| mul | 112000000 |
| mul_const | 1 |
| div | 0 |
| div_const | 16040000 |
| mod | 16004000 |
| cmp | 4001 |
| logical | 1 |
| bitwise | 0 |
| unary | 33 |
| if | 4001 |
| loop_for | 64024000 |
| call | 8026 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 64036001 |
| assign | int32 | 16007 |
| assign | ptr64 | 11 |
| add | float64 | 64004000 |
| add | int32 | 20010 |
| mul | float64 | 96000000 |
| mul | int32 | 16000000 |
| mul_const | int32 | 1 |
| div_const | float64 | 16040000 |
| mod | int32 | 16004000 |
| cmp | int32 | 4001 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 21 |
| unary | unknown | 10 |
| if | int1 | 4001 |
| loop_for | int32 | 64024000 |
| call | unknown | 8026 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 16036004 | 1 | 48016004 | 10 |
| add | 20000 | 0 | 64004000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16000000 | 0 | 96000000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16040000 | 0 | 0 | 0 |
| mod | 16000000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 16004000 | 4000 | 48016000 | 0 |
| call | 0 | 8004 | 0 | 22 |
