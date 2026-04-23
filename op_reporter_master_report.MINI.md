# Master Static Operation Report

Generated: 2026-04-21T09:42:47
Root directory: /Users/elshenma/Dropbox/SyncFolder/Benchmarks/PolyBenchC-4.2.1
Dataset mode: MINI
C files analyzed: 41
Functions analyzed: 140

## Global Totals

| Operation | Count |
|---|---:|
| assign | 823958 |
| add | 1744673 |
| sub | 665451 |
| mul | 354272 |
| mul_const | 382470 |
| div | 27582 |
| div_const | 62617 |
| mod | 62859 |
| cmp | 250543 |
| logical | 7232 |
| bitwise | 4 |
| unary | 227998 |
| if | 243343 |
| loop_for | 752634 |
| call | 48835 |

## Global Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 86925 |
| assign | float64 | 286469 |
| assign | int32 | 253638 |
| assign | ptr64 | 196923 |
| assign | unknown | 3 |
| add | float32 | 57346 |
| add | float64 | 646209 |
| add | int32 | 849117 |
| add | ptr64 | 192000 |
| add | unknown | 1 |
| sub | float32 | 4 |
| sub | float64 | 170043 |
| sub | int32 | 495403 |
| sub | unknown | 1 |
| mul | float32 | 12295 |
| mul | float64 | 320519 |
| mul | int32 | 21458 |
| mul_const | float32 | 61444 |
| mul_const | float64 | 282343 |
| mul_const | int32 | 38683 |
| div | float32 | 1 |
| div | float64 | 27580 |
| div | int32 | 1 |
| div_const | float32 | 4096 |
| div_const | float64 | 58520 |
| div_const | int32 | 1 |
| mod | int32 | 62859 |
| cmp | float64 | 28 |
| cmp | int32 | 250515 |
| logical | int32 | 7231 |
| logical | ptr64 | 1 |
| bitwise | int32 | 4 |
| unary | float32 | 10 |
| unary | float64 | 25980 |
| unary | int32 | 41 |
| unary | ptr64 | 201832 |
| unary | unknown | 135 |
| if | int1 | 243343 |
| loop_for | int32 | 752634 |
| call | unknown | 48835 |

## Per-File Kernel Operation Matrices

### File Table 1

| Operation | correlation | covariance | case01 | case02 | case03 | case04 |
|---|---:|---:|---:|---:|---:|---:|
| assign | 3900 | 1939 | 1 | 2 | 3 | 6 |
| add | 1819 | 896 | 1 | 1 | 0 | 4 |
| sub | 2718 | 896 | 0 | 0 | 2 | 0 |
| mul | 1792 | 0 | 0 | 1 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 | 0 | 0 |
| div | 952 | 28 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 28 | 0 | 0 | 0 | 1 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 28 | 0 | 0 | 0 | 1 | 0 |
| loop_for | 2803 | 1880 | 0 | 0 | 0 | 4 |
| call | 924 | 0 | 0 | 0 | 0 | 0 |

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
| assign | 16141 | 4964 | 1921 | 1821 | 661 | 661 |
| add | 15000 | 6440 | 1830 | 1200 | 0 | 0 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 30500 | 9600 | 1860 | 1800 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 600 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 16120 | 4960 | 930 | 620 | 630 | 630 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 4

| Operation | trmm | 2mm | 3mm | atax | bicg | doitgen |
|---|---:|---:|---:|---:|---:|---:|
| assign | 1221 | 14626 | 23725 | 3350 | 3316 | 14571 |
| add | 600 | 13248 | 21600 | 3192 | 3192 | 11520 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 600 | 19968 | 21600 | 3192 | 3192 | 11520 |
| mul_const | 0 | 0 | 0 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 620 | 13952 | 22686 | 3272 | 1676 | 13530 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 5

