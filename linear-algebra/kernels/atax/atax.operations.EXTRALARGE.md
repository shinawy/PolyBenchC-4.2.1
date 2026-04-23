# Static Operation Report: atax

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 11891612 |
| add | 11882205 |
| sub | 0 |
| mul | 7920000 |
| mul_const | 3960001 |
| div | 0 |
| div_const | 3962200 |
| mod | 3962200 |
| cmp | 2201 |
| logical | 1 |
| bitwise | 0 |
| unary | 12 |
| if | 2201 |
| loop_for | 11890200 |
| call | 4416 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 11886201 |
| assign | int32 | 5407 |
| assign | ptr64 | 4 |
| add | float64 | 7922200 |
| add | int32 | 3960005 |
| mul | float64 | 7920000 |
| mul_const | int32 | 3960001 |
| div_const | float64 | 3962200 |
| mod | int32 | 3962200 |
| cmp | int32 | 2201 |
| logical | int32 | 1 |
| unary | ptr64 | 7 |
| unary | unknown | 5 |
| if | int1 | 2201 |
| loop_for | int32 | 11890200 |
| call | unknown | 4416 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 3964003 | 1 | 7927602 | 6 |
| add | 3962200 | 0 | 7920000 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 7920000 | 0 |
| mul_const | 3960000 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3962200 | 0 | 0 | 0 |
| mod | 3960000 | 2200 | 0 | 0 |
| cmp | 0 | 2200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 2200 | 0 | 1 |
| loop_for | 3964000 | 2200 | 7924000 | 0 |
| call | 0 | 4404 | 0 | 12 |
