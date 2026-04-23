# Static Operation Report: seidel-2d

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 16004011006 |
| add | 223824056002 |
| sub | 111896026001 |
| mul | 16000000 |
| mul_const | 16000001 |
| div | 0 |
| div_const | 16000004000 |
| mod | 16000000 |
| cmp | 16000001 |
| logical | 1 |
| bitwise | 0 |
| unary | 5 |
| if | 16000001 |
| loop_for | 16020011000 |
| call | 32000010 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 16000004000 |
| assign | int32 | 4007005 |
| assign | ptr64 | 1 |
| add | float64 | 127888032000 |
| add | int32 | 95936024002 |
| sub | int32 | 111896026001 |
| mul | float64 | 16000000 |
| mul_const | int32 | 16000001 |
| div_const | float64 | 16000004000 |
| mod | int32 | 16000000 |
| cmp | int32 | 16000001 |
| logical | int32 | 1 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 16000001 |
| loop_for | int32 | 16020011000 |
| call | unknown | 32000010 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 16004001 | 4001 | 15988003001 | 3 |
| add | 32000000 | 16000000 | 223776056000 | 2 |
| sub | 0 | 0 | 111896026001 | 0 |
| mul | 16000000 | 0 | 0 | 0 |
| mul_const | 0 | 16000000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16000000 | 0 | 15984004000 | 0 |
| mod | 0 | 16000000 | 0 | 0 |
| cmp | 0 | 16000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 16000000 | 0 | 1 |
| loop_for | 16004000 | 16004000 | 15988003000 | 0 |
| call | 0 | 32000004 | 0 | 6 |
