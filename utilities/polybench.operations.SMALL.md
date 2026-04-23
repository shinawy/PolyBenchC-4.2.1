# Static Operation Report: polybench

Generated: 2026-04-21T09:42:50
Dataset mode: SMALL
Functions analyzed: 9

## File Totals

| Operation | Count |
|---|---:|
| assign | 13 |
| add | 2 |
| sub | 1 |
| mul | 1 |
| mul_const | 1 |
| div | 1 |
| div_const | 0 |
| mod | 0 |
| cmp | 0 |
| logical | 1 |
| bitwise | 0 |
| unary | 4 |
| if | 1 |
| loop_for | 0 |
| call | 12 |

## Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float64 | 1 |
| assign | int32 | 6 |
| assign | ptr64 | 3 |
| assign | unknown | 3 |
| add | int32 | 1 |
| add | unknown | 1 |
| sub | unknown | 1 |
| mul | int32 | 1 |
| mul_const | int32 | 1 |
| div | int32 | 1 |
| logical | ptr64 | 1 |
| unary | ptr64 | 2 |
| unary | unknown | 2 |
| if | int1 | 1 |
| call | unknown | 12 |

## Function Operation Matrices

### Function Table 1

| Operation | rtclock | polybench_flush_cache | polybench_prepare_instruments | polybench_timer_start | polybench_timer_stop | polybench_timer_print |
|---|---:|---:|---:|---:|---:|---:|
| assign | 0 | 4 | 0 | 1 | 1 | 0 |
| add | 0 | 0 | 0 | 0 | 0 | 0 |
| sub | 0 | 0 | 0 | 0 | 0 | 1 |
| mul | 0 | 0 | 0 | 0 | 0 | 0 |
| mul_const | 0 | 1 | 0 | 0 | 0 | 0 |
| div | 0 | 1 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 2 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 0 | 0 | 0 | 0 | 0 | 0 |
| call | 0 | 2 | 1 | 2 | 1 | 1 |

### Function Table 2

| Operation | xmalloc | polybench_free_data | polybench_alloc_data |
|---|---:|---:|---:|
| assign | 4 | 0 | 3 |
| add | 2 | 0 | 0 |
| sub | 0 | 0 | 0 |
| mul | 0 | 0 | 1 |
| mul_const | 0 | 0 | 0 |
| div | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 |
| mod | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 |
| logical | 1 | 0 | 0 |
| bitwise | 0 | 0 | 0 |
| unary | 2 | 0 | 0 |
| if | 1 | 0 | 0 |
| loop_for | 0 | 0 | 0 |
| call | 3 | 1 | 1 |

## Static Resolution Warnings

- polybench_flush_cache: unresolved loop bound
