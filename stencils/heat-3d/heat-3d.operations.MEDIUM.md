# Static Operation Report: heat-3d

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 11402287 |
| add | 99025606 |
| sub | 77477800 |
| mul | 0 |
| mul_const | 66102404 |
| div | 0 |
| div_const | 64000 |
| mod | 64000 |
| cmp | 64001 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 64001 |
| loop_for | 11402180 |
| call | 128011 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11102400 |
| assign | int32 | 299885 |
| assign | ptr64 | 2 |
| add | float64 | 65846400 |
| add | int32 | 33179206 |
| sub | float64 | 32923200 |
| sub | int32 | 44554600 |
| mul_const | float64 | 65910400 |
| mul_const | int32 | 192004 |
| div_const | float64 | 64000 |
| mod | int32 | 64000 |
| cmp | int32 | 64001 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 64001 |
| loop_for | int32 | 11402180 |
| call | unknown | 128011 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 129641 | 1641 | 11271001 | 4 |
| add | 128000 | 128000 | 98769600 | 6 |
| sub | 64000 | 0 | 77413800 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 64000 | 192000 | 65846400 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 64000 | 0 | 0 | 0 |
| mod | 0 | 64000 | 0 | 0 |
| cmp | 0 | 64000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 64000 | 0 | 1 |
| loop_for | 65640 | 65640 | 11270900 | 0 |
| call | 0 | 128004 | 0 | 7 |
