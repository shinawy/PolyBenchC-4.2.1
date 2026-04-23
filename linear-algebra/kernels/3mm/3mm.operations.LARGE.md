# Static Operation Report: 3mm

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 2709287220 |
| add | 2707200014 |
| sub | 0 |
| mul | 2704100000 |
| mul_const | 4980007 |
| div | 0 |
| div_const | 4100000 |
| mod | 4980000 |
| cmp | 880001 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 880001 |
| loop_for | 2707577200 |
| call | 1760022 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 2706690000 |
| assign | int32 | 2597213 |
| assign | ptr64 | 7 |
| add | float64 | 2700000000 |
| add | int32 | 7200014 |
| mul | float64 | 2700000000 |
| mul | int32 | 4100000 |
| mul_const | int32 | 4980007 |
| div_const | float64 | 4100000 |
| mod | int32 | 4980000 |
| cmp | int32 | 880001 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 8 |
| if | int1 | 880001 |
| loop_for | int32 | 2707577200 |
| call | unknown | 1760022 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 4103904 | 801 | 2705182503 | 12 |
| add | 6320000 | 880000 | 2700000000 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4100000 | 0 | 2700000000 | 0 |
| mul_const | 4100000 | 880000 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4100000 | 0 | 0 | 0 |
| mod | 4100000 | 880000 | 0 | 0 |
| cmp | 0 | 880000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 880000 | 0 | 1 |
| loop_for | 4103900 | 880800 | 2702592500 | 0 |
| call | 0 | 1760004 | 0 | 18 |
