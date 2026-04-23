# Static Operation Report: 3mm

Generated: 2026-04-21T09:42:44
Dataset mode: MEDIUM
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 23187340 |
| add | 23084014 |
| sub | 0 |
| mul | 22962000 |
| mul_const | 199807 |
| div | 0 |
| div_const | 162000 |
| mod | 199800 |
| cmp | 37801 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 37801 |
| loop_for | 23113220 |
| call | 75622 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 23073900 |
| assign | int32 | 113433 |
| assign | ptr64 | 7 |
| add | float64 | 22800000 |
| add | int32 | 284014 |
| mul | float64 | 22800000 |
| mul | int32 | 162000 |
| mul_const | int32 | 199807 |
| div_const | float64 | 162000 |
| mod | int32 | 199800 |
| cmp | int32 | 37801 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 8 |
| if | int1 | 37801 |
| loop_for | int32 | 23113220 |
| call | unknown | 75622 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 162794 | 181 | 23024353 | 12 |
| add | 246200 | 37800 | 22800000 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 162000 | 0 | 22800000 | 0 |
| mul_const | 162000 | 37800 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 162000 | 0 | 0 | 0 |
| mod | 162000 | 37800 | 0 | 0 |
| cmp | 0 | 37800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 37800 | 0 | 1 |
| loop_for | 162790 | 37980 | 22912450 | 0 |
| call | 0 | 75604 | 0 | 18 |
