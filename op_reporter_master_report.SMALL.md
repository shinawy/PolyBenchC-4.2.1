# Master Static Operation Report

Generated: 2026-04-21T09:42:50
Root directory: /Users/elshenma/Dropbox/SyncFolder/Benchmarks/PolyBenchC-4.2.1
Dataset mode: SMALL
C files analyzed: 41
Functions analyzed: 140

## Global Totals

| Operation | Count |
|---|---:|
| assign | 17133239 |
| add | 37843675 |
| sub | 12962691 |
| mul | 8109282 |
| mul_const | 6579454 |
| div | 551522 |
| div_const | 836045 |
| mod | 527105 |
| cmp | 6122083 |
| logical | 64832 |
| bitwise | 4 |
| unary | 5809278 |
| if | 6057283 |
| loop_for | 16525277 |
| call | 394297 |

## Global Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 518349 |
| assign | float64 | 5258445 |
| assign | int32 | 6129119 |
| assign | ptr64 | 5227323 |
| assign | unknown | 3 |
| add | float32 | 344066 |
| add | float64 | 13152791 |
| add | int32 | 19162817 |
| add | ptr64 | 5184000 |
| add | unknown | 1 |
| sub | float32 | 4 |
| sub | float64 | 3286159 |
| sub | int32 | 9676527 |
| sub | unknown | 1 |
| mul | float32 | 73735 |
| mul | float64 | 7844755 |
| mul | int32 | 190792 |
| mul_const | float32 | 368644 |
| mul_const | float64 | 5894723 |
| mul_const | int32 | 316087 |
| div | float32 | 1 |
| div | float64 | 551520 |
| div | int32 | 1 |
| div_const | float32 | 24576 |
| div_const | float64 | 811468 |
| div_const | int32 | 1 |
| mod | int32 | 527105 |
| cmp | float64 | 80 |
| cmp | int32 | 6122003 |
| logical | int32 | 64831 |
| logical | ptr64 | 1 |
| bitwise | int32 | 4 |
| unary | float32 | 10 |
| unary | float64 | 538380 |
| unary | int32 | 121 |
| unary | ptr64 | 5270632 |
| unary | unknown | 135 |
| if | int1 | 6057283 |
| loop_for | int32 | 16525277 |
| call | unknown | 394297 |

## Per-File Kernel Operation Matrices

### File Table 1

| Operation | correlation | covariance | case01 | case02 | case03 | case04 |
|---|---:|---:|---:|---:|---:|---:|
| assign | 32904 | 16423 | 1 | 2 | 3 | 6 |
| add | 16079 | 8000 | 1 | 1 | 0 | 4 |
| sub | 24082 | 8000 | 0 | 0 | 2 | 0 |
| mul | 16000 | 0 | 0 | 1 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 | 0 | 0 |
| div | 8160 | 80 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 80 | 0 | 0 | 0 | 1 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 80 | 0 | 0 | 0 | 1 | 0 |
| loop_for | 24339 | 16260 | 0 | 0 | 0 | 4 |
| call | 8080 | 0 | 0 | 0 | 0 | 0 |

### File Table 2

| Operation | case05 | case06 | case07 | case08 | case09 | case10 |
|---|---:|---:|---:|---:|---:|---:|
| assign | 10 | 2 | 3 | 5 | 7 | 7 |
| add | 6 | 0 | 2 | 3 | 4 | 5 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 6 | 0 | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 0 | 0 | 5 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 1 | 0 | 0 | 0 |
| mod | 0 | 0 | 1 | 0 | 0 | 0 |
| cmp | 0 | 2 | 0 | 0 | 0 | 0 |
| logical | 0 | 1 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 4 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 1 | 0 | 0 | 0 |
| if | 0 | 1 | 0 | 0 | 0 | 0 |
| loop_for | 8 | 0 | 0 | 3 | 4 | 5 |
| call | 0 | 0 | 0 | 3 | 0 | 0 |

### File Table 3

| Operation | gemm | gemver | gesummv | symm | syr2k | syrk |
|---|---:|---:|---:|---:|---:|---:|
| assign | 345121 | 43684 | 16561 | 14461 | 4961 | 4961 |
| add | 336000 | 57720 | 16290 | 9600 | 0 | 0 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 676200 | 86400 | 16380 | 14400 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 4800 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 345060 | 43680 | 8190 | 4860 | 4880 | 4880 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 4

