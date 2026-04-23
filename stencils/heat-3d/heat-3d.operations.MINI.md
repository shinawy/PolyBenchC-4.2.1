# Static Operation Report: heat-3d

Generated: 2026-04-21T09:42:47
Dataset mode: MINI
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 25627 |
| add | 188326 |
| sub | 150160 |
| mul | 0 |
| mul_const | 126884 |
| div | 0 |
| div_const | 1000 |
| mod | 1000 |
| cmp | 1001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 1001 |
| loop_for | 25600 |
| call | 2011 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 22480 |
| assign | int32 | 3145 |
| assign | ptr64 | 2 |
| add | float64 | 122880 |
| add | int32 | 65446 |
| sub | float64 | 61440 |
| sub | int32 | 88720 |
| mul_const | float64 | 123880 |
| mul_const | int32 | 3004 |
| div_const | float64 | 1000 |
| mod | int32 | 1000 |
| cmp | int32 | 1001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 1001 |
| loop_for | int32 | 25600 |
| call | unknown | 2011 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 2111 | 111 | 23401 | 4 |
| add | 2000 | 2000 | 184320 | 6 |
| sub | 1000 | 0 | 149160 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 1000 | 3000 | 122880 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1000 | 0 | 0 | 0 |
| mod | 0 | 1000 | 0 | 0 |
| cmp | 0 | 1000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 1000 | 0 | 1 |
| loop_for | 1110 | 1110 | 23380 | 0 |
| call | 0 | 2004 | 0 | 7 |
