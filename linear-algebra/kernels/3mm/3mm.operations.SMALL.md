# Static Operation Report: 3mm

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 572020 |
| add | 566414 |
| sub | 0 |
| mul | 555000 |
| mul_const | 17807 |
| div | 0 |
| div_const | 15000 |
| mod | 17800 |
| cmp | 2801 |
| logical | 1 |
| bitwise | 0 |
| unary | 20 |
| if | 2801 |
| loop_for | 566500 |
| call | 5622 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 563300 |
| assign | int32 | 8713 |
| assign | ptr64 | 7 |
| add | float64 | 540000 |
| add | int32 | 26414 |
| mul | float64 | 540000 |
| mul | int32 | 15000 |
| mul_const | int32 | 17807 |
| div_const | float64 | 15000 |
| mod | int32 | 17800 |
| cmp | int32 | 2801 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 8 |
| if | int1 | 2801 |
| loop_for | int32 | 566500 |
| call | unknown | 5622 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 15234 | 41 | 556733 | 12 |
| add | 23600 | 2800 | 540000 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15000 | 0 | 540000 | 0 |
| mul_const | 15000 | 2800 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15000 | 0 | 0 | 0 |
| mod | 15000 | 2800 | 0 | 0 |
| cmp | 0 | 2800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 2800 | 0 | 1 |
| loop_for | 15230 | 2840 | 548430 | 0 |
| call | 0 | 5604 | 0 | 18 |
