# Static Operation Report: adi

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 23980006022 |
| add | 55896056010 |
| sub | 55908042000 |
| mul | 7984008000 |
| mul_const | 55892056008 |
| div | 15968016000 |
| div_const | 4000007 |
| mod | 4000000 |
| cmp | 4000001 |
| logical | 1 |
| bitwise | 0 |
| unary | 15968016013 |
| if | 4000001 |
| loop_for | 15980017000 |
| call | 8000016 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 23972008013 |
| assign | int32 | 7998005 |
| assign | ptr64 | 4 |
| add | float64 | 39920040002 |
| add | int32 | 15976016008 |
| sub | float64 | 15968016000 |
| sub | int32 | 39940026000 |
| mul | float64 | 7984008000 |
| mul_const | float64 | 55888056004 |
| mul_const | int32 | 4000004 |
| div | float64 | 15968016000 |
| div_const | float64 | 4000007 |
| mod | int32 | 4000000 |
| cmp | int32 | 4000001 |
| logical | int32 | 1 |
| unary | float64 | 15968016002 |
| unary | ptr64 | 6 |
| unary | unknown | 5 |
| if | int1 | 4000001 |
| loop_for | int32 | 15980017000 |
| call | unknown | 8000016 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 4002001 | 2001 | 23976002014 | 6 |
| add | 4000000 | 4000000 | 55888056002 | 8 |
| sub | 4000000 | 0 | 55904042000 | 0 |
| mul | 0 | 0 | 7984008000 | 0 |
| mul_const | 0 | 4000000 | 55888056004 | 4 |
| div | 0 | 0 | 15968016000 | 0 |
| div_const | 4000000 | 0 | 7 | 0 |
| mod | 0 | 4000000 | 0 | 0 |
| cmp | 0 | 4000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 15968016002 | 11 |
| if | 0 | 4000000 | 0 | 1 |
| loop_for | 4002000 | 4002000 | 15972013000 | 0 |
| call | 0 | 8000004 | 0 | 12 |
