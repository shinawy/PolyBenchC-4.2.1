# Master Static Operation Report

Generated: 2026-04-21T09:42:40
Root directory: /Users/elshenma/Dropbox/SyncFolder/Benchmarks/PolyBenchC-4.2.1
Dataset mode: LARGE
C files analyzed: 41
Functions analyzed: 140

## Global Totals

| Operation | Count |
|---|---:|
| assign | 62701947804 |
| add | 136070083261 |
| sub | 43545509967 |
| mul | 33471156294 |
| mul_const | 20537429062 |
| div | 1994895602 |
| div_const | 2067618367 |
| mod | 135705521 |
| cmp | 22025347993 |
| logical | 15680032 |
| bitwise | 4 |
| unary | 26016012398 |
| if | 22009667993 |
| loop_for | 61589197648 |
| call | 101338397 |

## Global Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 185838365 |
| assign | float64 | 16476546117 |
| assign | int32 | 22027563196 |
| assign | ptr64 | 24012000123 |
| assign | unknown | 3 |
| add | float32 | 123863042 |
| add | float64 | 44424193901 |
| add | int32 | 67522026317 |
| add | ptr64 | 24000000000 |
| add | unknown | 1 |
| sub | float32 | 4 |
| sub | float64 | 11122327499 |
| sub | int32 | 32423182463 |
| sub | unknown | 1 |
| mul | float32 | 26542087 |
| mul | float64 | 33397028599 |
| mul | int32 | 47585608 |
| mul_const | float32 | 132710404 |
| mul_const | float64 | 20318952503 |
| mul_const | int32 | 85766155 |
| div | float32 | 1 |
| div | float64 | 1994895600 |
| div | int32 | 1 |
| div_const | float32 | 8847360 |
| div_const | float64 | 2058771006 |
| div_const | int32 | 1 |
| mod | int32 | 135705521 |
| cmp | float64 | 1200 |
| cmp | int32 | 22025346793 |
| logical | int32 | 15680031 |
| logical | ptr64 | 1 |
| bitwise | int32 | 4 |
| unary | float32 | 10 |
| unary | float64 | 1992010020 |
| unary | int32 | 2001 |
| unary | ptr64 | 24024000232 |
| unary | unknown | 135 |
| if | int1 | 22009667993 |
| loop_for | int32 | 61589197648 |
| call | unknown | 101338397 |

## Per-File Kernel Operation Matrices

### File Table 1

| Operation | correlation | covariance | case01 | case02 | case03 | case04 |
|---|---:|---:|---:|---:|---:|---:|
| assign | 6733404 | 3366203 | 1 | 2 | 3 | 6 |
| add | 3361199 | 1680000 | 1 | 1 | 0 | 4 |
| sub | 5041202 | 1680000 | 0 | 0 | 2 | 0 |
| mul | 3360000 | 0 | 0 | 1 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 | 0 | 0 |
| div | 1682400 | 1200 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 1200 | 0 | 0 | 0 | 1 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 1200 | 0 | 0 | 0 | 1 | 0 |
| loop_for | 5044999 | 3363800 | 0 | 0 | 0 | 4 |
| call | 1681200 | 0 | 0 | 0 | 0 | 0 |

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
| assign | 1322302001 | 12008004 | 3385201 | 3601001 | 1202401 | 1202401 |
| add | 1320000000 | 16002000 | 3381300 | 2400000 | 0 | 0 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 2641100000 | 24000000 | 3382600 | 3600000 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1200000 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 1322301000 | 12008000 | 1691300 | 1201000 | 1201200 | 1201200 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 4

| Operation | trmm | 2mm | 3mm | atax | bicg | doitgen |
|---|---:|---:|---:|---:|---:|---:|
| assign | 2401001 | 1659361602 | 2705182503 | 7987802 | 7986102 | 547722151 |
| add | 1200000 | 1656000000 | 2700000000 | 7980000 | 7980000 | 537600000 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 1200000 | 2448960000 | 2700000000 | 7980000 | 7980000 | 537600000 |
| mul_const | 0 | 0 | 0 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 1201000 | 1657681600 | 2702592500 | 7984000 | 3994000 | 544341150 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 5

