# Static Operation Report: deriche

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 696868348 |
| add | 530841610 |
| sub | 12004 |
| mul | 99532807 |
| mul_const | 597196808 |
| div | 1 |
| div_const | 33177600 |
| mod | 66355200 |
| cmp | 33177601 |
| logical | 1 |
| bitwise | 0 |
| unary | 24 |
| if | 33177601 |
| loop_for | 265475520 |
| call | 66355225 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 696813613 |
| assign | int32 | 54730 |
| assign | ptr64 | 5 |
| add | float32 | 464486402 |
| add | int32 | 66355208 |
| sub | float32 | 4 |
| sub | int32 | 12000 |
| mul | float32 | 99532807 |
| mul_const | float32 | 497664004 |
| mul_const | int32 | 99532804 |
| div | float32 | 1 |
| div_const | float32 | 33177600 |
| mod | int32 | 66355200 |
| cmp | int32 | 33177601 |
| logical | int32 | 1 |
| unary | float32 | 10 |
| unary | ptr64 | 8 |
| unary | unknown | 6 |
| if | int1 | 33177601 |
| loop_for | int32 | 265475520 |
| call | unknown | 66355225 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_deriche | main |
|---|---:|---:|---:|---:|
| assign | 33185282 | 7681 | 663675379 | 6 |
| add | 33177600 | 33177600 | 464486402 | 8 |
| sub | 0 | 0 | 12004 | 0 |
| mul | 0 | 0 | 99532807 | 0 |
| mul_const | 66355200 | 33177600 | 497664004 | 4 |
| div | 0 | 0 | 1 | 0 |
| div_const | 33177600 | 0 | 0 | 0 |
| mod | 33177600 | 33177600 | 0 | 0 |
| cmp | 0 | 33177600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 10 | 13 |
| if | 0 | 33177600 | 0 | 1 |
| loop_for | 33185280 | 33185280 | 199104960 | 0 |
| call | 0 | 66355204 | 9 | 12 |
