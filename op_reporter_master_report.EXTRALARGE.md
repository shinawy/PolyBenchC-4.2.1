# Master Static Operation Report

Generated: 2026-04-21T09:42:37
Root directory: /Users/elshenma/Dropbox/SyncFolder/Benchmarks/PolyBenchC-4.2.1
Dataset mode: EXTRALARGE
C files analyzed: 41
Functions analyzed: 140

## Global Totals

| Operation | Count |
|---|---:|
| assign | 506794490046 |
| add | 1124274618001 |
| sub | 375656603611 |
| mul | 269649553314 |
| mul_const | 181149835882 |
| div | 15981031802 |
| div_const | 16260409507 |
| mod | 535133401 |
| cmp | 175918307233 |
| logical | 62720032 |
| bitwise | 4 |
| unary | 208064024398 |
| if | 175855587233 |
| loop_for | 498385701662 |
| call | 424258877 |

## Global Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 696813613 |
| assign | float64 | 138100300917 |
| assign | int32 | 175949375390 |
| assign | ptr64 | 192048000123 |
| assign | unknown | 3 |
| add | float32 | 464486402 |
| add | float64 | 379811326001 |
| add | int32 | 551998805597 |
| add | ptr64 | 192000000000 |
| add | unknown | 1 |
| sub | float32 | 4 |
| sub | float64 | 98950574999 |
| sub | int32 | 276706028607 |
| sub | unknown | 1 |
| mul | float32 | 99532807 |
| mul | float64 | 269362157599 |
| mul | int32 | 187862908 |
| mul_const | float32 | 497664004 |
| mul_const | float64 | 180311569003 |
| mul_const | int32 | 340602875 |
| div | float32 | 1 |
| div | float64 | 15981031800 |
| div | int32 | 1 |
| div_const | float32 | 33177600 |
| div_const | float64 | 16227231906 |
| div_const | int32 | 1 |
| mod | int32 | 535133401 |
| cmp | float64 | 2600 |
| cmp | int32 | 175918304633 |
| logical | int32 | 62720031 |
| logical | ptr64 | 1 |
| bitwise | int32 | 4 |
| unary | float32 | 10 |
| unary | float64 | 15968020020 |
| unary | int32 | 4001 |
| unary | ptr64 | 192096000232 |
| unary | unknown | 135 |
| if | int1 | 175855587233 |
| loop_for | int32 | 498385701662 |
| call | unknown | 424258877 |

## Per-File Kernel Operation Matrices

### File Table 1

| Operation | correlation | covariance | case01 | case02 | case03 | case04 |
|---|---:|---:|---:|---:|---:|---:|
| assign | 31229004 | 15613403 | 1 | 2 | 3 | 6 |
| add | 15602599 | 7800000 | 1 | 1 | 0 | 4 |
| sub | 23402602 | 7800000 | 0 | 0 | 2 | 0 |
| mul | 15600000 | 0 | 0 | 1 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 | 0 | 0 |
| div | 7805200 | 2600 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 2600 | 0 | 0 | 0 | 1 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 2600 | 0 | 0 | 0 | 1 | 0 |
| loop_for | 23410799 | 15608200 | 0 | 0 | 0 | 4 |
| call | 7802600 | 0 | 0 | 0 | 0 | 0 |

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
| assign | 11969804001 | 48016004 | 15691201 | 15602001 | 5205201 | 5205201 |
| add | 11960000000 | 64004000 | 15682800 | 10400000 | 0 | 0 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 23924600000 | 96000000 | 15685600 | 15600000 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 5200000 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 11969802000 | 48016000 | 7842800 | 5202000 | 5202600 | 5202600 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 4

| Operation | trmm | 2mm | 3mm | atax | bicg | doitgen |
|---|---:|---:|---:|---:|---:|---:|
| assign | 10402001 | 13261443202 | 21620725003 | 7927602 | 7926202 | 4054160251 |
| add | 5200000 | 13248000000 | 21600000000 | 7920000 | 7920000 | 4009500000 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 5200000 | 19587840000 | 21600000000 | 7920000 | 7920000 | 4009500000 |
| mul_const | 0 | 0 | 0 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 5202000 | 13254723200 | 21610365000 | 7924000 | 3964000 | 4039255250 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 5