| Operation | mvt | cholesky | durbin | gramschmidt | lu | ludcmp |
|---|---:|---:|---:|---:|---:|---:|
| assign | 3282 | 121 | 277 | 1351 | 81 | 323 |
| add | 3200 | 0 | 39 | 630 | 0 | 40 |
| sub | 0 | 0 | 39 | 0 | 0 | 1 |
| mul | 3200 | 0 | 39 | 600 | 0 | 0 |
| mul_const | 0 | 0 | 39 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 600 | 0 | 40 |
| div_const | 0 | 0 | 39 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 41 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 3280 | 40 | 39 | 1230 | 40 | 120 |
| call | 0 | 40 | 0 | 30 | 0 | 0 |

### File Table 6

| Operation | trisolv | deriche | floyd-warshall | nussinov | adi | fdtd-2d |
|---|---:|---:|---:|---:|---:|---:|
| assign | 121 | 83219 | 219661 | 61 | 43254 | 35861 |
| add | 0 | 57346 | 432000 | 60 | 90722 | 33060 |
| sub | 0 | 132 | 0 | 1 | 93640 | 113860 |
| mul | 0 | 12295 | 0 | 0 | 12960 | 0 |
| mul_const | 0 | 61444 | 0 | 0 | 90724 | 34020 |
| div | 40 | 1 | 0 | 0 | 25920 | 0 |
| div_const | 0 | 0 | 0 | 0 | 7 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 216000 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 10 | 0 | 0 | 25922 | 0 |
| if | 0 | 0 | 216000 | 0 | 0 | 0 |
| loop_for | 40 | 24960 | 219660 | 60 | 26660 | 35800 |
| call | 0 | 9 | 0 | 0 | 0 | 0 |

### File Table 7

| Operation | heat-3d | jacobi-1d | jacobi-2d | seidel-2d | polybench |
|---|---:|---:|---:|---:|---:|
| assign | 23401 | 1161 | 32521 | 29661 | 4 |
| add | 184320 | 3360 | 188160 | 404320 | 2 |
| sub | 149160 | 2280 | 96360 | 203721 | 0 |
| mul | 0 | 0 | 0 | 0 | 0 |
| mul_const | 122880 | 1120 | 31360 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 28880 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 2 |
| if | 0 | 0 | 0 | 0 | 1 |
| loop_for | 23380 | 1140 | 32500 | 29660 | 0 |
| call | 0 | 0 | 0 | 0 | 3 |

## Function Matrices By File

### Functions for correlation

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 930 | 29 | 3900 | 6 |
| add | 896 | 784 | 1819 | 6 |
| sub | 0 | 0 | 2718 | 0 |
| mul | 896 | 0 | 1792 | 0 |
| mul_const | 0 | 784 | 0 | 2 |
| div | 0 | 0 | 952 | 0 |
| div_const | 896 | 0 | 0 | 0 |
| mod | 0 | 784 | 0 | 0 |
| cmp | 0 | 784 | 28 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 784 | 28 | 1 |
| loop_for | 928 | 812 | 2803 | 0 |
| call | 0 | 1572 | 924 | 12 |

### Functions for covariance

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 930 | 29 | 1939 | 5 |
| add | 0 | 784 | 896 | 5 |
| sub | 0 | 0 | 896 | 0 |
| mul | 896 | 0 | 0 | 0 |
| mul_const | 0 | 784 | 0 | 2 |
| div | 0 | 0 | 28 | 0 |
| div_const | 896 | 0 | 0 | 0 |
| mod | 0 | 784 | 0 | 0 |
| cmp | 0 | 784 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 784 | 0 | 1 |
| loop_for | 928 | 812 | 1880 | 0 |
| call | 0 | 1572 | 0 | 10 |

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
| assign | 1925 | 21 | 16141 | 6 |
| add | 1850 | 500 | 15000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1850 | 0 | 30500 | 0 |
| mul_const | 0 | 500 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1850 | 0 | 0 | 0 |
| mod | 1850 | 500 | 0 | 0 |
| cmp | 0 | 500 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 500 | 0 | 1 |
| loop_for | 1920 | 520 | 16120 | 0 |
| call | 0 | 1004 | 0 | 10 |

