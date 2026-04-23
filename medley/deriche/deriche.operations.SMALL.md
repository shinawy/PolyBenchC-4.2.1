# Static Operation Report: deriche

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 519772 |
| add | 393226 |
| sub | 324 |
| mul | 73735 |
| mul_const | 442376 |
| div | 1 |
| div_const | 24576 |
| mod | 49152 |
| cmp | 24577 |
| logical | 1 |
| bitwise | 0 |
| unary | 24 |
| if | 24577 |
| loop_for | 198016 |
| call | 49177 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 518349 |
| assign | int32 | 1418 |
| assign | ptr64 | 5 |
| add | float32 | 344066 |
| add | int32 | 49160 |
| sub | float32 | 4 |
| sub | int32 | 320 |
| mul | float32 | 73735 |
| mul_const | float32 | 368644 |
| mul_const | int32 | 73732 |
| div | float32 | 1 |
| div_const | float32 | 24576 |
| mod | int32 | 49152 |
| cmp | int32 | 24577 |
| logical | int32 | 1 |
| unary | float32 | 10 |
| unary | ptr64 | 8 |
| unary | unknown | 6 |
| if | int1 | 24577 |
| loop_for | int32 | 198016 |
| call | unknown | 49177 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_deriche | main |
|---|---:|---:|---:|---:|
| assign | 24770 | 193 | 494803 | 6 |
| add | 24576 | 24576 | 344066 | 8 |
| sub | 0 | 0 | 324 | 0 |
| mul | 0 | 0 | 73735 | 0 |
| mul_const | 49152 | 24576 | 368644 | 4 |
| div | 0 | 0 | 1 | 0 |
| div_const | 24576 | 0 | 0 | 0 |
| mod | 24576 | 24576 | 0 | 0 |
| cmp | 0 | 24576 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 10 | 13 |
| if | 0 | 24576 | 0 | 1 |
| loop_for | 24768 | 24768 | 148480 | 0 |
| call | 0 | 49156 | 9 | 12 |
