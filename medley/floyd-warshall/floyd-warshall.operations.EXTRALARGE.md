# Static Operation Report: floyd-warshall

Generated: 2026-04-21T09:42:37
Dataset mode: EXTRALARGE
Functions analyzed: 4

## File Totals

| Operation | Count |
|---|---:|
| assign | 175710096805 |
| add | 351388800002 |
| sub | 0 |
| mul | 31360000 |
| mul_const | 31360001 |
| div | 0 |
| div_const | 0 |
| mod | 156800000 |
| cmp | 175741440001 |
| logical | 62720001 |
| bitwise | 0 |
| unary | 5 |
| if | 175678720001 |
| loop_for | 175710096800 |
| call | 62720010 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | int32 | 175710096804 |
| assign | ptr64 | 1 |
| add | int32 | 351388800002 |
| mul | int32 | 31360000 |
| mul_const | int32 | 31360001 |
| mod | int32 | 156800000 |
| cmp | int32 | 175741440001 |
| logical | int32 | 62720001 |
| unary | ptr64 | 3 |
| unary | unknown | 2 |
| if | int1 | 175678720001 |
| loop_for | int32 | 175710096800 |
| call | unknown | 62720010 |

## Function Operation Matrices

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 62725601 | 5601 | 175647365601 | 2 |
| add | 125440000 | 31360000 | 351232000000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 31360000 | 0 | 0 | 0 |
| mul_const | 0 | 31360000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 125440000 | 31360000 | 0 | 0 |
| cmp | 94080000 | 31360000 | 175616000000 | 1 |
| logical | 62720000 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 31360000 | 31360000 | 175616000000 | 1 |
| loop_for | 31365600 | 31365600 | 175647365600 | 0 |
| call | 0 | 62720004 | 0 | 6 |