| Operation | mvt | cholesky | durbin | gramschmidt | lu | ludcmp |
|---|---:|---:|---:|---:|---:|---:|
| assign | 32008002 | 12001 | 27997 | 10413001 | 8001 | 32003 |
| add | 32000000 | 0 | 3999 | 5202600 | 0 | 4000 |
| sub | 0 | 0 | 3999 | 0 | 0 | 1 |
| mul | 32000000 | 0 | 3999 | 5200000 | 0 | 0 |
| mul_const | 0 | 0 | 3999 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 5200000 | 0 | 4000 |
| div_const | 0 | 0 | 3999 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 4001 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 32008000 | 4000 | 3999 | 10402600 | 4000 | 12000 |
| call | 0 | 4000 | 0 | 2600 | 0 | 0 |

### File Table 6

| Operation | trisolv | deriche | floyd-warshall | nussinov | adi | fdtd-2d |
|---|---:|---:|---:|---:|---:|---:|
| assign | 12001 | 663675379 | 175647365601 | 5501 | 23976002014 | 15599403001 |
| add | 0 | 464486402 | 351232000000 | 5500 | 55888056002 | 15586203000 |
| sub | 0 | 12004 | 0 | 1 | 55904042000 | 51971803000 |
| mul | 0 | 99532807 | 0 | 0 | 7984008000 | 0 |
| mul_const | 0 | 497664004 | 0 | 0 | 55888056004 | 15590801000 |
| div | 4000 | 1 | 0 | 0 | 15968016000 | 0 |
| div_const | 0 | 0 | 0 | 0 | 7 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 175616000000 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 10 | 0 | 0 | 15968016002 | 0 |
| if | 0 | 0 | 175616000000 | 0 | 0 | 0 |
| loop_for | 4000 | 199104960 | 175647365600 | 5500 | 15972013000 | 15599400000 |
| call | 0 | 9 | 0 | 0 | 0 | 0 |

### File Table 7

| Operation | heat-3d | jacobi-1d | jacobi-2d | seidel-2d | polybench |
|---|---:|---:|---:|---:|---:|
| assign | 15603590001 | 7998001 | 15663206001 | 15988003001 | 4 |
| add | 139723056000 | 23988000 | 93945648000 | 223776056000 | 2 |
| sub | 108831098000 | 15994000 | 46984018000 | 111896026001 | 0 |
| mul | 0 | 0 | 0 | 0 | 0 |
| mul_const | 93148704000 | 7996000 | 15657608000 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 15984004000 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 2 |
| if | 0 | 0 | 0 | 0 | 1 |
| loop_for | 15603589000 | 7997000 | 15663205000 | 15988003000 | 0 |
| call | 0 | 0 | 0 | 0 | 3 |

## Function Matrices By File

### Functions for correlation

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 7803002 | 2601 | 31229004 | 6 |
| add | 7800000 | 6760000 | 15602599 | 6 |
| sub | 0 | 0 | 23402602 | 0 |
| mul | 7800000 | 0 | 15600000 | 0 |
| mul_const | 0 | 6760000 | 0 | 2 |
| div | 0 | 0 | 7805200 | 0 |
| div_const | 7800000 | 0 | 0 | 0 |
| mod | 0 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 2600 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 6760000 | 2600 | 1 |
| loop_for | 7803000 | 6762600 | 23410799 | 0 |
| call | 0 | 13520004 | 7802600 | 12 |

### Functions for covariance

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 7803002 | 2601 | 15613403 | 5 |
| add | 0 | 6760000 | 7800000 | 5 |
| sub | 0 | 0 | 7800000 | 0 |
| mul | 7800000 | 0 | 0 | 0 |
| mul_const | 0 | 6760000 | 0 | 2 |
| div | 0 | 0 | 2600 | 0 |
| div_const | 7800000 | 0 | 0 | 0 |
| mod | 0 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 6760000 | 0 | 1 |
| loop_for | 7803000 | 6762600 | 15608200 | 0 |
| call | 0 | 13520004 | 0 | 10 |

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
| assign | 15786605 | 2001 | 11969804001 | 6 |
| add | 15780000 | 4600000 | 11960000000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15780000 | 0 | 23924600000 | 0 |
| mul_const | 0 | 4600000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15780000 | 0 | 0 | 0 |
| mod | 15780000 | 4600000 | 0 | 0 |
| cmp | 0 | 4600000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 4600000 | 0 | 1 |
| loop_for | 15786600 | 4602000 | 11969802000 | 0 |
| call | 0 | 9200004 | 0 | 10 |