| Operation | mvt | cholesky | durbin | gramschmidt | lu | ludcmp |
|---|---:|---:|---:|---:|---:|---:|
| assign | 8004002 | 6001 | 13997 | 2406001 | 4001 | 16003 |
| add | 8000000 | 0 | 1999 | 1201200 | 0 | 2000 |
| sub | 0 | 0 | 1999 | 0 | 0 | 1 |
| mul | 8000000 | 0 | 1999 | 1200000 | 0 | 0 |
| mul_const | 0 | 0 | 1999 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 1200000 | 0 | 2000 |
| div_const | 0 | 0 | 1999 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 2001 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 8004000 | 2000 | 1999 | 2401200 | 2000 | 6000 |
| call | 0 | 2000 | 0 | 1200 | 0 | 0 |

### File Table 6

| Operation | trisolv | deriche | floyd-warshall | nussinov | adi | fdtd-2d |
|---|---:|---:|---:|---:|---:|---:|
| assign | 6001 | 177011715 | 21959842801 | 2501 | 2994001014 | 1799901501 |
| add | 0 | 123863042 | 43904000000 | 2500 | 6972028002 | 1796701500 |
| sub | 0 | 6260 | 0 | 1 | 6976021000 | 5993301500 |
| mul | 0 | 26542087 | 0 | 0 | 996004000 | 0 |
| mul_const | 0 | 132710404 | 0 | 0 | 6972028004 | 1797800500 |
| div | 2000 | 1 | 0 | 0 | 1992008000 | 0 |
| div_const | 0 | 0 | 0 | 0 | 7 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 21952000000 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 10 | 0 | 0 | 1992008002 | 0 |
| if | 0 | 0 | 21952000000 | 0 | 0 | 0 |
| loop_for | 2000 | 53104864 | 21959842800 | 2500 | 1993006500 | 1799900000 |
| call | 0 | 9 | 0 | 0 | 0 | 0 |

### File Table 7

| Operation | heat-3d | jacobi-1d | jacobi-2d | seidel-2d | polybench |
|---|---:|---:|---:|---:|---:|
| assign | 1657075001 | 1999001 | 1686103001 | 1997001501 | 4 |
| add | 14787288000 | 5994000 | 10108824000 | 27944028000 | 2 |
| sub | 11529309000 | 3997000 | 5057009000 | 13974013001 | 0 |
| mul | 0 | 0 | 0 | 0 | 0 |
| mul_const | 9858192000 | 1998000 | 1684804000 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 1996002000 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 2 |
| if | 0 | 0 | 0 | 0 | 1 |
| loop_for | 1657074500 | 1998500 | 1686102500 | 1997001500 | 0 |
| call | 0 | 0 | 0 | 0 | 3 |

## Function Matrices By File

### Functions for correlation

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 1681402 | 1201 | 6733404 | 6 |
| add | 1680000 | 1440000 | 3361199 | 6 |
| sub | 0 | 0 | 5041202 | 0 |
| mul | 1680000 | 0 | 3360000 | 0 |
| mul_const | 0 | 1440000 | 0 | 2 |
| div | 0 | 0 | 1682400 | 0 |
| div_const | 1680000 | 0 | 0 | 0 |
| mod | 0 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 1200 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 1440000 | 1200 | 1 |
| loop_for | 1681400 | 1441200 | 5044999 | 0 |
| call | 0 | 2880004 | 1681200 | 12 |

### Functions for covariance

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 1681402 | 1201 | 3366203 | 5 |
| add | 0 | 1440000 | 1680000 | 5 |
| sub | 0 | 0 | 1680000 | 0 |
| mul | 1680000 | 0 | 0 | 0 |
| mul_const | 0 | 1440000 | 0 | 2 |
| div | 0 | 0 | 1200 | 0 |
| div_const | 1680000 | 0 | 0 | 0 |
| mod | 0 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 1440000 | 0 | 1 |
| loop_for | 1681400 | 1441200 | 3363800 | 0 |
| call | 0 | 2880004 | 0 | 10 |

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
| assign | 3623205 | 1001 | 1322302001 | 6 |
| add | 3620000 | 1100000 | 1320000000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3620000 | 0 | 2641100000 | 0 |
| mul_const | 0 | 1100000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3620000 | 0 | 0 | 0 |
| mod | 3620000 | 1100000 | 0 | 0 |
| cmp | 0 | 1100000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 1100000 | 0 | 1 |
| loop_for | 3623200 | 1101000 | 1322301000 | 0 |
| call | 0 | 2200004 | 0 | 10 |

