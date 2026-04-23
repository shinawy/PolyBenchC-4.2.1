# Static Operation Report: deriche

Generated: 2026-04-21T09:42:40
Dataset mode: LARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 185867276 |
| add | 141557770 |
| sub | 6260 |
| mul | 26542087 |
| mul_const | 159252488 |
| div | 1 |
| div_const | 8847360 |
| mod | 17694720 |
| cmp | 8847361 |
| logical | 1 |
| bitwise | 0 |
| unary | 24 |
| if | 8847361 |
| loop_for | 70807776 |
| call | 17694745 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 185838365 |
| assign | int32 | 28906 |
| assign | ptr64 | 5 |
| add | float32 | 123863042 |
| add | int32 | 17694728 |
| sub | float32 | 4 |
| sub | int32 | 6256 |
| mul | float32 | 26542087 |
| mul_const | float32 | 132710404 |
| mul_const | int32 | 26542084 |
| div | float32 | 1 |
| div_const | float32 | 8847360 |
| mod | int32 | 17694720 |
| cmp | int32 | 8847361 |
| logical | int32 | 1 |
| unary | float32 | 10 |
| unary | ptr64 | 8 |
| unary | unknown | 6 |
| if | int1 | 8847361 |
| loop_for | int32 | 70807776 |
| call | unknown | 17694745 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_deriche | main |
|---|---:|---:|---:|---:|
| assign | 8851458 | 4097 | 177011715 | 6 |
| add | 8847360 | 8847360 | 123863042 | 8 |
| sub | 0 | 0 | 6260 | 0 |
| mul | 0 | 0 | 26542087 | 0 |
| mul_const | 17694720 | 8847360 | 132710404 | 4 |
| div | 0 | 0 | 1 | 0 |
| div_const | 8847360 | 0 | 0 | 0 |
| mod | 8847360 | 8847360 | 0 | 0 |
| cmp | 0 | 8847360 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 10 | 13 |
| if | 0 | 8847360 | 0 | 1 |
| loop_for | 8851456 | 8851456 | 53104864 | 0 |
| call | 0 | 17694724 | 9 | 12 |