### Functions for gemver

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 16036004 | 1 | 48016004 | 10 |
| add | 20000 | 0 | 64004000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16000000 | 0 | 96000000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16040000 | 0 | 0 | 0 |
| mod | 16000000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 16004000 | 4000 | 48016000 | 0 |
| call | 0 | 8004 | 0 | 22 |

### Functions for gesummv

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 15685603 | 1 | 15691201 | 6 |
| add | 15680000 | 0 | 15682800 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15680000 | 0 | 15685600 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15682800 | 0 | 0 | 0 |
| mod | 15682800 | 2800 | 0 | 0 |
| cmp | 0 | 2800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 2800 | 0 | 1 |
| loop_for | 7842800 | 2800 | 7842800 | 0 |
| call | 0 | 5604 | 0 | 14 |

### Functions for symm

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 10406004 | 2001 | 15602001 | 5 |
| add | 10402000 | 5200000 | 10400000 | 6 |
| sub | 5200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 15600000 | 0 |
| mul_const | 0 | 5200000 | 5200000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 10400000 | 0 | 0 | 0 |
| mod | 10400000 | 5200000 | 0 | 0 |
| cmp | 0 | 5200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 5200000 | 0 | 1 |
| loop_for | 5204000 | 5202000 | 5202000 | 0 |
| call | 0 | 10400004 | 0 | 10 |

### Functions for syr2k

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 17165204 | 2601 | 5205201 | 5 |
| add | 17160000 | 6760000 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 17160000 | 0 | 0 | 0 |
| mul_const | 0 | 6760000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 17160000 | 0 | 0 | 0 |
| mod | 17160000 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 6760000 | 0 | 1 |
| loop_for | 11965200 | 6762600 | 5202600 | 0 |
| call | 0 | 13520004 | 0 | 10 |

### Functions for syrk

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 11965204 | 2601 | 5205201 | 4 |
| add | 11960000 | 6760000 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 11960000 | 0 | 0 | 0 |
| mul_const | 0 | 6760000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 11960000 | 0 | 0 | 0 |
| mod | 11960000 | 6760000 | 0 | 0 |
| cmp | 0 | 6760000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 6760000 | 0 | 1 |
| loop_for | 11965200 | 6762600 | 5202600 | 0 |
| call | 0 | 13520004 | 0 | 8 |

### Functions for trmm

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 5206002 | 2001 | 10402001 | 4 |
| add | 5200000 | 5200000 | 5200000 | 4 |
| sub | 5200000 | 0 | 0 | 0 |
| mul | 0 | 0 | 5200000 | 0 |
| mul_const | 0 | 5200000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 5200000 | 0 | 0 | 0 |
| mod | 5200000 | 5200000 | 0 | 0 |
| cmp | 0 | 5200000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 5200000 | 0 | 1 |
| loop_for | 5202000 | 5202000 | 5202000 | 0 |
| call | 0 | 10400004 | 0 | 8 |

### Functions for 2mm

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 15647206 | 1601 | 13261443202 | 9 |
| add | 19960000 | 3840000 | 13248000000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 15640000 | 0 | 19587840000 | 0 |
| mul_const | 0 | 3840000 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15640000 | 0 | 0 | 0 |
| mod | 15640000 | 3840000 | 0 | 0 |
| cmp | 0 | 3840000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 3840000 | 0 | 1 |
| loop_for | 15647200 | 3841600 | 13254723200 | 0 |
| call | 0 | 7680004 | 0 | 14 |

### Functions for 3mm

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 16407804 | 1601 | 21620725003 | 12 |
| add | 25280000 | 3520000 | 21600000000 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 16400000 | 0 | 21600000000 | 0 |
| mul_const | 16400000 | 3520000 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16400000 | 0 | 0 | 0 |
| mod | 16400000 | 3520000 | 0 | 0 |
| cmp | 0 | 3520000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 3520000 | 0 | 1 |
| loop_for | 16407800 | 3521600 | 21610365000 | 0 |
| call | 0 | 7040004 | 0 | 18 |

