# Static Operation Report: heat-3d

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 510847 |
| add | 4231046 |
| sub | 3328720 |
| mul | 0 |
| mul_const | 2831364 |
| div | 0 |
| div_const | 8000 |
| mod | 8000 |
| cmp | 8001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 8001 |
| loop_for | 510800 |
| call | 16011 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 482560 |
| assign | int32 | 28285 |
| assign | ptr64 | 2 |
| add | float64 | 2799360 |
| add | int32 | 1431686 |
| sub | float64 | 1399680 |
| sub | int32 | 1929040 |
| mul_const | float64 | 2807360 |
| mul_const | int32 | 24004 |
| div_const | float64 | 8000 |
| mod | int32 | 8000 |
| cmp | int32 | 8001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 8001 |
| loop_for | int32 | 510800 |
| call | unknown | 16011 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 16421 | 421 | 494001 | 4 |
| add | 16000 | 16000 | 4199040 | 6 |
| sub | 8000 | 0 | 3320720 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 8000 | 24000 | 2799360 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 8000 | 0 | 0 |
| cmp | 0 | 8000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 8000 | 0 | 1 |
| loop_for | 8420 | 8420 | 493960 | 0 |
| call | 0 | 16004 | 0 | 7 |