| Operation | trmm | 2mm | 3mm | atax | bicg | doitgen |
|---|---:|---:|---:|---:|---:|---:|
| assign | 9661 | 310482 | 556733 | 29242 | 29134 | 496026 |
| add | 4800 | 300000 | 540000 | 28768 | 28768 | 450000 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 4800 | 443200 | 540000 | 28768 | 28768 | 450000 |
| mul_const | 0 | 0 | 0 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 4860 | 305280 | 548430 | 29008 | 14624 | 480525 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 5

| Operation | mvt | cholesky | durbin | gramschmidt | lu | ludcmp |
|---|---:|---:|---:|---:|---:|---:|
| assign | 29042 | 361 | 837 | 10001 | 241 | 963 |
| add | 28800 | 0 | 119 | 4880 | 0 | 120 |
| sub | 0 | 0 | 119 | 0 | 0 | 1 |
| mul | 28800 | 0 | 119 | 4800 | 0 | 0 |
| mul_const | 0 | 0 | 119 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 4800 | 0 | 120 |
| div_const | 0 | 0 | 119 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 121 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 29040 | 120 | 119 | 9680 | 120 | 360 |
| call | 0 | 120 | 0 | 80 | 0 | 0 |

### File Table 6

| Operation | trisolv | deriche | floyd-warshall | nussinov | adi | fdtd-2d |
|---|---:|---:|---:|---:|---:|---:|
| assign | 361 | 494803 | 5864581 | 181 | 835294 | 575321 |
| add | 0 | 344066 | 11664000 | 180 | 1883842 | 559320 |
| sub | 0 | 324 | 0 | 1 | 1902480 | 1885720 |
| mul | 0 | 73735 | 0 | 0 | 269120 | 0 |
| mul_const | 0 | 368644 | 0 | 0 | 1883844 | 564840 |
| div | 120 | 1 | 0 | 0 | 538240 | 0 |
| div_const | 0 | 0 | 0 | 0 | 7 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 5832000 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 10 | 0 | 0 | 538242 | 0 |
| if | 0 | 0 | 5832000 | 0 | 0 | 0 |
| loop_for | 120 | 148480 | 5864580 | 180 | 542920 | 575200 |
| call | 0 | 9 | 0 | 0 | 0 | 0 |

### File Table 7

| Operation | heat-3d | jacobi-1d | jacobi-2d | seidel-2d | polybench |
|---|---:|---:|---:|---:|---:|
| assign | 494001 | 9521 | 626641 | 561721 | 4 |
| add | 4199040 | 28320 | 3717120 | 7797440 | 2 |
| sub | 3320720 | 18960 | 1872720 | 3908241 | 0 |
| mul | 0 | 0 | 0 | 0 | 0 |
| mul_const | 2799360 | 9440 | 619520 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 556960 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 2 |
| if | 0 | 0 | 0 | 0 | 1 |
| loop_for | 493960 | 9480 | 626600 | 561720 | 0 |
| call | 0 | 0 | 0 | 0 | 3 |

## Function Matrices By File

### Functions for correlation

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 8102 | 81 | 32904 | 6 |
| add | 8000 | 6400 | 16079 | 6 |
| sub | 0 | 0 | 24082 | 0 |
| mul | 8000 | 0 | 16000 | 0 |
| mul_const | 0 | 6400 | 0 | 2 |
| div | 0 | 0 | 8160 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 80 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 6400 | 80 | 1 |
| loop_for | 8100 | 6480 | 24339 | 0 |
| call | 0 | 12804 | 8080 | 12 |

### Functions for covariance

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 8102 | 81 | 16423 | 5 |
| add | 0 | 6400 | 8000 | 5 |
| sub | 0 | 0 | 8000 | 0 |
| mul | 8000 | 0 | 0 | 0 |
| mul_const | 0 | 6400 | 0 | 2 |
| div | 0 | 0 | 80 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 6400 | 0 | 1 |
| loop_for | 8100 | 6480 | 16260 | 0 |
| call | 0 | 12804 | 0 | 10 |

### Functions for case01

| Operation | case01_kernel |
|---|---:|
| assign | 1 |
| add | 1 |
| sub | 0 |
| mul | 0 |
| mul_const | 0 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 0 |
| logical | 0 |
| bitwise | 0 |
| unary | 0 |
| if | 0 |
| loop_for | 0 |
| call | 0 |

### Functions for case02

| Operation | case02_kernel |
|---|---:|
| assign | 2 |
| add | 1 |
| sub | 0 |
| mul | 1 |
| mul_const | 1 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 0 |
| logical | 0 |
| bitwise | 0 |
| unary | 0 |
| if | 0 |
| loop_for | 0 |
| call | 0 |

### Functions for case03