### Functions for atax

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 3964003 | 1 | 7927602 | 6 |
| add | 3962200 | 0 | 7920000 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 7920000 | 0 |
| mul_const | 3960000 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3962200 | 0 | 0 | 0 |
| mod | 3960000 | 2200 | 0 | 0 |
| cmp | 0 | 2200 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 2200 | 0 | 1 |
| loop_for | 3964000 | 2200 | 7924000 | 0 |
| call | 0 | 4404 | 0 | 12 |

### Functions for bicg

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 3966202 | 2 | 7926202 | 7 |
| add | 3960000 | 0 | 7920000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 3960000 | 0 | 7920000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 3964000 | 0 | 0 | 0 |
| mod | 3964000 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 3964000 | 4000 | 3964000 | 0 |
| call | 0 | 8006 | 0 | 14 |

### Functions for doitgen

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 14978422 | 55251 | 4054160251 | 6 |
| add | 14850000 | 29700000 | 4009500000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 14922900 | 0 | 4009500000 | 0 |
| mul_const | 0 | 44550000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 14922900 | 0 | 0 | 0 |
| mod | 14922900 | 14850000 | 0 | 0 |
| cmp | 0 | 14850000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 14850000 | 0 | 1 |
| loop_for | 14978420 | 14905250 | 4039255250 | 0 |
| call | 0 | 29700004 | 0 | 10 |

### Functions for mvt

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

### Functions for cholesky

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 64048024005 | 4001 | 12001 | 2 |
| add | 64000004002 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64032000001 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 64048016000 | 4000 | 4000 | 0 |
| call | 2 | 4 | 4000 | 6 |

### Functions for durbin

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 4001 | 1 | 27997 | 3 |
| add | 4000 | 0 | 3999 | 2 |
| sub | 4000 | 0 | 3999 | 0 |
| mul | 0 | 0 | 3999 | 0 |
| mul_const | 0 | 0 | 3999 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 3999 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 4001 | 7 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4000 | 4000 | 3999 | 0 |
| call | 0 | 8004 | 0 | 8 |

### Functions for gramschmidt

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 17164602 | 4602 | 10413001 | 5 |
| add | 5200000 | 11960000 | 5202600 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 5200000 | 0 | 5200000 | 0 |
| mul_const | 5200000 | 11960000 | 0 | 3 |
| div | 0 | 0 | 5200000 | 0 |
| div_const | 5200000 | 0 | 0 | 0 |
| mod | 5200000 | 11960000 | 0 | 0 |
| cmp | 0 | 11960000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 11960000 | 0 | 1 |
| loop_for | 11964600 | 11964600 | 10402600 | 0 |
| call | 0 | 23920006 | 2600 | 10 |

### Functions for lu

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 64048024005 | 4001 | 8001 | 2 |
| add | 64000004002 | 16000000 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000000000 | 0 | 0 | 0 |
| mul_const | 1 | 16000000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 16000000 | 0 | 0 |
| cmp | 0 | 16000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64032000001 | 0 | 0 | 5 |
| if | 0 | 16000000 | 0 | 1 |
| loop_for | 64048016000 | 16004000 | 4000 | 0 |
| call | 2 | 32000004 | 0 | 6 |

### Functions for ludcmp

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 64048036007 | 1 | 32003 | 5 |
| add | 64000012002 | 0 | 4000 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 64000000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 4000 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64032000001 | 0 | 0 | 14 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 64048020000 | 4000 | 12000 | 0 |
| call | 2 | 8004 | 0 | 12 |

### Functions for trisolv

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 12001 | 1 | 12001 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 4000 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 4000 | 0 | 0 | 11 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4000 | 4000 | 4000 | 0 |
| call | 0 | 8004 | 0 | 10 |

### Functions for deriche

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

### Functions for floyd-warshall

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

### Functions for nussinov

| Operation | init_array | print_array | kernel_nussinov | main |
|---|---:|---:|---:|---:|
| assign | 30261002 | 5502 | 5501 | 3 |
| add | 5500 | 0 | 5500 | 3 |
| sub | 0 | 0 | 1 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 5500 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 30261000 | 5500 | 5500 | 0 |
| call | 0 | 4 | 0 | 8 |