### Functions for gemver

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 4018004 | 1 | 12008004 | 10 |
| add | 10000 | 0 | 16002000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4000000 | 0 | 24000000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4020000 | 0 | 0 | 0 |
| mod | 4000000 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 4002000 | 2000 | 12008000 | 0 |
| call | 0 | 4004 | 0 | 22 |

### Functions for gesummv

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 3382603 | 1 | 3385201 | 6 |
| add | 3380000 | 0 | 3381300 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3380000 | 0 | 3382600 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3381300 | 0 | 0 | 0 |
| mod | 3381300 | 1300 | 0 | 0 |
| cmp | 0 | 1300 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 1300 | 0 | 1 |
| loop_for | 1691300 | 1300 | 1691300 | 0 |
| call | 0 | 2604 | 0 | 14 |

### Functions for symm

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 2403004 | 1001 | 3601001 | 5 |
| add | 2401000 | 1200000 | 2400000 | 6 |
| sub | 1200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 3600000 | 0 |
| mul_const | 0 | 1200000 | 1200000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2400000 | 0 | 0 | 0 |
| mod | 2400000 | 1200000 | 0 | 0 |
| cmp | 0 | 1200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 1200000 | 0 | 1 |
| loop_for | 1202000 | 1201000 | 1201000 | 0 |
| call | 0 | 2400004 | 0 | 10 |

### Functions for syr2k

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 3842404 | 1201 | 1202401 | 5 |
| add | 3840000 | 1440000 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3840000 | 0 | 0 | 0 |
| mul_const | 0 | 1440000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3840000 | 0 | 0 | 0 |
| mod | 3840000 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 1440000 | 0 | 1 |
| loop_for | 2642400 | 1441200 | 1201200 | 0 |
| call | 0 | 2880004 | 0 | 10 |

### Functions for syrk

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 2642404 | 1201 | 1202401 | 4 |
| add | 2640000 | 1440000 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 2640000 | 0 | 0 | 0 |
| mul_const | 0 | 1440000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 2640000 | 0 | 0 | 0 |
| mod | 2640000 | 1440000 | 0 | 0 |
| cmp | 0 | 1440000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 1440000 | 0 | 1 |
| loop_for | 2642400 | 1441200 | 1201200 | 0 |
| call | 0 | 2880004 | 0 | 8 |

### Functions for trmm

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 1203002 | 1001 | 2401001 | 4 |
| add | 1200000 | 1200000 | 1200000 | 4 |
| sub | 1200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 1200000 | 0 |
| mul_const | 0 | 1200000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1200000 | 0 | 0 | 0 |
| mod | 1200000 | 1200000 | 0 | 0 |
| cmp | 0 | 1200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 1200000 | 0 | 1 |
| loop_for | 1201000 | 1201000 | 1201000 | 0 |
| call | 0 | 2400004 | 0 | 8 |

### Functions for 2mm

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 3913606 | 801 | 1659361602 | 9 |
| add | 4990000 | 960000 | 1656000000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3910000 | 0 | 2448960000 | 0 |
| mul_const | 0 | 960000 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3910000 | 0 | 0 | 0 |
| mod | 3910000 | 960000 | 0 | 0 |
| cmp | 0 | 960000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 960000 | 0 | 1 |
| loop_for | 3913600 | 960800 | 1657681600 | 0 |
| call | 0 | 1920004 | 0 | 14 |

### Functions for 3mm

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 4103904 | 801 | 2705182503 | 12 |
| add | 6320000 | 880000 | 2700000000 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4100000 | 0 | 2700000000 | 0 |
| mul_const | 4100000 | 880000 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4100000 | 0 | 0 | 0 |
| mod | 4100000 | 880000 | 0 | 0 |
| cmp | 0 | 880000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 880000 | 0 | 1 |
| loop_for | 4103900 | 880800 | 2702592500 | 0 |
| call | 0 | 1760004 | 0 | 18 |

