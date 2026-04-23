# Static Operation Report: mvt

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 48028011 |
| add | 32012006 |
| sub | 0 |
| mul | 48000000 |
| mul_const | 1 |
| div | 0 |
| div_const | 16016000 |
| mod | 16024000 |
| cmp | 8001 |
| logical | 1 |
| bitwise | 0 |
| unary | 18 |
| if | 8001 |
| loop_for | 48020000 |
| call | 16020 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 48016000 |
| assign | int32 | 12006 |
| assign | ptr64 | 5 |
| add | float64 | 32000000 |
| add | int32 | 12006 |
| mul | float64 | 32000000 |
| mul | int32 | 16000000 |
| mul_const | int32 | 1 |
| div_const | float64 | 16016000 |
| mod | int32 | 16024000 |
| cmp | int32 | 8001 |
| logical | int32 | 1 |
| unary | ptr64 | 12 |
| unary | unknown | 6 |
| if | int1 | 8001 |
| loop_for | int32 | 48020000 |
| call | unknown | 16020 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 16020001 | 2 | 32008002 | 6 |
| add | 12000 | 0 | 32000000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16000000 | 0 | 32000000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16016000 | 0 | 0 | 0 |
| mod | 16016000 | 8000 | 0 | 0 |
| cmp | 0 | 8000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 8000 | 0 | 1 |
| loop_for | 16004000 | 8000 | 32008000 | 0 |
| call | 0 | 16006 | 0 | 14 |