### Functions for adi

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

### Functions for fdtd-2d

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 15603002 | 6003 | 15599403001 | 7 |
| add | 15600000 | 15600000 | 15586203000 | 7 |
| sub | 0 | 0 | 51971803000 | 0 |
| mul | 15600000 | 0 | 0 | 0 |
| mul_const | 0 | 15600000 | 15590801000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15600000 | 0 | 0 | 0 |
| mod | 0 | 15600000 | 0 | 0 |
| cmp | 0 | 15600000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 15600000 | 0 | 1 |
| loop_for | 5203000 | 15606000 | 15599400000 | 0 |
| call | 0 | 31200008 | 0 | 12 |

### Functions for heat-3d

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 16040201 | 40201 | 15603590001 | 4 |
| add | 16000000 | 16000000 | 139723056000 | 6 |
| sub | 8000000 | 0 | 108831098000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 8000000 | 24000000 | 93148704000 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 8000000 | 0 | 0 | 0 |
| mod | 0 | 8000000 | 0 | 0 |
| cmp | 0 | 8000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 8000000 | 0 | 1 |
| loop_for | 8040200 | 8040200 | 15603589000 | 0 |
| call | 0 | 16000004 | 0 | 7 |

### Functions for jacobi-1d

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 8001 | 1 | 7998001 | 4 |
| add | 8000 | 0 | 23988000 | 2 |
| sub | 0 | 0 | 15994000 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 7996000 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 8000 | 0 | 0 | 0 |
| mod | 0 | 4000 | 0 | 0 |
| cmp | 0 | 4000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 4000 | 0 | 1 |
| loop_for | 4000 | 4000 | 7997000 | 0 |
| call | 0 | 8004 | 0 | 8 |

### Functions for jacobi-2d

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 15682801 | 2801 | 15663206001 | 4 |
| add | 31360000 | 7840000 | 93945648000 | 4 |
| sub | 0 | 0 | 46984018000 | 0 |
| mul | 15680000 | 0 | 0 | 0 |
| mul_const | 0 | 7840000 | 15657608000 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 15680000 | 0 | 0 | 0 |
| mod | 0 | 7840000 | 0 | 0 |
| cmp | 0 | 7840000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 7840000 | 0 | 1 |
| loop_for | 7842800 | 7842800 | 15663205000 | 0 |
| call | 0 | 15680004 | 0 | 8 |

### Functions for seidel-2d

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 16004001 | 4001 | 15988003001 | 3 |
| add | 32000000 | 16000000 | 223776056000 | 2 |
| sub | 0 | 0 | 111896026001 | 0 |
| mul | 16000000 | 0 | 0 | 0 |
| mul_const | 0 | 16000000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 16000000 | 0 | 15984004000 | 0 |
| mod | 0 | 16000000 | 0 | 0 |
| cmp | 0 | 16000000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 16000000 | 0 | 1 |
| loop_for | 16004000 | 16004000 | 15988003000 | 0 |
| call | 0 | 32000004 | 0 | 6 |

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