| Operation | case03_kernel |
|---|---:|
| assign | 3 |
| add | 0 |
| sub | 2 |
| mul | 0 |
| mul_const | 0 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 1 |
| logical | 0 |
| bitwise | 0 |
| unary | 0 |
| if | 1 |
| loop_for | 0 |
| call | 0 |

### Functions for case04

| Operation | case04_kernel |
|---|---:|
| assign | 6 |
| add | 4 |
| sub | 0 |
| mul | 0 |
| mul_const | 0 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 0 |
| logical | 0 |
| bitwise | 0 |
| unary | 0 |
| if | 0 |
| loop_for | 4 |
| call | 0 |

### Functions for case05

| Operation | case05_kernel |
|---|---:|
| assign | 10 |
| add | 6 |
| sub | 0 |
| mul | 6 |
| mul_const | 0 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 0 |
| logical | 0 |
| bitwise | 0 |
| unary | 0 |
| if | 0 |
| loop_for | 8 |
| call | 0 |

### Functions for case06

| Operation | case06_kernel |
|---|---:|
| assign | 2 |
| add | 0 |
| sub | 0 |
| mul | 0 |
| mul_const | 0 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 2 |
| logical | 1 |
| bitwise | 4 |
| unary | 0 |
| if | 1 |
| loop_for | 0 |
| call | 0 |

### Functions for case07

| Operation | case07_kernel |
|---|---:|
| assign | 3 |
| add | 2 |
| sub | 0 |
| mul | 0 |
| mul_const | 0 |
| div | 0 |
| div_const | 1 |
| mod | 1 |
| cmp | 0 |
| logical | 0 |
| bitwise | 0 |
| unary | 1 |
| if | 0 |
| loop_for | 0 |
| call | 0 |

### Functions for case08

| Operation | case08_helper | case08_kernel |
|---|---:|---:|
| assign | 0 | 5 |
| add | 1 | 3 |
| sub | 0 | 0 |
| mul | 0 | 0 |
| mul_const | 0 | 0 |
| div | 0 | 0 |
| div_const | 0 | 0 |
| mod | 0 | 0 |
| cmp | 0 | 0 |
| logical | 0 | 0 |
| bitwise | 0 | 0 |
| unary | 0 | 0 |
| if | 0 | 0 |
| loop_for | 0 | 3 |
| call | 0 | 3 |

### Functions for case09

| Operation | case09_kernel |
|---|---:|
| assign | 7 |
| add | 4 |
| sub | 0 |
| mul | 0 |
| mul_const | 0 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 0 |
| logical | 0 |
| bitwise | 0 |
| unary | 0 |
| if | 0 |
| loop_for | 4 |
| call | 0 |

### Functions for case10

| Operation | case10_kernel |
|---|---:|
| assign | 7 |
| add | 5 |
| sub | 0 |
| mul | 0 |
| mul_const | 5 |
| div | 0 |
| div_const | 0 |
| mod | 0 |
| cmp | 0 |
| logical | 0 |
| bitwise | 0 |
| unary | 0 |
| if | 0 |
| loop_for | 5 |
| call | 0 |

### Functions for gemm

| Operation | init_array | print_array | kernel_gemm | main |
|---|---:|---:|---:|---:|
| assign | 14805 | 61 | 345121 | 6 |
| add | 14600 | 4200 | 336000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14600 | 0 | 676200 | 0 |
| mul_const | 0 | 4200 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14600 | 0 | 0 | 0 |
| mod | 14600 | 4200 | 0 | 0 |
| cmp | 0 | 4200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 4200 | 0 | 1 |
| loop_for | 14800 | 4260 | 345060 | 0 |
| call | 0 | 8404 | 0 | 10 |

### Functions for gemver

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 15484 | 1 | 43684 | 10 |
| add | 600 | 0 | 57720 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14400 | 0 | 86400 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15600 | 0 | 0 | 0 |
| mod | 14400 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 14520 | 120 | 43680 | 0 |
| call | 0 | 244 | 0 | 22 |

### Functions for gesummv

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 16383 | 1 | 16561 | 6 |
| add | 16200 | 0 | 16290 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16200 | 0 | 16380 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16290 | 0 | 0 | 0 |
| mod | 16290 | 90 | 0 | 0 |
| cmp | 0 | 90 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 90 | 0 | 1 |
| loop_for | 8190 | 90 | 8190 | 0 |
| call | 0 | 184 | 0 | 14 |