### Functions for gemver

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 1964 | 1 | 4964 | 10 |
| add | 200 | 0 | 6440 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1600 | 0 | 9600 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2000 | 0 | 0 | 0 |
| mod | 1600 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 1640 | 40 | 4960 | 0 |
| call | 0 | 84 | 0 | 22 |

### Functions for gesummv

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 1863 | 1 | 1921 | 6 |
| add | 1800 | 0 | 1830 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1800 | 0 | 1860 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1830 | 0 | 0 | 0 |
| mod | 1830 | 30 | 0 | 0 |
| cmp | 0 | 30 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 30 | 0 | 1 |
| loop_for | 930 | 30 | 930 | 0 |
| call | 0 | 64 | 0 | 14 |

### Functions for symm

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 1264 | 21 | 1821 | 5 |
| add | 1220 | 600 | 1200 | 6 |
| sub | 600 | 0 | 0 | 0 |
| mul | 0 | 0 | 1800 | 0 |
| mul_const | 0 | 600 | 600 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1200 | 0 | 0 | 0 |
| mod | 1200 | 600 | 0 | 0 |
| cmp | 0 | 600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 600 | 0 | 1 |
| loop_for | 640 | 620 | 620 | 0 |
| call | 0 | 1204 | 0 | 10 |

### Functions for syr2k

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 2164 | 31 | 661 | 5 |
| add | 2100 | 900 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 2100 | 0 | 0 | 0 |
| mul_const | 0 | 900 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2100 | 0 | 0 | 0 |
| mod | 2100 | 900 | 0 | 0 |
| cmp | 0 | 900 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 900 | 0 | 1 |
| loop_for | 1560 | 930 | 630 | 0 |
| call | 0 | 1804 | 0 | 10 |

### Functions for syrk

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 1564 | 31 | 661 | 4 |
| add | 1500 | 900 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1500 | 0 | 0 | 0 |
| mul_const | 0 | 900 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1500 | 0 | 0 | 0 |
| mod | 1500 | 900 | 0 | 0 |
| cmp | 0 | 900 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 900 | 0 | 1 |
| loop_for | 1560 | 930 | 630 | 0 |
| call | 0 | 1804 | 0 | 8 |

### Functions for trmm

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 662 | 21 | 1221 | 4 |
| add | 600 | 600 | 600 | 4 |
| sub | 600 | 0 | 0 | 0 |
| mul | 0 | 0 | 600 | 0 |
| mul_const | 0 | 600 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 600 | 0 | 0 | 0 |
| mod | 600 | 600 | 0 | 0 |
| cmp | 0 | 600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 600 | 0 | 1 |
| loop_for | 620 | 620 | 620 | 0 |
| call | 0 | 1204 | 0 | 8 |

### Functions for 2mm

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 1642 | 17 | 14626 | 9 |
| add | 1996 | 384 | 13248 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1564 | 0 | 19968 | 0 |
| mul_const | 0 | 384 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1564 | 0 | 0 | 0 |
| mod | 1564 | 384 | 0 | 0 |
| cmp | 0 | 384 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 384 | 0 | 1 |
| loop_for | 1636 | 400 | 13952 | 0 |
| call | 0 | 772 | 0 | 14 |

### Functions for 3mm

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 1722 | 17 | 23725 | 12 |
| add | 2528 | 352 | 21600 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1640 | 0 | 21600 | 0 |
| mul_const | 1640 | 352 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1640 | 0 | 0 | 0 |
| mod | 1640 | 352 | 0 | 0 |
| cmp | 0 | 352 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 352 | 0 | 1 |
| loop_for | 1718 | 368 | 22686 | 0 |
| call | 0 | 708 | 0 | 18 |

### Functions for atax

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 1679 | 1 | 3350 | 6 |
| add | 1638 | 0 | 3192 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 3192 | 0 |
| mul_const | 1596 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1638 | 0 | 0 | 0 |
| mod | 1596 | 42 | 0 | 0 |
| cmp | 0 | 42 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 42 | 0 | 1 |
| loop_for | 1676 | 42 | 3272 | 0 |
| call | 0 | 88 | 0 | 12 |