- correlation: [datamining/correlation/correlation.operations.EXTRALARGE.md](datamining/correlation/correlation.operations.EXTRALARGE.md), [datamining/correlation/correlation.operations.EXTRALARGE.pdf](datamining/correlation/correlation.operations.EXTRALARGE.pdf)
- covariance: [datamining/covariance/covariance.operations.EXTRALARGE.md](datamining/covariance/covariance.operations.EXTRALARGE.md), [datamining/covariance/covariance.operations.EXTRALARGE.pdf](datamining/covariance/covariance.operations.EXTRALARGE.pdf)
- case01: [dummy_tests/case01/case01.operations.EXTRALARGE.md](dummy_tests/case01/case01.operations.EXTRALARGE.md), [dummy_tests/case01/case01.operations.EXTRALARGE.pdf](dummy_tests/case01/case01.operations.EXTRALARGE.pdf)
- case02: [dummy_tests/case02/case02.operations.EXTRALARGE.md](dummy_tests/case02/case02.operations.EXTRALARGE.md), [dummy_tests/case02/case02.operations.EXTRALARGE.pdf](dummy_tests/case02/case02.operations.EXTRALARGE.pdf)
- case03: [dummy_tests/case03/case03.operations.EXTRALARGE.md](dummy_tests/case03/case03.operations.EXTRALARGE.md), [dummy_tests/case03/case03.operations.EXTRALARGE.pdf](dummy_tests/case03/case03.operations.EXTRALARGE.pdf)
- case04: [dummy_tests/case04/case04.operations.EXTRALARGE.md](dummy_tests/case04/case04.operations.EXTRALARGE.md), [dummy_tests/case04/case04.operations.EXTRALARGE.pdf](dummy_tests/case04/case04.operations.EXTRALARGE.pdf)
- case05: [dummy_tests/case05/case05.operations.EXTRALARGE.md](dummy_tests/case05/case05.operations.EXTRALARGE.md), [dummy_tests/case05/case05.operations.EXTRALARGE.pdf](dummy_tests/case05/case05.operations.EXTRALARGE.pdf)
- case06: [dummy_tests/case06/case06.operations.EXTRALARGE.md](dummy_tests/case06/case06.operations.EXTRALARGE.md), [dummy_tests/case06/case06.operations.EXTRALARGE.pdf](dummy_tests/case06/case06.operations.EXTRALARGE.pdf)
- case07: [dummy_tests/case07/case07.operations.EXTRALARGE.md](dummy_tests/case07/case07.operations.EXTRALARGE.md), [dummy_tests/case07/case07.operations.EXTRALARGE.pdf](dummy_tests/case07/case07.operations.EXTRALARGE.pdf)
- case08: [dummy_tests/case08/case08.operations.EXTRALARGE.md](dummy_tests/case08/case08.operations.EXTRALARGE.md), [dummy_tests/case08/case08.operations.EXTRALARGE.pdf](dummy_tests/case08/case08.operations.EXTRALARGE.pdf)
- case09: [dummy_tests/case09/case09.operations.EXTRALARGE.md](dummy_tests/case09/case09.operations.EXTRALARGE.md), [dummy_tests/case09/case09.operations.EXTRALARGE.pdf](dummy_tests/case09/case09.operations.EXTRALARGE.pdf)
- case10: [dummy_tests/case10/case10.operations.EXTRALARGE.md](dummy_tests/case10/case10.operations.EXTRALARGE.md), [dummy_tests/case10/case10.operations.EXTRALARGE.pdf](dummy_tests/case10/case10.operations.EXTRALARGE.pdf)
- gemm: [linear-algebra/blas/gemm/gemm.operations.EXTRALARGE.md](linear-algebra/blas/gemm/gemm.operations.EXTRALARGE.md), [linear-algebra/blas/gemm/gemm.operations.EXTRALARGE.pdf](linear-algebra/blas/gemm/gemm.operations.EXTRALARGE.pdf)
- gemver: [linear-algebra/blas/gemver/gemver.operations.EXTRALARGE.md](linear-algebra/blas/gemver/gemver.operations.EXTRALARGE.md), [linear-algebra/blas/gemver/gemver.operations.EXTRALARGE.pdf](linear-algebra/blas/gemver/gemver.operations.EXTRALARGE.pdf)
- gesummv: [linear-algebra/blas/gesummv/gesummv.operations.EXTRALARGE.md](linear-algebra/blas/gesummv/gesummv.operations.EXTRALARGE.md), [linear-algebra/blas/gesummv/gesummv.operations.EXTRALARGE.pdf](linear-algebra/blas/gesummv/gesummv.operations.EXTRALARGE.pdf)
- symm: [linear-algebra/blas/symm/symm.operations.EXTRALARGE.md](linear-algebra/blas/symm/symm.operations.EXTRALARGE.md), [linear-algebra/blas/symm/symm.operations.EXTRALARGE.pdf](linear-algebra/blas/symm/symm.operations.EXTRALARGE.pdf)
- syr2k: [linear-algebra/blas/syr2k/syr2k.operations.EXTRALARGE.md](linear-algebra/blas/syr2k/syr2k.operations.EXTRALARGE.md), [linear-algebra/blas/syr2k/syr2k.operations.EXTRALARGE.pdf](linear-algebra/blas/syr2k/syr2k.operations.EXTRALARGE.pdf)
- syrk: [linear-algebra/blas/syrk/syrk.operations.EXTRALARGE.md](linear-algebra/blas/syrk/syrk.operations.EXTRALARGE.md), [linear-algebra/blas/syrk/syrk.operations.EXTRALARGE.pdf](linear-algebra/blas/syrk/syrk.operations.EXTRALARGE.pdf)
- trmm: [linear-algebra/blas/trmm/trmm.operations.EXTRALARGE.md](linear-algebra/blas/trmm/trmm.operations.EXTRALARGE.md), [linear-algebra/blas/trmm/trmm.operations.EXTRALARGE.pdf](linear-algebra/blas/trmm/trmm.operations.EXTRALARGE.pdf)
- 2mm: [linear-algebra/kernels/2mm/2mm.operations.EXTRALARGE.md](linear-algebra/kernels/2mm/2mm.operations.EXTRALARGE.md), [linear-algebra/kernels/2mm/2mm.operations.EXTRALARGE.pdf](linear-algebra/kernels/2mm/2mm.operations.EXTRALARGE.pdf)
- 3mm: [linear-algebra/kernels/3mm/3mm.operations.EXTRALARGE.md](linear-algebra/kernels/3mm/3mm.operations.EXTRALARGE.md), [linear-algebra/kernels/3mm/3mm.operations.EXTRALARGE.pdf](linear-algebra/kernels/3mm/3mm.operations.EXTRALARGE.pdf)
- atax: [linear-algebra/kernels/atax/atax.operations.EXTRALARGE.md](linear-algebra/kernels/atax/atax.operations.EXTRALARGE.md), [linear-algebra/kernels/atax/atax.operations.EXTRALARGE.pdf](linear-algebra/kernels/atax/atax.operations.EXTRALARGE.pdf)
- bicg: [linear-algebra/kernels/bicg/bicg.operations.EXTRALARGE.md](linear-algebra/kernels/bicg/bicg.operations.EXTRALARGE.md), [linear-algebra/kernels/bicg/bicg.operations.EXTRALARGE.pdf](linear-algebra/kernels/bicg/bicg.operations.EXTRALARGE.pdf)
- doitgen: [linear-algebra/kernels/doitgen/doitgen.operations.EXTRALARGE.md](linear-algebra/kernels/doitgen/doitgen.operations.EXTRALARGE.md), [linear-algebra/kernels/doitgen/doitgen.operations.EXTRALARGE.pdf](linear-algebra/kernels/doitgen/doitgen.operations.EXTRALARGE.pdf)
- mvt: [linear-algebra/kernels/mvt/mvt.operations.EXTRALARGE.md](linear-algebra/kernels/mvt/mvt.operations.EXTRALARGE.md), [linear-algebra/kernels/mvt/mvt.operations.EXTRALARGE.pdf](linear-algebra/kernels/mvt/mvt.operations.EXTRALARGE.pdf)
- cholesky: [linear-algebra/solvers/cholesky/cholesky.operations.EXTRALARGE.md](linear-algebra/solvers/cholesky/cholesky.operations.EXTRALARGE.md), [linear-algebra/solvers/cholesky/cholesky.operations.EXTRALARGE.pdf](linear-algebra/solvers/cholesky/cholesky.operations.EXTRALARGE.pdf)
- durbin: [linear-algebra/solvers/durbin/durbin.operations.EXTRALARGE.md](linear-algebra/solvers/durbin/durbin.operations.EXTRALARGE.md), [linear-algebra/solvers/durbin/durbin.operations.EXTRALARGE.pdf](linear-algebra/solvers/durbin/durbin.operations.EXTRALARGE.pdf)
- gramschmidt: [linear-algebra/solvers/gramschmidt/gramschmidt.operations.EXTRALARGE.md](linear-algebra/solvers/gramschmidt/gramschmidt.operations.EXTRALARGE.md), [linear-algebra/solvers/gramschmidt/gramschmidt.operations.EXTRALARGE.pdf](linear-algebra/solvers/gramschmidt/gramschmidt.operations.EXTRALARGE.pdf)
- lu: [linear-algebra/solvers/lu/lu.operations.EXTRALARGE.md](linear-algebra/solvers/lu/lu.operations.EXTRALARGE.md), [linear-algebra/solvers/lu/lu.operations.EXTRALARGE.pdf](linear-algebra/solvers/lu/lu.operations.EXTRALARGE.pdf)
- ludcmp: [linear-algebra/solvers/ludcmp/ludcmp.operations.EXTRALARGE.md](linear-algebra/solvers/ludcmp/ludcmp.operations.EXTRALARGE.md), [linear-algebra/solvers/ludcmp/ludcmp.operations.EXTRALARGE.pdf](linear-algebra/solvers/ludcmp/ludcmp.operations.EXTRALARGE.pdf)
- trisolv: [linear-algebra/solvers/trisolv/trisolv.operations.EXTRALARGE.md](linear-algebra/solvers/trisolv/trisolv.operations.EXTRALARGE.md), [linear-algebra/solvers/trisolv/trisolv.operations.EXTRALARGE.pdf](linear-algebra/solvers/trisolv/trisolv.operations.EXTRALARGE.pdf)
- deriche: [medley/deriche/deriche.operations.EXTRALARGE.md](medley/deriche/deriche.operations.EXTRALARGE.md), [medley/deriche/deriche.operations.EXTRALARGE.pdf](medley/deriche/deriche.operations.EXTRALARGE.pdf)
- floyd-warshall: [medley/floyd-warshall/floyd-warshall.operations.EXTRALARGE.md](medley/floyd-warshall/floyd-warshall.operations.EXTRALARGE.md), [medley/floyd-warshall/floyd-warshall.operations.EXTRALARGE.pdf](medley/floyd-warshall/floyd-warshall.operations.EXTRALARGE.pdf)
- nussinov: [medley/nussinov/nussinov.operations.EXTRALARGE.md](medley/nussinov/nussinov.operations.EXTRALARGE.md), [medley/nussinov/nussinov.operations.EXTRALARGE.pdf](medley/nussinov/nussinov.operations.EXTRALARGE.pdf)
- adi: [stencils/adi/adi.operations.EXTRALARGE.md](stencils/adi/adi.operations.EXTRALARGE.md), [stencils/adi/adi.operations.EXTRALARGE.pdf](stencils/adi/adi.operations.EXTRALARGE.pdf)
- fdtd-2d: [stencils/fdtd-2d/fdtd-2d.operations.EXTRALARGE.md](stencils/fdtd-2d/fdtd-2d.operations.EXTRALARGE.md), [stencils/fdtd-2d/fdtd-2d.operations.EXTRALARGE.pdf](stencils/fdtd-2d/fdtd-2d.operations.EXTRALARGE.pdf)
- heat-3d: [stencils/heat-3d/heat-3d.operations.EXTRALARGE.md](stencils/heat-3d/heat-3d.operations.EXTRALARGE.md), [stencils/heat-3d/heat-3d.operations.EXTRALARGE.pdf](stencils/heat-3d/heat-3d.operations.EXTRALARGE.pdf)
- jacobi-1d: [stencils/jacobi-1d/jacobi-1d.operations.EXTRALARGE.md](stencils/jacobi-1d/jacobi-1d.operations.EXTRALARGE.md), [stencils/jacobi-1d/jacobi-1d.operations.EXTRALARGE.pdf](stencils/jacobi-1d/jacobi-1d.operations.EXTRALARGE.pdf)
- jacobi-2d: [stencils/jacobi-2d/jacobi-2d.operations.EXTRALARGE.md](stencils/jacobi-2d/jacobi-2d.operations.EXTRALARGE.md), [stencils/jacobi-2d/jacobi-2d.operations.EXTRALARGE.pdf](stencils/jacobi-2d/jacobi-2d.operations.EXTRALARGE.pdf)
- seidel-2d: [stencils/seidel-2d/seidel-2d.operations.EXTRALARGE.md](stencils/seidel-2d/seidel-2d.operations.EXTRALARGE.md), [stencils/seidel-2d/seidel-2d.operations.EXTRALARGE.pdf](stencils/seidel-2d/seidel-2d.operations.EXTRALARGE.pdf)
- polybench: [utilities/polybench.operations.EXTRALARGE.md](utilities/polybench.operations.EXTRALARGE.md), [utilities/polybench.operations.EXTRALARGE.pdf](utilities/polybench.operations.EXTRALARGE.pdf)
