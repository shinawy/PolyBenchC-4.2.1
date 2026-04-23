# Static Operation Report: heat-3d

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 1660560047 |
| add | 14794200006 |
| sub | 11531037000 |
| mul | 0 |
| mul_const | 9865104004 |
| div | 0 |
| div_const | 1728000 |
| mod | 1728000 |
| cmp | 1728001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 1728001 |
| loop_for | 1660559540 |
| call | 3456011 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1646488000 |
| assign | int32 | 14072045 |
| assign | ptr64 | 2 |
| add | float64 | 9858192000 |
| add | int32 | 4936008006 |
| sub | float64 | 4929096000 |
| sub | int32 | 6601941000 |
| mul_const | float64 | 9859920000 |
| mul_const | int32 | 5184004 |
| div_const | float64 | 1728000 |
| mod | int32 | 1728000 |
| cmp | int32 | 1728001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 1728001 |
| loop_for | int32 | 1660559540 |
| call | unknown | 3456011 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 3470521 | 14521 | 1657075001 | 4 |
| add | 3456000 | 3456000 | 14787288000 | 6 |
| sub | 1728000 | 0 | 11529309000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 1728000 | 5184000 | 9858192000 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1728000 | 0 | 0 | 0 |
| mod | 0 | 1728000 | 0 | 0 |
| cmp | 0 | 1728000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 1728000 | 0 | 1 |
| loop_for | 1742520 | 1742520 | 1657074500 | 0 |
| call | 0 | 3456004 | 0 | 7 |