### Functions for bicg

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 1720 | 2 | 3316 | 7 |
| add | 1596 | 0 | 3192 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1596 | 0 | 3192 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1676 | 0 | 0 | 0 |
| mod | 1676 | 80 | 0 | 0 |
| cmp | 0 | 80 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 80 | 0 | 1 |
| loop_for | 1676 | 80 | 1676 | 0 |
| call | 0 | 166 | 0 | 14 |

### Functions for doitgen

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 1208 | 91 | 14571 | 6 |
| add | 960 | 1920 | 11520 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1104 | 0 | 11520 | 0 |
| mul_const | 0 | 2880 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1104 | 0 | 0 | 0 |
| mod | 1104 | 960 | 0 | 0 |
| cmp | 0 | 960 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 960 | 0 | 1 |
| loop_for | 1206 | 1050 | 13530 | 0 |
| call | 0 | 1924 | 0 | 10 |

### Functions for mvt

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 1801 | 2 | 3282 | 6 |
| add | 120 | 0 | 3200 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1600 | 0 | 3200 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1760 | 0 | 0 | 0 |
| mod | 1760 | 80 | 0 | 0 |
| cmp | 0 | 80 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 80 | 0 | 1 |
| loop_for | 1640 | 80 | 3280 | 0 |
| call | 0 | 166 | 0 | 14 |

### Functions for cholesky

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 69045 | 41 | 121 | 2 |
| add | 64042 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 67201 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 68960 | 40 | 40 | 0 |
| call | 2 | 4 | 40 | 6 |

### Functions for durbin

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 41 | 1 | 277 | 3 |
| add | 40 | 0 | 39 | 2 |
| sub | 40 | 0 | 39 | 0 |
| mul | 0 | 0 | 39 | 0 |
| mul_const | 0 | 0 | 39 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 39 | 0 |
| mod | 0 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 41 | 7 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 40 | 40 | 39 | 0 |
| call | 0 | 84 | 0 | 8 |

### Functions for gramschmidt

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 2152 | 52 | 1351 | 5 |
| add | 600 | 1500 | 630 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 600 | 0 | 600 | 0 |
| mul_const | 600 | 1500 | 0 | 3 |
| div | 0 | 0 | 600 | 0 |
| div_const | 600 | 0 | 0 | 0 |
| mod | 600 | 1500 | 0 | 0 |
| cmp | 0 | 1500 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 1500 | 0 | 1 |
| loop_for | 1550 | 1550 | 1230 | 0 |
| call | 0 | 3006 | 30 | 10 |

### Functions for lu

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 69045 | 41 | 81 | 2 |
| add | 64042 | 1600 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000 | 0 | 0 | 0 |
| mul_const | 1 | 1600 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 1600 | 0 | 0 |
| cmp | 0 | 1600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 67201 | 0 | 0 | 5 |
| if | 0 | 1600 | 0 | 1 |
| loop_for | 68960 | 1640 | 40 | 0 |
| call | 2 | 3204 | 0 | 6 |

### Functions for ludcmp

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 69167 | 1 | 323 | 5 |
| add | 64122 | 0 | 40 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 64000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 40 | 0 |
| div_const | 80 | 0 | 0 | 0 |
| mod | 0 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 67201 | 0 | 0 | 14 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 69000 | 40 | 120 | 0 |
| call | 2 | 84 | 0 | 12 |

### Functions for trisolv

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 121 | 1 | 121 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 40 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 40 | 0 | 0 |
| cmp | 0 | 40 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 40 | 0 | 0 | 11 |
| if | 0 | 40 | 0 | 1 |
| loop_for | 40 | 40 | 40 | 0 |
| call | 0 | 84 | 0 | 10 |

### Functions for deriche

| Operation | init_array | print_array | kernel_deriche | main |
|---|---:|---:|---:|---:|
| assign | 4162 | 65 | 83219 | 6 |
| add | 4096 | 4096 | 57346 | 8 |
| sub | 0 | 0 | 132 | 0 |
| mul | 0 | 0 | 12295 | 0 |
| mul_const | 8192 | 4096 | 61444 | 4 |
| div | 0 | 0 | 1 | 0 |
| div_const | 4096 | 0 | 0 | 0 |
| mod | 4096 | 4096 | 0 | 0 |
| cmp | 0 | 4096 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 10 | 13 |
| if | 0 | 4096 | 0 | 1 |
| loop_for | 4160 | 4160 | 24960 | 0 |
| call | 0 | 8196 | 9 | 12 |