### Functions for atax

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 3994003 | 1 | 7987802 | 6 |
| add | 3992100 | 0 | 7980000 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 7980000 | 0 |
| mul_const | 3990000 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3992100 | 0 | 0 | 0 |
| mod | 3990000 | 2100 | 0 | 0 |
| cmp | 0 | 2100 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 2100 | 0 | 1 |
| loop_for | 3994000 | 2100 | 7984000 | 0 |
| call | 0 | 4204 | 0 | 12 |

### Functions for bicg

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 3996102 | 2 | 7986102 | 7 |
| add | 3990000 | 0 | 7980000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3990000 | 0 | 7980000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3994000 | 0 | 0 | 0 |
| mod | 3994000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 3994000 | 4000 | 3994000 | 0 |
| call | 0 | 8006 | 0 | 14 |

### Functions for doitgen

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 3406912 | 21151 | 547722151 | 6 |
| add | 3360000 | 6720000 | 537600000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3385600 | 0 | 537600000 | 0 |
| mul_const | 0 | 10080000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3385600 | 0 | 0 | 0 |
| mod | 3385600 | 3360000 | 0 | 0 |
| cmp | 0 | 3360000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 3360000 | 0 | 1 |
| loop_for | 3406910 | 3381150 | 544341150 | 0 |
| call | 0 | 6720004 | 0 | 10 |

### Functions for mvt

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 4010001 | 2 | 8004002 | 6 |
| add | 6000 | 0 | 8000000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 4000000 | 0 | 8000000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4008000 | 0 | 0 | 0 |
| mod | 4008000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4002000 | 4000 | 8004000 | 0 |
| call | 0 | 8006 | 0 | 14 |

### Functions for cholesky

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 8012012005 | 2001 | 6001 | 2 |
| add | 8000002002 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 8000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 8008000001 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 8012008000 | 2000 | 2000 | 0 |
| call | 2 | 4 | 2000 | 6 |

### Functions for durbin

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 2001 | 1 | 13997 | 3 |
| add | 2000 | 0 | 1999 | 2 |
| sub | 2000 | 0 | 1999 | 0 |
| mul | 0 | 0 | 1999 | 0 |
| mul_const | 0 | 0 | 1999 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 1999 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 2001 | 7 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 2000 | 2000 | 1999 | 0 |
| call | 0 | 4004 | 0 | 8 |

### Functions for gramschmidt

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 3842202 | 2202 | 2406001 | 5 |
| add | 1200000 | 2640000 | 1201200 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 1200000 | 0 | 1200000 | 0 |
| mul_const | 1200000 | 2640000 | 0 | 3 |
| div | 0 | 0 | 1200000 | 0 |
| div_const | 1200000 | 0 | 0 | 0 |
| mod | 1200000 | 2640000 | 0 | 0 |
| cmp | 0 | 2640000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 2640000 | 0 | 1 |
| loop_for | 2642200 | 2642200 | 2401200 | 0 |
| call | 0 | 5280006 | 1200 | 10 |

### Functions for lu

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 8012012005 | 2001 | 4001 | 2 |
| add | 8000002002 | 4000000 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 8000000000 | 0 | 0 | 0 |
| mul_const | 1 | 4000000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 4000000 | 0 | 0 |
| cmp | 0 | 4000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 8008000001 | 0 | 0 | 5 |
| if | 0 | 4000000 | 0 | 1 |
| loop_for | 8012008000 | 4002000 | 2000 | 0 |
| call | 2 | 8000004 | 0 | 6 |

### Functions for ludcmp

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 8012018007 | 1 | 16003 | 5 |
| add | 8000006002 | 0 | 2000 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 8000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 2000 | 0 |
| div_const | 4000 | 0 | 0 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 8008000001 | 0 | 0 | 14 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 8012010000 | 2000 | 6000 | 0 |
| call | 2 | 4004 | 0 | 12 |

### Functions for trisolv

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 6001 | 1 | 6001 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 2000 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2000 | 0 | 0 | 11 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 2000 | 2000 | 2000 | 0 |
| call | 0 | 4004 | 0 | 10 |

### Functions for deriche

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