### Functions for symm

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 9784 | 61 | 14461 | 5 |
| add | 9660 | 4800 | 9600 | 6 |
| sub | 4800 | 0 | 0 | 0 |
| mul | 0 | 0 | 14400 | 0 |
| mul_const | 0 | 4800 | 4800 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 9600 | 0 | 0 | 0 |
| mod | 9600 | 4800 | 0 | 0 |
| cmp | 0 | 4800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 4800 | 0 | 1 |
| loop_for | 4920 | 4860 | 4860 | 0 |
| call | 0 | 9604 | 0 | 10 |

### Functions for syr2k

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 16164 | 81 | 4961 | 5 |
| add | 16000 | 6400 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16000 | 0 | 0 | 0 |
| mul_const | 0 | 6400 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16000 | 0 | 0 | 0 |
| mod | 16000 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 6400 | 0 | 1 |
| loop_for | 11360 | 6480 | 4880 | 0 |
| call | 0 | 12804 | 0 | 10 |

### Functions for syrk

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 11364 | 81 | 4961 | 4 |
| add | 11200 | 6400 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 11200 | 0 | 0 | 0 |
| mul_const | 0 | 6400 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 11200 | 0 | 0 | 0 |
| mod | 11200 | 6400 | 0 | 0 |
| cmp | 0 | 6400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 6400 | 0 | 1 |
| loop_for | 11360 | 6480 | 4880 | 0 |
| call | 0 | 12804 | 0 | 8 |

### Functions for trmm

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 4982 | 61 | 9661 | 4 |
| add | 4800 | 4800 | 4800 | 4 |
| sub | 4800 | 0 | 0 | 0 |
| mul | 0 | 0 | 4800 | 0 |
| mul_const | 0 | 4800 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4800 | 0 | 0 | 0 |
| mod | 4800 | 4800 | 0 | 0 |
| cmp | 0 | 4800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 4800 | 0 | 1 |
| loop_for | 4860 | 4860 | 4860 | 0 |
| call | 0 | 9604 | 0 | 8 |

### Functions for 2mm

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 13706 | 41 | 310482 | 9 |
| add | 17500 | 3200 | 300000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 13500 | 0 | 443200 | 0 |
| mul_const | 0 | 3200 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 13500 | 0 | 0 | 0 |
| mod | 13500 | 3200 | 0 | 0 |
| cmp | 0 | 3200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 3200 | 0 | 1 |
| loop_for | 13700 | 3240 | 305280 | 0 |
| call | 0 | 6404 | 0 | 14 |

### Functions for 3mm

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

### Functions for atax

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 14627 | 1 | 29242 | 6 |
| add | 14508 | 0 | 28768 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 28768 | 0 |
| mul_const | 14384 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14508 | 0 | 0 | 0 |
| mod | 14384 | 124 | 0 | 0 |
| cmp | 0 | 124 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 124 | 0 | 1 |
| loop_for | 14624 | 124 | 29008 | 0 |
| call | 0 | 252 | 0 | 12 |

### Functions for bicg

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 14750 | 2 | 29134 | 7 |
| add | 14384 | 0 | 28768 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14384 | 0 | 28768 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14624 | 0 | 0 | 0 |
| mod | 14624 | 240 | 0 | 0 |
| cmp | 0 | 240 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 240 | 0 | 1 |
| loop_for | 14624 | 240 | 14624 | 0 |
| call | 0 | 486 | 0 | 14 |

### Functions for doitgen

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 16457 | 526 | 496026 | 6 |
| add | 15000 | 30000 | 450000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15900 | 0 | 450000 | 0 |
| mul_const | 0 | 45000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15900 | 0 | 0 | 0 |
| mod | 15900 | 15000 | 0 | 0 |
| cmp | 0 | 15000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 15000 | 0 | 1 |
| loop_for | 16455 | 15525 | 480525 | 0 |
| call | 0 | 30004 | 0 | 10 |

### Functions for mvt

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 15001 | 2 | 29042 | 6 |
| add | 360 | 0 | 28800 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14400 | 0 | 28800 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14880 | 0 | 0 | 0 |
| mod | 14880 | 240 | 0 | 0 |
| cmp | 0 | 240 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 240 | 0 | 1 |
| loop_for | 14520 | 240 | 29040 | 0 |
| call | 0 | 486 | 0 | 14 |

### Functions for cholesky

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 1771925 | 121 | 361 | 2 |
| add | 1728122 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1728000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1756801 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 1771680 | 120 | 120 | 0 |
| call | 2 | 4 | 120 | 6 |

### Functions for durbin

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 121 | 1 | 837 | 3 |
| add | 120 | 0 | 119 | 2 |
| sub | 120 | 0 | 119 | 0 |
| mul | 0 | 0 | 119 | 0 |
| mul_const | 0 | 0 | 119 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 119 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 121 | 7 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 120 | 120 | 119 | 0 |
| call | 0 | 244 | 0 | 8 |

