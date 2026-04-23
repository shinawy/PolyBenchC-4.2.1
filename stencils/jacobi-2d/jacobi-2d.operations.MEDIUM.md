# Static Operation Report: jacobi-2d

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 12476107 |
| add | 74117304 |
| sub | 37001800 |
| mul | 125000 |
| mul_const | 12363302 |
| div | 0 |
| div_const | 125000 |
| mod | 62500 |
| cmp | 62501 |
| logical | 1 |
| bitwise | 0 |
| unary | 8 |
| if | 62501 |
| loop_for | 12476000 |
| call | 125012 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 12425800 |
| assign | int32 | 50305 |
| assign | ptr64 | 2 |
| add | float64 | 49328200 |
| add | int32 | 24789104 |
| sub | int32 | 37001800 |
| mul | float64 | 125000 |
| mul_const | float64 | 12300800 |
| mul_const | int32 | 62502 |
| div_const | float64 | 125000 |
| mod | int32 | 62500 |
| cmp | int32 | 62501 |
| logical | int32 | 1 |
| unary | ptr64 | 5 |
| unary | unknown | 3 |
| if | int1 | 62501 |
| loop_for | int32 | 12476000 |
| call | unknown | 125012 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 125251 | 251 | 12350601 | 4 |
| add | 250000 | 62500 | 73804800 | 4 |
| sub | 0 | 0 | 37001800 | 0 |
| mul | 125000 | 0 | 0 | 0 |
| mul_const | 0 | 62500 | 12300800 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 125000 | 0 | 0 | 0 |
| mod | 0 | 62500 | 0 | 0 |
| cmp | 0 | 62500 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 62500 | 0 | 1 |
| loop_for | 62750 | 62750 | 12350500 | 0 |
| call | 0 | 125004 | 0 | 8 |