### Functions for floyd-warshall

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 15682801 | 2801 | 21959842801 | 2 |
| add | 31360000 | 7840000 | 43904000000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 7840000 | 0 | 0 | 0 |
| mul_const | 0 | 7840000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 31360000 | 7840000 | 0 | 0 |
| cmp | 23520000 | 7840000 | 21952000000 | 1 |
| logical | 15680000 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 7840000 | 7840000 | 21952000000 | 1 |
| loop_for | 7842800 | 7842800 | 21959842800 | 0 |
| call | 0 | 15680004 | 0 | 6 |

### Functions for nussinov

| Operation | init_array | print_array | kernel_nussinov | main |
|---|---:|---:|---:|---:|
| assign | 6255002 | 2502 | 2501 | 3 |
| add | 2500 | 0 | 2500 | 3 |
| sub | 0 | 0 | 1 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 2500 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 6255000 | 2500 | 2500 | 0 |
| call | 0 | 4 | 0 | 8 |

### Functions for adi

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 1001001 | 1001 | 2994001014 | 6 |
| add | 1000000 | 1000000 | 6972028002 | 8 |
| sub | 1000000 | 0 | 6976021000 | 0 |
| mul | 0 | 0 | 996004000 | 0 |
| mul_const | 0 | 1000000 | 6972028004 | 4 |
| div | 0 | 0 | 1992008000 | 0 |
| div_const | 1000000 | 0 | 7 | 0 |
| mod | 0 | 1000000 | 0 | 0 |
| cmp | 0 | 1000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 1992008002 | 11 |
| if | 0 | 1000000 | 0 | 1 |
| loop_for | 1001000 | 1001000 | 1993006500 | 0 |
| call | 0 | 2000004 | 0 | 12 |

### Functions for fdtd-2d

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 3601502 | 3003 | 1799901501 | 7 |
| add | 3600000 | 3600000 | 1796701500 | 7 |
| sub | 0 | 0 | 5993301500 | 0 |
| mul | 3600000 | 0 | 0 | 0 |
| mul_const | 0 | 3600000 | 1797800500 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3600000 | 0 | 0 | 0 |
| mod | 0 | 3600000 | 0 | 0 |
| cmp | 0 | 3600000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 3600000 | 0 | 1 |
| loop_for | 1201500 | 3603000 | 1799900000 | 0 |
| call | 0 | 7200008 | 0 | 12 |

### Functions for heat-3d

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 3470521 | 14521 | 1657075001 | 4 |
| add | 3456000 | 3456000 | 14787288000 | 6 |
| sub | 1728000 | 0 | 11529309000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 1728000 | 5184000 | 9858192000 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 1728000 | 0 | 0 | 0 |
| mod | 0 | 1728000 | 0 | 0 |
| cmp | 0 | 1728000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 1728000 | 0 | 1 |
| loop_for | 1742520 | 1742520 | 1657074500 | 0 |
| call | 0 | 3456004 | 0 | 7 |

### Functions for jacobi-1d

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 4001 | 1 | 1999001 | 4 |
| add | 4000 | 0 | 5994000 | 2 |
| sub | 0 | 0 | 3997000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 1998000 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4000 | 0 | 0 | 0 |
| mod | 0 | 2000 | 0 | 0 |
| cmp | 0 | 2000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 2000 | 0 | 1 |
| loop_for | 2000 | 2000 | 1998500 | 0 |
| call | 0 | 4004 | 0 | 8 |

### Functions for jacobi-2d

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 3381301 | 1301 | 1686103001 | 4 |
| add | 6760000 | 1690000 | 10108824000 | 4 |
| sub | 0 | 0 | 5057009000 | 0 |
| mul | 3380000 | 0 | 0 | 0 |
| mul_const | 0 | 1690000 | 1684804000 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3380000 | 0 | 0 | 0 |
| mod | 0 | 1690000 | 0 | 0 |
| cmp | 0 | 1690000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 1690000 | 0 | 1 |
| loop_for | 1691300 | 1691300 | 1686102500 | 0 |
| call | 0 | 3380004 | 0 | 8 |