### Functions for gramschmidt

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 16142 | 142 | 10001 | 5 |
| add | 4800 | 11200 | 4880 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4800 | 0 | 4800 | 0 |
| mul_const | 4800 | 11200 | 0 | 3 |
| div | 0 | 0 | 4800 | 0 |
| div_const | 4800 | 0 | 0 | 0 |
| mod | 4800 | 11200 | 0 | 0 |
| cmp | 0 | 11200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 11200 | 0 | 1 |
| loop_for | 11340 | 11340 | 9680 | 0 |
| call | 0 | 22406 | 80 | 10 |

### Functions for lu

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 1771925 | 121 | 241 | 2 |
| add | 1728122 | 14400 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1728000 | 0 | 0 | 0 |
| mul_const | 1 | 14400 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 14400 | 0 | 0 |
| cmp | 0 | 14400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1756801 | 0 | 0 | 5 |
| if | 0 | 14400 | 0 | 1 |
| loop_for | 1771680 | 14520 | 120 | 0 |
| call | 2 | 28804 | 0 | 6 |

### Functions for ludcmp

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 1772287 | 1 | 963 | 5 |
| add | 1728362 | 0 | 120 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 1728000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 120 | 0 |
| div_const | 240 | 0 | 0 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1756801 | 0 | 0 | 14 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 1771800 | 120 | 360 | 0 |
| call | 2 | 244 | 0 | 12 |

### Functions for trisolv

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 361 | 1 | 361 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 120 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 120 | 0 | 0 | 11 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 120 | 120 | 120 | 0 |
| call | 0 | 244 | 0 | 10 |

### Functions for deriche

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

### Functions for floyd-warshall

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 64981 | 181 | 5864581 | 2 |
| add | 129600 | 32400 | 11664000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 32400 | 0 | 0 | 0 |
| mul_const | 0 | 32400 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 129600 | 32400 | 0 | 0 |
| cmp | 97200 | 32400 | 5832000 | 1 |
| logical | 64800 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 32400 | 32400 | 5832000 | 1 |
| loop_for | 32580 | 32580 | 5864580 | 0 |
| call | 0 | 64804 | 0 | 6 |

### Functions for nussinov

| Operation | init_array | print_array | kernel_nussinov | main |
|---|---:|---:|---:|---:|
| assign | 32762 | 182 | 181 | 3 |
| add | 180 | 0 | 180 | 3 |
| sub | 0 | 0 | 1 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 180 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 32760 | 180 | 180 | 0 |
| call | 0 | 4 | 0 | 8 |

### Functions for adi

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 3661 | 61 | 835294 | 6 |
| add | 3600 | 3600 | 1883842 | 8 |
| sub | 3600 | 0 | 1902480 | 0 |
| mul | 0 | 0 | 269120 | 0 |
| mul_const | 0 | 3600 | 1883844 | 4 |
| div | 0 | 0 | 538240 | 0 |
| div_const | 3600 | 0 | 7 | 0 |
| mod | 0 | 3600 | 0 | 0 |
| cmp | 0 | 3600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 538242 | 11 |
| if | 0 | 3600 | 0 | 1 |
| loop_for | 3660 | 3660 | 542920 | 0 |
| call | 0 | 7204 | 0 | 12 |

### Functions for fdtd-2d

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 14502 | 183 | 575321 | 7 |
| add | 14400 | 14400 | 559320 | 7 |
| sub | 0 | 0 | 1885720 | 0 |
| mul | 14400 | 0 | 0 | 0 |
| mul_const | 0 | 14400 | 564840 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14400 | 0 | 0 | 0 |
| mod | 0 | 14400 | 0 | 0 |
| cmp | 0 | 14400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 14400 | 0 | 1 |
| loop_for | 4900 | 14580 | 575200 | 0 |
| call | 0 | 28808 | 0 | 12 |

### Functions for heat-3d

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 16421 | 421 | 494001 | 4 |
| add | 16000 | 16000 | 4199040 | 6 |
| sub | 8000 | 0 | 3320720 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 8000 | 24000 | 2799360 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 8000 | 0 | 0 |
| cmp | 0 | 8000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 8000 | 0 | 1 |
| loop_for | 8420 | 8420 | 493960 | 0 |
| call | 0 | 16004 | 0 | 7 |