### Functions for floyd-warshall

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 7261 | 61 | 219661 | 2 |
| add | 14400 | 3600 | 432000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3600 | 0 | 0 | 0 |
| mul_const | 0 | 3600 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 14400 | 3600 | 0 | 0 |
| cmp | 10800 | 3600 | 216000 | 1 |
| logical | 7200 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 3600 | 3600 | 216000 | 1 |
| loop_for | 3660 | 3660 | 219660 | 0 |
| call | 0 | 7204 | 0 | 6 |

### Functions for nussinov

| Operation | init_array | print_array | kernel_nussinov | main |
|---|---:|---:|---:|---:|
| assign | 3722 | 62 | 61 | 3 |
| add | 60 | 0 | 60 | 3 |
| sub | 0 | 0 | 1 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 60 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 3720 | 60 | 60 | 0 |
| call | 0 | 4 | 0 | 8 |

### Functions for adi

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 421 | 21 | 43254 | 6 |
| add | 400 | 400 | 90722 | 8 |
| sub | 400 | 0 | 93640 | 0 |
| mul | 0 | 0 | 12960 | 0 |
| mul_const | 0 | 400 | 90724 | 4 |
| div | 0 | 0 | 25920 | 0 |
| div_const | 400 | 0 | 7 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 25922 | 11 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 420 | 420 | 26660 | 0 |
| call | 0 | 804 | 0 | 12 |

### Functions for fdtd-2d

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 1842 | 63 | 35861 | 7 |
| add | 1800 | 1800 | 33060 | 7 |
| sub | 0 | 0 | 113860 | 0 |
| mul | 1800 | 0 | 0 | 0 |
| mul_const | 0 | 1800 | 34020 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1800 | 0 | 0 | 0 |
| mod | 0 | 1800 | 0 | 0 |
| cmp | 0 | 1800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 1800 | 0 | 1 |
| loop_for | 640 | 1860 | 35800 | 0 |
| call | 0 | 3608 | 0 | 12 |

### Functions for heat-3d

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 2111 | 111 | 23401 | 4 |
| add | 2000 | 2000 | 184320 | 6 |
| sub | 1000 | 0 | 149160 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 1000 | 3000 | 122880 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1000 | 0 | 0 | 0 |
| mod | 0 | 1000 | 0 | 0 |
| cmp | 0 | 1000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 1000 | 0 | 1 |
| loop_for | 1110 | 1110 | 23380 | 0 |
| call | 0 | 2004 | 0 | 7 |

### Functions for jacobi-1d

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 61 | 1 | 1161 | 4 |
| add | 60 | 0 | 3360 | 2 |
| sub | 0 | 0 | 2280 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 1120 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 60 | 0 | 0 | 0 |
| mod | 0 | 30 | 0 | 0 |
| cmp | 0 | 30 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 30 | 0 | 1 |
| loop_for | 30 | 30 | 1140 | 0 |
| call | 0 | 64 | 0 | 8 |

### Functions for jacobi-2d

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 1831 | 31 | 32521 | 4 |
| add | 3600 | 900 | 188160 | 4 |
| sub | 0 | 0 | 96360 | 0 |
| mul | 1800 | 0 | 0 | 0 |
| mul_const | 0 | 900 | 31360 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1800 | 0 | 0 | 0 |
| mod | 0 | 900 | 0 | 0 |
| cmp | 0 | 900 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 900 | 0 | 1 |
| loop_for | 930 | 930 | 32500 | 0 |
| call | 0 | 1804 | 0 | 8 |