### Functions for seidel-2d

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 4002001 | 2001 | 1997001501 | 3 |
| add | 8000000 | 4000000 | 27944028000 | 2 |
| sub | 0 | 0 | 13974013001 | 0 |
| mul | 4000000 | 0 | 0 | 0 |
| mul_const | 0 | 4000000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 4000000 | 0 | 1996002000 | 0 |
| mod | 0 | 4000000 | 0 | 0 |
| cmp | 0 | 4000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 4000000 | 0 | 1 |
| loop_for | 4002000 | 4002000 | 1997001500 | 0 |
| call | 0 | 8000004 | 0 | 6 |

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

- correlation: [datamining/correlation/correlation.operations.LARGE.md](datamining/correlation/correlation.operations.LARGE.md), [datamining/correlation/correlation.operations.LARGE.pdf](datamining/correlation/correlation.operations.LARGE.pdf)
- covariance: [datamining/covariance/covariance.operations.LARGE.md](datamining/covariance/covariance.operations.LARGE.md), [datamining/covariance/covariance.operations.LARGE.pdf](datamining/covariance/covariance.operations.LARGE.pdf)
- case01: [dummy_tests/case01/case01.operations.LARGE.md](dummy_tests/case01/case01.operations.LARGE.md), [dummy_tests/case01/case01.operations.LARGE.pdf](dummy_tests/case01/case01.operations.LARGE.pdf)
- case02: [dummy_tests/case02/case02.operations.LARGE.md](dummy_tests/case02/case02.operations.LARGE.md), [dummy_tests/case02/case02.operations.LARGE.pdf](dummy_tests/case02/case02.operations.LARGE.pdf)
- case03: [dummy_tests/case03/case03.operations.LARGE.md](dummy_tests/case03/case03.operations.LARGE.md), [dummy_tests/case03/case03.operations.LARGE.pdf](dummy_tests/case03/case03.operations.LARGE.pdf)
- case04: [dummy_tests/case04/case04.operations.LARGE.md](dummy_tests/case04/case04.operations.LARGE.md), [dummy_tests/case04/case04.operations.LARGE.pdf](dummy_tests/case04/case04.operations.LARGE.pdf)
- case05: [dummy_tests/case05/case05.operations.LARGE.md](dummy_tests/case05/case05.operations.LARGE.md), [dummy_tests/case05/case05.operations.LARGE.pdf](dummy_tests/case05/case05.operations.LARGE.pdf)
- case06: [dummy_tests/case06/case06.operations.LARGE.md](dummy_tests/case06/case06.operations.LARGE.md), [dummy_tests/case06/case06.operations.LARGE.pdf](dummy_tests/case06/case06.operations.LARGE.pdf)
- case07: [dummy_tests/case07/case07.operations.LARGE.md](dummy_tests/case07/case07.operations.LARGE.md), [dummy_tests/case07/case07.operations.LARGE.pdf](dummy_tests/case07/case07.operations.LARGE.pdf)
- case08: [dummy_tests/case08/case08.operations.LARGE.md](dummy_tests/case08/case08.operations.LARGE.md), [dummy_tests/case08/case08.operations.LARGE.pdf](dummy_tests/case08/case08.operations.LARGE.pdf)
- case09: [dummy_tests/case09/case09.operations.LARGE.md](dummy_tests/case09/case09.operations.LARGE.md), [dummy_tests/case09/case09.operations.LARGE.pdf](dummy_tests/case09/case09.operations.LARGE.pdf)
- case10: [dummy_tests/case10/case10.operations.LARGE.md](dummy_tests/case10/case10.operations.LARGE.md), [dummy_tests/case10/case10.operations.LARGE.pdf](dummy_tests/case10/case10.operations.LARGE.pdf)
- gemm: [linear-algebra/blas/gemm/gemm.operations.LARGE.md](linear-algebra/blas/gemm/gemm.operations.LARGE.md), [linear-algebra/blas/gemm/gemm.operations.LARGE.pdf](linear-algebra/blas/gemm/gemm.operations.LARGE.pdf)
- gemver: [linear-algebra/blas/gemver/gemver.operations.LARGE.md](linear-algebra/blas/gemver/gemver.operations.LARGE.md), [linear-algebra/blas/gemver/gemver.operations.LARGE.pdf](linear-algebra/blas/gemver/gemver.operations.LARGE.pdf)
- gesummv: [linear-algebra/blas/gesummv/gesummv.operations.LARGE.md](linear-algebra/blas/gesummv/gesummv.operations.LARGE.md), [linear-algebra/blas/gesummv/gesummv.operations.LARGE.pdf](linear-algebra/blas/gesummv/gesummv.operations.LARGE.pdf)
- symm: [linear-algebra/blas/symm/symm.operations.LARGE.md](linear-algebra/blas/symm/symm.operations.LARGE.md), [linear-algebra/blas/symm/symm.operations.LARGE.pdf](linear-algebra/blas/symm/symm.operations.LARGE.pdf)
- syr2k: [linear-algebra/blas/syr2k/syr2k.operations.LARGE.md](linear-algebra/blas/syr2k/syr2k.operations.LARGE.md), [linear-algebra/blas/syr2k/syr2k.operations.LARGE.pdf](linear-algebra/blas/syr2k/syr2k.operations.LARGE.pdf)
- syrk: [linear-algebra/blas/syrk/syrk.operations.LARGE.md](linear-algebra/blas/syrk/syrk.operations.LARGE.md), [linear-algebra/blas/syrk/syrk.operations.LARGE.pdf](linear-algebra/blas/syrk/syrk.operations.LARGE.pdf)
- trmm: [linear-algebra/blas/trmm/trmm.operations.LARGE.md](linear-algebra/blas/trmm/trmm.operations.LARGE.md), [linear-algebra/blas/trmm/trmm.operations.LARGE.pdf](linear-algebra/blas/trmm/trmm.operations.LARGE.pdf)
- 2mm: [linear-algebra/kernels/2mm/2mm.operations.LARGE.md](linear-algebra/kernels/2mm/2mm.operations.LARGE.md), [linear-algebra/kernels/2mm/2mm.operations.LARGE.pdf](linear-algebra/kernels/2mm/2mm.operations.LARGE.pdf)
- 3mm: [linear-algebra/kernels/3mm/3mm.operations.LARGE.md](linear-algebra/kernels/3mm/3mm.operations.LARGE.md), [linear-algebra/kernels/3mm/3mm.operations.LARGE.pdf](linear-algebra/kernels/3mm/3mm.operations.LARGE.pdf)
- atax: [linear-algebra/kernels/atax/atax.operations.LARGE.md](linear-algebra/kernels/atax/atax.operations.LARGE.md), [linear-algebra/kernels/atax/atax.operations.LARGE.pdf](linear-algebra/kernels/atax/atax.operations.LARGE.pdf)
- bicg: [linear-algebra/kernels/bicg/bicg.operations.LARGE.md](linear-algebra/kernels/bicg/bicg.operations.LARGE.md), [linear-algebra/kernels/bicg/bicg.operations.LARGE.pdf](linear-algebra/kernels/bicg/bicg.operations.LARGE.pdf)
- doitgen: [linear-algebra/kernels/doitgen/doitgen.operations.LARGE.md](linear-algebra/kernels/doitgen/doitgen.operations.LARGE.md), [linear-algebra/kernels/doitgen/doitgen.operations.LARGE.pdf](linear-algebra/kernels/doitgen/doitgen.operations.LARGE.pdf)
- mvt: [linear-algebra/kernels/mvt/mvt.operations.LARGE.md](linear-algebra/kernels/mvt/mvt.operations.LARGE.md), [linear-algebra/kernels/mvt/mvt.operations.LARGE.pdf](linear-algebra/kernels/mvt/mvt.operations.LARGE.pdf)
- cholesky: [linear-algebra/solvers/cholesky/cholesky.operations.LARGE.md](linear-algebra/solvers/cholesky/cholesky.operations.LARGE.md), [linear-algebra/solvers/cholesky/cholesky.operations.LARGE.pdf](linear-algebra/solvers/cholesky/cholesky.operations.LARGE.pdf)
- durbin: [linear-algebra/solvers/durbin/durbin.operations.LARGE.md](linear-algebra/solvers/durbin/durbin.operations.LARGE.md), [linear-algebra/solvers/durbin/durbin.operations.LARGE.pdf](linear-algebra/solvers/durbin/durbin.operations.LARGE.pdf)
- gramschmidt: [linear-algebra/solvers/gramschmidt/gramschmidt.operations.LARGE.md](linear-algebra/solvers/gramschmidt/gramschmidt.operations.LARGE.md), [linear-algebra/solvers/gramschmidt/gramschmidt.operations.LARGE.pdf](linear-algebra/solvers/gramschmidt/gramschmidt.operations.LARGE.pdf)
- lu: [linear-algebra/solvers/lu/lu.operations.LARGE.md](linear-algebra/solvers/lu/lu.operations.LARGE.md), [linear-algebra/solvers/lu/lu.operations.LARGE.pdf](linear-algebra/solvers/lu/lu.operations.LARGE.pdf)
- ludcmp: [linear-algebra/solvers/ludcmp/ludcmp.operations.LARGE.md](linear-algebra/solvers/ludcmp/ludcmp.operations.LARGE.md), [linear-algebra/solvers/ludcmp/ludcmp.operations.LARGE.pdf](linear-algebra/solvers/ludcmp/ludcmp.operations.LARGE.pdf)
- trisolv: [linear-algebra/solvers/trisolv/trisolv.operations.LARGE.md](linear-algebra/solvers/trisolv/trisolv.operations.LARGE.md), [linear-algebra/solvers/trisolv/trisolv.operations.LARGE.pdf](linear-algebra/solvers/trisolv/trisolv.operations.LARGE.pdf)
- deriche: [medley/deriche/deriche.operations.LARGE.md](medley/deriche/deriche.operations.LARGE.md), [medley/deriche/deriche.operations.LARGE.pdf](medley/deriche/deriche.operations.LARGE.pdf)
- floyd-warshall: [medley/floyd-warshall/floyd-warshall.operations.LARGE.md](medley/floyd-warshall/floyd-warshall.operations.LARGE.md), [medley/floyd-warshall/floyd-warshall.operations.LARGE.pdf](medley/floyd-warshall/floyd-warshall.operations.LARGE.pdf)
- nussinov: [medley/nussinov/nussinov.operations.LARGE.md](medley/nussinov/nussinov.operations.LARGE.md), [medley/nussinov/nussinov.operations.LARGE.pdf](medley/nussinov/nussinov.operations.LARGE.pdf)
- adi: [stencils/adi/adi.operations.LARGE.md](stencils/adi/adi.operations.LARGE.md), [stencils/adi/adi.operations.LARGE.pdf](stencils/adi/adi.operations.LARGE.pdf)
- fdtd-2d: [stencils/fdtd-2d/fdtd-2d.operations.LARGE.md](stencils/fdtd-2d/fdtd-2d.operations.LARGE.md), [stencils/fdtd-2d/fdtd-2d.operations.LARGE.pdf](stencils/fdtd-2d/fdtd-2d.operations.LARGE.pdf)
- heat-3d: [stencils/heat-3d/heat-3d.operations.LARGE.md](stencils/heat-3d/heat-3d.operations.LARGE.md), [stencils/heat-3d/heat-3d.operations.LARGE.pdf](stencils/heat-3d/heat-3d.operations.LARGE.pdf)
- jacobi-1d: [stencils/jacobi-1d/jacobi-1d.operations.LARGE.md](stencils/jacobi-1d/jacobi-1d.operations.LARGE.md), [stencils/jacobi-1d/jacobi-1d.operations.LARGE.pdf](stencils/jacobi-1d/jacobi-1d.operations.LARGE.pdf)
- jacobi-2d: [stencils/jacobi-2d/jacobi-2d.operations.LARGE.md](stencils/jacobi-2d/jacobi-2d.operations.LARGE.md), [stencils/jacobi-2d/jacobi-2d.operations.LARGE.pdf](stencils/jacobi-2d/jacobi-2d.operations.LARGE.pdf)
- seidel-2d: [stencils/seidel-2d/seidel-2d.operations.LARGE.md](stencils/seidel-2d/seidel-2d.operations.LARGE.md), [stencils/seidel-2d/seidel-2d.operations.LARGE.pdf](stencils/seidel-2d/seidel-2d.operations.LARGE.pdf)
- polybench: [utilities/polybench.operations.LARGE.md](utilities/polybench.operations.LARGE.md), [utilities/polybench.operations.LARGE.pdf](utilities/polybench.operations.LARGE.pdf)