### Functions for jacobi-1d

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 241 | 1 | 9521 | 4 |
| add | 240 | 0 | 28320 | 2 |
| sub | 0 | 0 | 18960 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 9440 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 240 | 0 | 0 | 0 |
| mod | 0 | 120 | 0 | 0 |
| cmp | 0 | 120 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 120 | 0 | 1 |
| loop_for | 120 | 120 | 9480 | 0 |
| call | 0 | 244 | 0 | 8 |

### Functions for jacobi-2d

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 16291 | 91 | 626641 | 4 |
| add | 32400 | 8100 | 3717120 | 4 |
| sub | 0 | 0 | 1872720 | 0 |
| mul | 16200 | 0 | 0 | 0 |
| mul_const | 0 | 8100 | 619520 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16200 | 0 | 0 | 0 |
| mod | 0 | 8100 | 0 | 0 |
| cmp | 0 | 8100 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 8100 | 0 | 1 |
| loop_for | 8190 | 8190 | 626600 | 0 |
| call | 0 | 16204 | 0 | 8 |

### Functions for seidel-2d

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 14521 | 121 | 561721 | 3 |
| add | 28800 | 14400 | 7797440 | 2 |
| sub | 0 | 0 | 3908241 | 0 |
| mul | 14400 | 0 | 0 | 0 |
| mul_const | 0 | 14400 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14400 | 0 | 556960 | 0 |
| mod | 0 | 14400 | 0 | 0 |
| cmp | 0 | 14400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 14400 | 0 | 1 |
| loop_for | 14520 | 14520 | 561720 | 0 |
| call | 0 | 28804 | 0 | 6 |

### Functions for polybench

#### Function Table 1

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

#### Function Table 2

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

## Per-File Reports

