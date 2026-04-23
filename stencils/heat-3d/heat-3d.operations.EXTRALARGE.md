# Static Operation Report: heat-3d

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 15619670407 |
| add | 139755056006 |
| sub | 108839098000 |
| mul | 0 |
| mul_const | 93180704004 |
| div | 0 |
| div_const | 8000000 |
| mod | 8000000 |
| cmp | 8000001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 8000001 |
| loop_for | 15619669400 |
| call | 16000011 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 15540784000 |
| assign | int32 | 78886405 |
| assign | ptr64 | 2 |
| add | float64 | 93148704000 |
| add | int32 | 46606352006 |
| sub | float64 | 46574352000 |
| sub | int32 | 62264746000 |
| mul_const | float64 | 93156704000 |
| mul_const | int32 | 24000004 |
| div_const | float64 | 8000000 |
| mod | int32 | 8000000 |
| cmp | int32 | 8000001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 8000001 |
| loop_for | int32 | 15619669400 |
| call | unknown | 16000011 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 16040201 | 40201 | 15603590001 | 4 |
| add | 16000000 | 16000000 | 139723056000 | 6 |
| sub | 8000000 | 0 | 108831098000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 8000000 | 24000000 | 93148704000 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 8000000 | 0 | 0 | 0 |
| mod | 0 | 8000000 | 0 | 0 |
| cmp | 0 | 8000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 8000000 | 0 | 1 |
| loop_for | 8040200 | 8040200 | 15603589000 | 0 |
| call | 0 | 16000004 | 0 | 7 |
