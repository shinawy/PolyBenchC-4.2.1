# Static Operation Report: gesummv

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 31376811 |
| add | 31362807 |
| sub | 0 |
| mul | 31365600 |
| mul_const | 2 |
| div | 0 |
| div_const | 15682800 |
| mod | 15685600 |
| cmp | 2801 |
| logical | 1 |
| bitwise | 0 |
| unary | 19 |
| if | 2801 |
| loop_for | 15688400 |
| call | 5618 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 31371200 |
| assign | int32 | 5604 |
| assign | ptr64 | 7 |
| add | float64 | 15682800 |
| add | int32 | 15680007 |
| mul | float64 | 15685600 |
| mul | int32 | 15680000 |
| mul_const | int32 | 2 |
| div_const | float64 | 15682800 |
| mod | int32 | 15685600 |
| cmp | int32 | 2801 |
| logical | int32 | 1 |
| unary | float64 | 2 |
| unary | ptr64 | 11 |
| unary | unknown | 6 |
| if | int1 | 2801 |
| loop_for | int32 | 15688400 |
| call | unknown | 5618 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 15685603 | 1 | 15691201 | 6 |
| add | 15680000 | 0 | 15682800 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15680000 | 0 | 15685600 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15682800 | 0 | 0 | 0 |
| mod | 15682800 | 2800 | 0 | 0 |
| cmp | 0 | 2800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 2800 | 0 | 1 |
| loop_for | 7842800 | 2800 | 7842800 | 0 |
| call | 0 | 5604 | 0 | 14 |
