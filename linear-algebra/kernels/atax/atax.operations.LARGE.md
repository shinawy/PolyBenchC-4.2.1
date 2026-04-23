# Static Operation Report: atax

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 11981812 |
| add | 11972105 |
| sub | 0 |
| mul | 7980000 |
| mul_const | 3990001 |
| div | 0 |
| div_const | 3992100 |
| mod | 3992100 |
| cmp | 2101 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 2101 |
| loop_for | 11980100 |
| call | 4216 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11976101 |
| assign | int32 | 5707 |
| assign | ptr64 | 4 |
| add | float64 | 7982100 |
| add | int32 | 3990005 |
| mul | float64 | 7980000 |
| mul_const | int32 | 3990001 |
| div_const | float64 | 3992100 |
| mod | int32 | 3992100 |
| cmp | int32 | 2101 |
| logical | int32 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 2101 |
| loop_for | int32 | 11980100 |
| call | unknown | 4216 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 3994003 | 1 | 7987802 | 6 |
| add | 3992100 | 0 | 7980000 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 7980000 | 0 |
| mul_const | 3990000 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3992100 | 0 | 0 | 0 |
| mod | 3990000 | 2100 | 0 | 0 |
| cmp | 0 | 2100 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 2100 | 0 | 1 |
| loop_for | 3994000 | 2100 | 7984000 | 0 |
| call | 0 | 4204 | 0 | 12 |