### Functions for seidel-2d

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 1641 | 41 | 29661 | 3 |
| add | 3200 | 1600 | 404320 | 2 |
| sub | 0 | 0 | 203721 | 0 |
| mul | 1600 | 0 | 0 | 0 |
| mul_const | 0 | 1600 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1600 | 0 | 28880 | 0 |
| mod | 0 | 1600 | 0 | 0 |
| cmp | 0 | 1600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 1600 | 0 | 1 |
| loop_for | 1640 | 1640 | 29660 | 0 |
| call | 0 | 3204 | 0 | 6 |

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

- correlation: [datamining/correlation/correlation.operations.MINI.md](datamining/correlation/correlation.operations.MINI.md), [datamining/correlation/correlation.operations.MINI.pdf](datamining/correlation/correlation.operations.MINI.pdf)
- covariance: [datamining/covariance/covariance.operations.MINI.md](datamining/covariance/covariance.operations.MINI.md), [datamining/covariance/covariance.operations.MINI.pdf](datamining/covariance/covariance.operations.MINI.pdf)
- case01: [dummy_tests/case01/case01.operations.MINI.md](dummy_tests/case01/case01.operations.MINI.md), [dummy_tests/case01/case01.operations.MINI.pdf](dummy_tests/case01/case01.operations.MINI.pdf)
- case02: [dummy_tests/case02/case02.operations.MINI.md](dummy_tests/case02/case02.operations.MINI.md), [dummy_tests/case02/case02.operations.MINI.pdf](dummy_tests/case02/case02.operations.MINI.pdf)
- case03: [dummy_tests/case03/case03.operations.MINI.md](dummy_tests/case03/case03.operations.MINI.md), [dummy_tests/case03/case03.operations.MINI.pdf](dummy_tests/case03/case03.operations.MINI.pdf)
- case04: [dummy_tests/case04/case04.operations.MINI.md](dummy_tests/case04/case04.operations.MINI.md), [dummy_tests/case04/case04.operations.MINI.pdf](dummy_tests/case04/case04.operations.MINI.pdf)
- case05: [dummy_tests/case05/case05.operations.MINI.md](dummy_tests/case05/case05.operations.MINI.md), [dummy_tests/case05/case05.operations.MINI.pdf](dummy_tests/case05/case05.operations.MINI.pdf)
- case06: [dummy_tests/case06/case06.operations.MINI.md](dummy_tests/case06/case06.operations.MINI.md), [dummy_tests/case06/case06.operations.MINI.pdf](dummy_tests/case06/case06.operations.MINI.pdf)
- case07: [dummy_tests/case07/case07.operations.MINI.md](dummy_tests/case07/case07.operations.MINI.md), [dummy_tests/case07/case07.operations.MINI.pdf](dummy_tests/case07/case07.operations.MINI.pdf)
- case08: [dummy_tests/case08/case08.operations.MINI.md](dummy_tests/case08/case08.operations.MINI.md), [dummy_tests/case08/case08.operations.MINI.pdf](dummy_tests/case08/case08.operations.MINI.pdf)
- case09: [dummy_tests/case09/case09.operations.MINI.md](dummy_tests/case09/case09.operations.MINI.md), [dummy_tests/case09/case09.operations.MINI.pdf](dummy_tests/case09/case09.operations.MINI.pdf)
- case10: [dummy_tests/case10/case10.operations.MINI.md](dummy_tests/case10/case10.operations.MINI.md), [dummy_tests/case10/case10.operations.MINI.pdf](dummy_tests/case10/case10.operations.MINI.pdf)
- gemm: [linear-algebra/blas/gemm/gemm.operations.MINI.md](linear-algebra/blas/gemm/gemm.operations.MINI.md), [linear-algebra/blas/gemm/gemm.operations.MINI.pdf](linear-algebra/blas/gemm/gemm.operations.MINI.pdf)
- gemver: [linear-algebra/blas/gemver/gemver.operations.MINI.md](linear-algebra/blas/gemver/gemver.operations.MINI.md), [linear-algebra/blas/gemver/gemver.operations.MINI.pdf](linear-algebra/blas/gemver/gemver.operations.MINI.pdf)
- gesummv: [linear-algebra/blas/gesummv/gesummv.operations.MINI.md](linear-algebra/blas/gesummv/gesummv.operations.MINI.md), [linear-algebra/blas/gesummv/gesummv.operations.MINI.pdf](linear-algebra/blas/gesummv/gesummv.operations.MINI.pdf)
- symm: [linear-algebra/blas/symm/symm.operations.MINI.md](linear-algebra/blas/symm/symm.operations.MINI.md), [linear-algebra/blas/symm/symm.operations.MINI.pdf](linear-algebra/blas/symm/symm.operations.MINI.pdf)
- syr2k: [linear-algebra/blas/syr2k/syr2k.operations.MINI.md](linear-algebra/blas/syr2k/syr2k.operations.MINI.md), [linear-algebra/blas/syr2k/syr2k.operations.MINI.pdf](linear-algebra/blas/syr2k/syr2k.operations.MINI.pdf)
- syrk: [linear-algebra/blas/syrk/syrk.operations.MINI.md](linear-algebra/blas/syrk/syrk.operations.MINI.md), [linear-algebra/blas/syrk/syrk.operations.MINI.pdf](linear-algebra/blas/syrk/syrk.operations.MINI.pdf)
- trmm: [linear-algebra/blas/trmm/trmm.operations.MINI.md](linear-algebra/blas/trmm/trmm.operations.MINI.md), [linear-algebra/blas/trmm/trmm.operations.MINI.pdf](linear-algebra/blas/trmm/trmm.operations.MINI.pdf)
- 2mm: [linear-algebra/kernels/2mm/2mm.operations.MINI.md](linear-algebra/kernels/2mm/2mm.operations.MINI.md), [linear-algebra/kernels/2mm/2mm.operations.MINI.pdf](linear-algebra/kernels/2mm/2mm.operations.MINI.pdf)
- 3mm: [linear-algebra/kernels/3mm/3mm.operations.MINI.md](linear-algebra/kernels/3mm/3mm.operations.MINI.md), [linear-algebra/kernels/3mm/3mm.operations.MINI.pdf](linear-algebra/kernels/3mm/3mm.operations.MINI.pdf)
- atax: [linear-algebra/kernels/atax/atax.operations.MINI.md](linear-algebra/kernels/atax/atax.operations.MINI.md), [linear-algebra/kernels/atax/atax.operations.MINI.pdf](linear-algebra/kernels/atax/atax.operations.MINI.pdf)
- bicg: [linear-algebra/kernels/bicg/bicg.operations.MINI.md](linear-algebra/kernels/bicg/bicg.operations.MINI.md), [linear-algebra/kernels/bicg/bicg.operations.MINI.pdf](linear-algebra/kernels/bicg/bicg.operations.MINI.pdf)
- doitgen: [linear-algebra/kernels/doitgen/doitgen.operations.MINI.md](linear-algebra/kernels/doitgen/doitgen.operations.MINI.md), [linear-algebra/kernels/doitgen/doitgen.operations.MINI.pdf](linear-algebra/kernels/doitgen/doitgen.operations.MINI.pdf)
- mvt: [linear-algebra/kernels/mvt/mvt.operations.MINI.md](linear-algebra/kernels/mvt/mvt.operations.MINI.md), [linear-algebra/kernels/mvt/mvt.operations.MINI.pdf](linear-algebra/kernels/mvt/mvt.operations.MINI.pdf)
- cholesky: [linear-algebra/solvers/cholesky/cholesky.operations.MINI.md](linear-algebra/solvers/cholesky/cholesky.operations.MINI.md), [linear-algebra/solvers/cholesky/cholesky.operations.MINI.pdf](linear-algebra/solvers/cholesky/cholesky.operations.MINI.pdf)
- durbin: [linear-algebra/solvers/durbin/durbin.operations.MINI.md](linear-algebra/solvers/durbin/durbin.operations.MINI.md), [linear-algebra/solvers/durbin/durbin.operations.MINI.pdf](linear-algebra/solvers/durbin/durbin.operations.MINI.pdf)
- gramschmidt: [linear-algebra/solvers/gramschmidt/gramschmidt.operations.MINI.md](linear-algebra/solvers/gramschmidt/gramschmidt.operations.MINI.md), [linear-algebra/solvers/gramschmidt/gramschmidt.operations.MINI.pdf](linear-algebra/solvers/gramschmidt/gramschmidt.operations.MINI.pdf)
- lu: [linear-algebra/solvers/lu/lu.operations.MINI.md](linear-algebra/solvers/lu/lu.operations.MINI.md), [linear-algebra/solvers/lu/lu.operations.MINI.pdf](linear-algebra/solvers/lu/lu.operations.MINI.pdf)
- ludcmp: [linear-algebra/solvers/ludcmp/ludcmp.operations.MINI.md](linear-algebra/solvers/ludcmp/ludcmp.operations.MINI.md), [linear-algebra/solvers/ludcmp/ludcmp.operations.MINI.pdf](linear-algebra/solvers/ludcmp/ludcmp.operations.MINI.pdf)
- trisolv: [linear-algebra/solvers/trisolv/trisolv.operations.MINI.md](linear-algebra/solvers/trisolv/trisolv.operations.MINI.md), [linear-algebra/solvers/trisolv/trisolv.operations.MINI.pdf](linear-algebra/solvers/trisolv/trisolv.operations.MINI.pdf)
- deriche: [medley/deriche/deriche.operations.MINI.md](medley/deriche/deriche.operations.MINI.md), [medley/deriche/deriche.operations.MINI.pdf](medley/deriche/deriche.operations.MINI.pdf)
- floyd-warshall: [medley/floyd-warshall/floyd-warshall.operations.MINI.md](medley/floyd-warshall/floyd-warshall.operations.MINI.md), [medley/floyd-warshall/floyd-warshall.operations.MINI.pdf](medley/floyd-warshall/floyd-warshall.operations.MINI.pdf)
- nussinov: [medley/nussinov/nussinov.operations.MINI.md](medley/nussinov/nussinov.operations.MINI.md), [medley/nussinov/nussinov.operations.MINI.pdf](medley/nussinov/nussinov.operations.MINI.pdf)
- adi: [stencils/adi/adi.operations.MINI.md](stencils/adi/adi.operations.MINI.md), [stencils/adi/adi.operations.MINI.pdf](stencils/adi/adi.operations.MINI.pdf)
- fdtd-2d: [stencils/fdtd-2d/fdtd-2d.operations.MINI.md](stencils/fdtd-2d/fdtd-2d.operations.MINI.md), [stencils/fdtd-2d/fdtd-2d.operations.MINI.pdf](stencils/fdtd-2d/fdtd-2d.operations.MINI.pdf)
- heat-3d: [stencils/heat-3d/heat-3d.operations.MINI.md](stencils/heat-3d/heat-3d.operations.MINI.md), [stencils/heat-3d/heat-3d.operations.MINI.pdf](stencils/heat-3d/heat-3d.operations.MINI.pdf)
- jacobi-1d: [stencils/jacobi-1d/jacobi-1d.operations.MINI.md](stencils/jacobi-1d/jacobi-1d.operations.MINI.md), [stencils/jacobi-1d/jacobi-1d.operations.MINI.pdf](stencils/jacobi-1d/jacobi-1d.operations.MINI.pdf)
- jacobi-2d: [stencils/jacobi-2d/jacobi-2d.operations.MINI.md](stencils/jacobi-2d/jacobi-2d.operations.MINI.md), [stencils/jacobi-2d/jacobi-2d.operations.MINI.pdf](stencils/jacobi-2d/jacobi-2d.operations.MINI.pdf)
- seidel-2d: [stencils/seidel-2d/seidel-2d.operations.MINI.md](stencils/seidel-2d/seidel-2d.operations.MINI.md), [stencils/seidel-2d/seidel-2d.operations.MINI.pdf](stencils/seidel-2d/seidel-2d.operations.MINI.pdf)
- polybench: [utilities/polybench.operations.MINI.md](utilities/polybench.operations.MINI.md), [utilities/polybench.operations.MINI.pdf](utilities/polybench.operations.MINI.pdf)