- correlation: [datamining/correlation/correlation.operations.SMALL.md](datamining/correlation/correlation.operations.SMALL.md), [datamining/correlation/correlation.operations.SMALL.pdf](datamining/correlation/correlation.operations.SMALL.pdf)
- covariance: [datamining/covariance/covariance.operations.SMALL.md](datamining/covariance/covariance.operations.SMALL.md), [datamining/covariance/covariance.operations.SMALL.pdf](datamining/covariance/covariance.operations.SMALL.pdf)
- case01: [dummy_tests/case01/case01.operations.SMALL.md](dummy_tests/case01/case01.operations.SMALL.md), [dummy_tests/case01/case01.operations.SMALL.pdf](dummy_tests/case01/case01.operations.SMALL.pdf)
- case02: [dummy_tests/case02/case02.operations.SMALL.md](dummy_tests/case02/case02.operations.SMALL.md), [dummy_tests/case02/case02.operations.SMALL.pdf](dummy_tests/case02/case02.operations.SMALL.pdf)
- case03: [dummy_tests/case03/case03.operations.SMALL.md](dummy_tests/case03/case03.operations.SMALL.md), [dummy_tests/case03/case03.operations.SMALL.pdf](dummy_tests/case03/case03.operations.SMALL.pdf)
- case04: [dummy_tests/case04/case04.operations.SMALL.md](dummy_tests/case04/case04.operations.SMALL.md), [dummy_tests/case04/case04.operations.SMALL.pdf](dummy_tests/case04/case04.operations.SMALL.pdf)
- case05: [dummy_tests/case05/case05.operations.SMALL.md](dummy_tests/case05/case05.operations.SMALL.md), [dummy_tests/case05/case05.operations.SMALL.pdf](dummy_tests/case05/case05.operations.SMALL.pdf)
- case06: [dummy_tests/case06/case06.operations.SMALL.md](dummy_tests/case06/case06.operations.SMALL.md), [dummy_tests/case06/case06.operations.SMALL.pdf](dummy_tests/case06/case06.operations.SMALL.pdf)
- case07: [dummy_tests/case07/case07.operations.SMALL.md](dummy_tests/case07/case07.operations.SMALL.md), [dummy_tests/case07/case07.operations.SMALL.pdf](dummy_tests/case07/case07.operations.SMALL.pdf)
- case08: [dummy_tests/case08/case08.operations.SMALL.md](dummy_tests/case08/case08.operations.SMALL.md), [dummy_tests/case08/case08.operations.SMALL.pdf](dummy_tests/case08/case08.operations.SMALL.pdf)
- case09: [dummy_tests/case09/case09.operations.SMALL.md](dummy_tests/case09/case09.operations.SMALL.md), [dummy_tests/case09/case09.operations.SMALL.pdf](dummy_tests/case09/case09.operations.SMALL.pdf)
- case10: [dummy_tests/case10/case10.operations.SMALL.md](dummy_tests/case10/case10.operations.SMALL.md), [dummy_tests/case10/case10.operations.SMALL.pdf](dummy_tests/case10/case10.operations.SMALL.pdf)
- gemm: [linear-algebra/blas/gemm/gemm.operations.SMALL.md](linear-algebra/blas/gemm/gemm.operations.SMALL.md), [linear-algebra/blas/gemm/gemm.operations.SMALL.pdf](linear-algebra/blas/gemm/gemm.operations.SMALL.pdf)
- gemver: [linear-algebra/blas/gemver/gemver.operations.SMALL.md](linear-algebra/blas/gemver/gemver.operations.SMALL.md), [linear-algebra/blas/gemver/gemver.operations.SMALL.pdf](linear-algebra/blas/gemver/gemver.operations.SMALL.pdf)
- gesummv: [linear-algebra/blas/gesummv/gesummv.operations.SMALL.md](linear-algebra/blas/gesummv/gesummv.operations.SMALL.md), [linear-algebra/blas/gesummv/gesummv.operations.SMALL.pdf](linear-algebra/blas/gesummv/gesummv.operations.SMALL.pdf)
- symm: [linear-algebra/blas/symm/symm.operations.SMALL.md](linear-algebra/blas/symm/symm.operations.SMALL.md), [linear-algebra/blas/symm/symm.operations.SMALL.pdf](linear-algebra/blas/symm/symm.operations.SMALL.pdf)
- syr2k: [linear-algebra/blas/syr2k/syr2k.operations.SMALL.md](linear-algebra/blas/syr2k/syr2k.operations.SMALL.md), [linear-algebra/blas/syr2k/syr2k.operations.SMALL.pdf](linear-algebra/blas/syr2k/syr2k.operations.SMALL.pdf)
- syrk: [linear-algebra/blas/syrk/syrk.operations.SMALL.md](linear-algebra/blas/syrk/syrk.operations.SMALL.md), [linear-algebra/blas/syrk/syrk.operations.SMALL.pdf](linear-algebra/blas/syrk/syrk.operations.SMALL.pdf)
- trmm: [linear-algebra/blas/trmm/trmm.operations.SMALL.md](linear-algebra/blas/trmm/trmm.operations.SMALL.md), [linear-algebra/blas/trmm/trmm.operations.SMALL.pdf](linear-algebra/blas/trmm/trmm.operations.SMALL.pdf)
- 2mm: [linear-algebra/kernels/2mm/2mm.operations.SMALL.md](linear-algebra/kernels/2mm/2mm.operations.SMALL.md), [linear-algebra/kernels/2mm/2mm.operations.SMALL.pdf](linear-algebra/kernels/2mm/2mm.operations.SMALL.pdf)
- 3mm: [linear-algebra/kernels/3mm/3mm.operations.SMALL.md](linear-algebra/kernels/3mm/3mm.operations.SMALL.md), [linear-algebra/kernels/3mm/3mm.operations.SMALL.pdf](linear-algebra/kernels/3mm/3mm.operations.SMALL.pdf)
- atax: [linear-algebra/kernels/atax/atax.operations.SMALL.md](linear-algebra/kernels/atax/atax.operations.SMALL.md), [linear-algebra/kernels/atax/atax.operations.SMALL.pdf](linear-algebra/kernels/atax/atax.operations.SMALL.pdf)
- bicg: [linear-algebra/kernels/bicg/bicg.operations.SMALL.md](linear-algebra/kernels/bicg/bicg.operations.SMALL.md), [linear-algebra/kernels/bicg/bicg.operations.SMALL.pdf](linear-algebra/kernels/bicg/bicg.operations.SMALL.pdf)
- doitgen: [linear-algebra/kernels/doitgen/doitgen.operations.SMALL.md](linear-algebra/kernels/doitgen/doitgen.operations.SMALL.md), [linear-algebra/kernels/doitgen/doitgen.operations.SMALL.pdf](linear-algebra/kernels/doitgen/doitgen.operations.SMALL.pdf)
- mvt: [linear-algebra/kernels/mvt/mvt.operations.SMALL.md](linear-algebra/kernels/mvt/mvt.operations.SMALL.md), [linear-algebra/kernels/mvt/mvt.operations.SMALL.pdf](linear-algebra/kernels/mvt/mvt.operations.SMALL.pdf)
- cholesky: [linear-algebra/solvers/cholesky/cholesky.operations.SMALL.md](linear-algebra/solvers/cholesky/cholesky.operations.SMALL.md), [linear-algebra/solvers/cholesky/cholesky.operations.SMALL.pdf](linear-algebra/solvers/cholesky/cholesky.operations.SMALL.pdf)
- durbin: [linear-algebra/solvers/durbin/durbin.operations.SMALL.md](linear-algebra/solvers/durbin/durbin.operations.SMALL.md), [linear-algebra/solvers/durbin/durbin.operations.SMALL.pdf](linear-algebra/solvers/durbin/durbin.operations.SMALL.pdf)
- gramschmidt: [linear-algebra/solvers/gramschmidt/gramschmidt.operations.SMALL.md](linear-algebra/solvers/gramschmidt/gramschmidt.operations.SMALL.md), [linear-algebra/solvers/gramschmidt/gramschmidt.operations.SMALL.pdf](linear-algebra/solvers/gramschmidt/gramschmidt.operations.SMALL.pdf)
- lu: [linear-algebra/solvers/lu/lu.operations.SMALL.md](linear-algebra/solvers/lu/lu.operations.SMALL.md), [linear-algebra/solvers/lu/lu.operations.SMALL.pdf](linear-algebra/solvers/lu/lu.operations.SMALL.pdf)
- ludcmp: [linear-algebra/solvers/ludcmp/ludcmp.operations.SMALL.md](linear-algebra/solvers/ludcmp/ludcmp.operations.SMALL.md), [linear-algebra/solvers/ludcmp/ludcmp.operations.SMALL.pdf](linear-algebra/solvers/ludcmp/ludcmp.operations.SMALL.pdf)
- trisolv: [linear-algebra/solvers/trisolv/trisolv.operations.SMALL.md](linear-algebra/solvers/trisolv/trisolv.operations.SMALL.md), [linear-algebra/solvers/trisolv/trisolv.operations.SMALL.pdf](linear-algebra/solvers/trisolv/trisolv.operations.SMALL.pdf)
- deriche: [medley/deriche/deriche.operations.SMALL.md](medley/deriche/deriche.operations.SMALL.md), [medley/deriche/deriche.operations.SMALL.pdf](medley/deriche/deriche.operations.SMALL.pdf)
- floyd-warshall: [medley/floyd-warshall/floyd-warshall.operations.SMALL.md](medley/floyd-warshall/floyd-warshall.operations.SMALL.md), [medley/floyd-warshall/floyd-warshall.operations.SMALL.pdf](medley/floyd-warshall/floyd-warshall.operations.SMALL.pdf)
- nussinov: [medley/nussinov/nussinov.operations.SMALL.md](medley/nussinov/nussinov.operations.SMALL.md), [medley/nussinov/nussinov.operations.SMALL.pdf](medley/nussinov/nussinov.operations.SMALL.pdf)
- adi: [stencils/adi/adi.operations.SMALL.md](stencils/adi/adi.operations.SMALL.md), [stencils/adi/adi.operations.SMALL.pdf](stencils/adi/adi.operations.SMALL.pdf)
- fdtd-2d: [stencils/fdtd-2d/fdtd-2d.operations.SMALL.md](stencils/fdtd-2d/fdtd-2d.operations.SMALL.md), [stencils/fdtd-2d/fdtd-2d.operations.SMALL.pdf](stencils/fdtd-2d/fdtd-2d.operations.SMALL.pdf)
- heat-3d: [stencils/heat-3d/heat-3d.operations.SMALL.md](stencils/heat-3d/heat-3d.operations.SMALL.md), [stencils/heat-3d/heat-3d.operations.SMALL.pdf](stencils/heat-3d/heat-3d.operations.SMALL.pdf)
- jacobi-1d: [stencils/jacobi-1d/jacobi-1d.operations.SMALL.md](stencils/jacobi-1d/jacobi-1d.operations.SMALL.md), [stencils/jacobi-1d/jacobi-1d.operations.SMALL.pdf](stencils/jacobi-1d/jacobi-1d.operations.SMALL.pdf)
- jacobi-2d: [stencils/jacobi-2d/jacobi-2d.operations.SMALL.md](stencils/jacobi-2d/jacobi-2d.operations.SMALL.md), [stencils/jacobi-2d/jacobi-2d.operations.SMALL.pdf](stencils/jacobi-2d/jacobi-2d.operations.SMALL.pdf)
- seidel-2d: [stencils/seidel-2d/seidel-2d.operations.SMALL.md](stencils/seidel-2d/seidel-2d.operations.SMALL.md), [stencils/seidel-2d/seidel-2d.operations.SMALL.pdf](stencils/seidel-2d/seidel-2d.operations.SMALL.pdf)
- polybench: [utilities/polybench.operations.SMALL.md](utilities/polybench.operations.SMALL.md), [utilities/polybench.operations.SMALL.pdf](utilities/polybench.operations.SMALL.pdf)
