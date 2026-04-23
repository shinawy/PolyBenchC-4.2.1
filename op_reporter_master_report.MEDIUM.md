# Master Static Operation Report

Generated: 2026-04-21T09:42:44
Root directory: /Users/elshenma/Dropbox/SyncFolder/Benchmarks/PolyBenchC-4.2.1
Dataset mode: MEDIUM
C files analyzed: 41
Functions analyzed: 140

## Global Totals

| Operation | Count |
|---|---:|
| assign | 465611296 |
| add | 973932441 |
| sub | 328765951 |
| mul | 278684914 |
| mul_const | 156049582 |
| div | 15793522 |
| div_const | 18658367 |
| mod | 5058011 |
| cmp | 127654033 |
| logical | 500032 |
| bitwise | 4 |
| unary | 208642798 |
| if | 127154033 |
| loop_for | 453190272 |
| call | 3871277 |

## Global Width Totals

| Operation | Width | Count |
|---|---|---:|
| assign | float32 | 7266013 |
| assign | float64 | 138260467 |
| assign | int32 | 127604690 |
| assign | ptr64 | 192480123 |
| assign | unknown | 3 |
| add | float32 | 4838402 |
| add | float64 | 343611961 |
| add | int32 | 433482077 |
| add | ptr64 | 192000000 |
| add | unknown | 1 |
| sub | float32 | 4 |
| sub | float64 | 82235099 |
| sub | int32 | 246530847 |
| sub | unknown | 1 |
| mul | float32 | 1036807 |
| mul | float64 | 275834099 |
| mul | int32 | 1814008 |
| mul_const | float32 | 5184004 |
| mul_const | float64 | 147584903 |
| mul_const | int32 | 3280675 |
| div | float32 | 1 |
| div | float64 | 15793520 |
| div | int32 | 1 |
| div_const | float32 | 345600 |
| div_const | float64 | 18312766 |
| div_const | int32 | 1 |
| mod | int32 | 5058011 |
| cmp | float64 | 240 |
| cmp | int32 | 127653793 |
| logical | int32 | 500031 |
| logical | ptr64 | 1 |
| bitwise | int32 | 4 |
| unary | float32 | 10 |
| unary | float64 | 15682020 |
| unary | int32 | 401 |
| unary | ptr64 | 192960232 |
| unary | unknown | 135 |
| if | int1 | 127154033 |
| loop_for | int32 | 453190272 |
| call | unknown | 3871277 |

## Per-File Kernel Operation Matrices

### File Table 1

| Operation | correlation | covariance | case01 | case02 | case03 | case04 |
|---|---:|---:|---:|---:|---:|---:|
| assign | 252264 | 126023 | 1 | 2 | 3 | 6 |
| add | 125039 | 62400 | 1 | 1 | 0 | 4 |
| sub | 187442 | 62400 | 0 | 0 | 2 | 0 |
| mul | 124800 | 0 | 0 | 1 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 | 0 | 0 |
| div | 62880 | 240 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 240 | 0 | 0 | 0 | 1 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 240 | 0 | 0 | 0 | 1 | 0 |
| loop_for | 188179 | 125540 | 0 | 0 | 0 | 4 |
| call | 62640 | 0 | 0 | 0 | 0 | 0 |

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
| assign | 10652401 | 481604 | 126001 | 144201 | 48481 | 48481 |
| add | 10560000 | 640400 | 125250 | 96000 | 0 | 0 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 21164000 | 960000 | 125500 | 144000 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 48000 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 10652200 | 481600 | 62750 | 48200 | 48240 | 48240 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 4

| Operation | trmm | 2mm | 3mm | atax | bicg | doitgen |
|---|---:|---:|---:|---:|---:|---:|
| assign | 96201 | 14853962 | 23024353 | 321382 | 321012 | 7564051 |
| add | 48000 | 14706000 | 22800000 | 319800 | 319800 | 7200000 |
| sub | 0 | 0 | 0 | 0 | 0 | 0 |
| mul | 48000 | 21927600 | 22800000 | 319800 | 319800 | 7200000 |
| mul_const | 0 | 0 | 0 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 48200 | 14780160 | 22912450 | 320600 | 160700 | 7442050 |
| call | 0 | 0 | 0 | 0 | 0 | 0 |

### File Table 5

| Operation | mvt | cholesky | durbin | gramschmidt | lu | ludcmp |
|---|---:|---:|---:|---:|---:|---:|
| assign | 320802 | 1201 | 2797 | 97201 | 801 | 3203 |
| add | 320000 | 0 | 399 | 48240 | 0 | 400 |
| sub | 0 | 0 | 399 | 0 | 0 | 1 |
| mul | 320000 | 0 | 399 | 48000 | 0 | 0 |
| mul_const | 0 | 0 | 399 | 0 | 0 | 0 |
| div | 0 | 0 | 0 | 48000 | 0 | 400 |
| div_const | 0 | 0 | 399 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 401 | 0 | 0 | 0 |
| if | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_for | 320800 | 400 | 399 | 96240 | 400 | 1200 |
| call | 0 | 400 | 0 | 240 | 0 | 0 |

### File Table 6

| Operation | trisolv | deriche | floyd-warshall | nussinov | adi | fdtd-2d |
|---|---:|---:|---:|---:|---:|---:|
| assign | 1201 | 6924259 | 125250501 | 501 | 23760214 | 14396301 |
| add | 0 | 4838402 | 250000000 | 500 | 54885602 | 14268300 |
| sub | 0 | 1204 | 0 | 1 | 55044200 | 47732300 |
| mul | 0 | 1036807 | 0 | 0 | 7840800 | 0 |
| mul_const | 0 | 5184004 | 0 | 0 | 54885604 | 14312100 |
| div | 400 | 1 | 0 | 0 | 15681600 | 0 |
| div_const | 0 | 0 | 0 | 0 | 7 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 125000000 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 0 | 0 |
| bitwise | 0 | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 10 | 0 | 0 | 15681602 | 0 |
| if | 0 | 0 | 125000000 | 0 | 0 | 0 |
| loop_for | 400 | 2077440 | 125250500 | 500 | 15721300 | 14396000 |
| call | 0 | 9 | 0 | 0 | 0 | 0 |

### File Table 7

| Operation | heat-3d | jacobi-1d | jacobi-2d | seidel-2d | polybench |
|---|---:|---:|---:|---:|---:|
| assign | 11271001 | 79801 | 12350601 | 15880301 | 4 |
| add | 98769600 | 238800 | 73804800 | 221765600 | 2 |
| sub | 77413800 | 159400 | 37001800 | 110962601 | 0 |
| mul | 0 | 0 | 0 | 0 | 0 |
| mul_const | 65846400 | 79600 | 12300800 | 0 | 0 |
| div | 0 | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 15840400 | 0 |
| mod | 0 | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 0 | 0 |
| logical | 0 | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 0 | 2 |
| if | 0 | 0 | 0 | 0 | 1 |
| loop_for | 11270900 | 79700 | 12350500 | 15880300 | 0 |
| call | 0 | 0 | 0 | 0 | 3 |

## Function Matrices By File

### Functions for correlation

| Operation | init_array | print_array | kernel_correlation | main |
|---|---:|---:|---:|---:|
| assign | 62662 | 241 | 252264 | 6 |
| add | 62400 | 57600 | 125039 | 6 |
| sub | 0 | 0 | 187442 | 0 |
| mul | 62400 | 0 | 124800 | 0 |
| mul_const | 0 | 57600 | 0 | 2 |
| div | 0 | 0 | 62880 | 0 |
| div_const | 62400 | 0 | 0 | 0 |
| mod | 0 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 240 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 12 |
| if | 0 | 57600 | 240 | 1 |
| loop_for | 62660 | 57840 | 188179 | 0 |
| call | 0 | 115204 | 62640 | 12 |

### Functions for covariance

| Operation | init_array | print_array | kernel_covariance | main |
|---|---:|---:|---:|---:|
| assign | 62662 | 241 | 126023 | 5 |
| add | 0 | 57600 | 62400 | 5 |
| sub | 0 | 0 | 62400 | 0 |
| mul | 62400 | 0 | 0 | 0 |
| mul_const | 0 | 57600 | 0 | 2 |
| div | 0 | 0 | 240 | 0 |
| div_const | 62400 | 0 | 0 | 0 |
| mod | 0 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 10 |
| if | 0 | 57600 | 0 | 1 |
| loop_for | 62660 | 57840 | 125540 | 0 |
| call | 0 | 115204 | 0 | 10 |

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
| assign | 145445 | 201 | 10652401 | 6 |
| add | 144800 | 44000 | 10560000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 144800 | 0 | 21164000 | 0 |
| mul_const | 0 | 44000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 144800 | 0 | 0 | 0 |
| mod | 144800 | 44000 | 0 | 0 |
| cmp | 0 | 44000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 44000 | 0 | 1 |
| loop_for | 145440 | 44200 | 10652200 | 0 |
| call | 0 | 88004 | 0 | 10 |

### Functions for gemver

| Operation | init_array | print_array | kernel_gemver | main |
|---|---:|---:|---:|---:|
| assign | 163604 | 1 | 481604 | 10 |
| add | 2000 | 0 | 640400 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 160000 | 0 | 960000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 164000 | 0 | 0 | 0 |
| mod | 160000 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 31 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 160400 | 400 | 481600 | 0 |
| call | 0 | 804 | 0 | 22 |

### Functions for gesummv

| Operation | init_array | print_array | kernel_gesummv | main |
|---|---:|---:|---:|---:|
| assign | 125503 | 1 | 126001 | 6 |
| add | 125000 | 0 | 125250 | 7 |
| sub | 0 | 0 | 0 | 0 |
| mul | 125000 | 0 | 125500 | 0 |
| mul_const | 0 | 0 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 125250 | 0 | 0 | 0 |
| mod | 125250 | 250 | 0 | 0 |
| cmp | 0 | 250 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 17 |
| if | 0 | 250 | 0 | 1 |
| loop_for | 62750 | 250 | 62750 | 0 |
| call | 0 | 504 | 0 | 14 |

### Functions for symm

| Operation | init_array | print_array | kernel_symm | main |
|---|---:|---:|---:|---:|
| assign | 96604 | 201 | 144201 | 5 |
| add | 96200 | 48000 | 96000 | 6 |
| sub | 48000 | 0 | 0 | 0 |
| mul | 0 | 0 | 144000 | 0 |
| mul_const | 0 | 48000 | 48000 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 96000 | 0 | 0 | 0 |
| mod | 96000 | 48000 | 0 | 0 |
| cmp | 0 | 48000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 48000 | 0 | 1 |
| loop_for | 48400 | 48200 | 48200 | 0 |
| call | 0 | 96004 | 0 | 10 |

### Functions for syr2k

| Operation | init_array | print_array | kernel_syr2k | main |
|---|---:|---:|---:|---:|
| assign | 154084 | 241 | 48481 | 5 |
| add | 153600 | 57600 | 0 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 153600 | 0 | 0 | 0 |
| mul_const | 0 | 57600 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 153600 | 0 | 0 | 0 |
| mod | 153600 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 13 |
| if | 0 | 57600 | 0 | 1 |
| loop_for | 106080 | 57840 | 48240 | 0 |
| call | 0 | 115204 | 0 | 10 |

### Functions for syrk

| Operation | init_array | print_array | kernel_syrk | main |
|---|---:|---:|---:|---:|
| assign | 106084 | 241 | 48481 | 4 |
| add | 105600 | 57600 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 105600 | 0 | 0 | 0 |
| mul_const | 0 | 57600 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 105600 | 0 | 0 | 0 |
| mod | 105600 | 57600 | 0 | 0 |
| cmp | 0 | 57600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 10 |
| if | 0 | 57600 | 0 | 1 |
| loop_for | 106080 | 57840 | 48240 | 0 |
| call | 0 | 115204 | 0 | 8 |

### Functions for trmm

| Operation | init_array | print_array | kernel_trmm | main |
|---|---:|---:|---:|---:|
| assign | 48602 | 201 | 96201 | 4 |
| add | 48000 | 48000 | 48000 | 4 |
| sub | 48000 | 0 | 0 | 0 |
| mul | 0 | 0 | 48000 | 0 |
| mul_const | 0 | 48000 | 0 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 48000 | 0 | 0 | 0 |
| mod | 48000 | 48000 | 0 | 0 |
| cmp | 0 | 48000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 0 | 9 |
| if | 0 | 48000 | 0 | 1 |
| loop_for | 48200 | 48200 | 48200 | 0 |
| call | 0 | 96004 | 0 | 8 |

### Functions for 2mm

| Operation | init_array | print_array | kernel_2mm | main |
|---|---:|---:|---:|---:|
| assign | 159866 | 181 | 14853962 | 9 |
| add | 200900 | 39600 | 14706000 | 10 |
| sub | 0 | 0 | 0 | 0 |
| mul | 159100 | 0 | 21927600 | 0 |
| mul_const | 0 | 39600 | 0 | 5 |
| div | 0 | 0 | 0 | 0 |
| div_const | 159100 | 0 | 0 | 0 |
| mod | 159100 | 39600 | 0 | 0 |
| cmp | 0 | 39600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 2 | 0 | 0 | 18 |
| if | 0 | 39600 | 0 | 1 |
| loop_for | 159860 | 39780 | 14780160 | 0 |
| call | 0 | 79204 | 0 | 14 |

### Functions for 3mm

| Operation | init_array | print_array | kernel_3mm | main |
|---|---:|---:|---:|---:|
| assign | 162794 | 181 | 23024353 | 12 |
| add | 246200 | 37800 | 22800000 | 14 |
| sub | 0 | 0 | 0 | 0 |
| mul | 162000 | 0 | 22800000 | 0 |
| mul_const | 162000 | 37800 | 0 | 7 |
| div | 0 | 0 | 0 | 0 |
| div_const | 162000 | 0 | 0 | 0 |
| mod | 162000 | 37800 | 0 | 0 |
| cmp | 0 | 37800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 20 |
| if | 0 | 37800 | 0 | 1 |
| loop_for | 162790 | 37980 | 22912450 | 0 |
| call | 0 | 75604 | 0 | 18 |

### Functions for atax

| Operation | init_array | print_array | kernel_atax | main |
|---|---:|---:|---:|---:|
| assign | 160703 | 1 | 321382 | 6 |
| add | 160310 | 0 | 319800 | 5 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 319800 | 0 |
| mul_const | 159900 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 160310 | 0 | 0 | 0 |
| mod | 159900 | 410 | 0 | 0 |
| cmp | 0 | 410 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 12 |
| if | 0 | 410 | 0 | 1 |
| loop_for | 160700 | 410 | 320600 | 0 |
| call | 0 | 824 | 0 | 12 |

### Functions for bicg

| Operation | init_array | print_array | kernel_bicg | main |
|---|---:|---:|---:|---:|
| assign | 161112 | 2 | 321012 | 7 |
| add | 159900 | 0 | 319800 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 159900 | 0 | 319800 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 160700 | 0 | 0 | 0 |
| mod | 160700 | 800 | 0 | 0 |
| cmp | 0 | 800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 800 | 0 | 1 |
| loop_for | 160700 | 800 | 160700 | 0 |
| call | 0 | 1606 | 0 | 14 |

### Functions for doitgen

| Operation | init_array | print_array | kernel_doitgen | main |
|---|---:|---:|---:|---:|
| assign | 125712 | 2051 | 7564051 | 6 |
| add | 120000 | 240000 | 7200000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 123600 | 0 | 7200000 | 0 |
| mul_const | 0 | 360000 | 0 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 123600 | 0 | 0 | 0 |
| mod | 123600 | 120000 | 0 | 0 |
| cmp | 0 | 120000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 10 |
| if | 0 | 120000 | 0 | 1 |
| loop_for | 125710 | 122050 | 7442050 | 0 |
| call | 0 | 240004 | 0 | 10 |

### Functions for mvt

| Operation | init_array | print_array | kernel_mvt | main |
|---|---:|---:|---:|---:|
| assign | 162001 | 2 | 320802 | 6 |
| add | 1200 | 0 | 320000 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 160000 | 0 | 320000 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 161600 | 0 | 0 | 0 |
| mod | 161600 | 800 | 0 | 0 |
| cmp | 0 | 800 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 18 |
| if | 0 | 800 | 0 | 1 |
| loop_for | 160400 | 800 | 320800 | 0 |
| call | 0 | 1606 | 0 | 14 |

### Functions for cholesky

| Operation | init_array | print_array | kernel_cholesky | main |
|---|---:|---:|---:|---:|
| assign | 64482405 | 401 | 1201 | 2 |
| add | 64000402 | 0 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64320001 | 0 | 0 | 5 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 64481600 | 400 | 400 | 0 |
| call | 2 | 4 | 400 | 6 |

### Functions for durbin

| Operation | init_array | print_array | kernel_durbin | main |
|---|---:|---:|---:|---:|
| assign | 401 | 1 | 2797 | 3 |
| add | 400 | 0 | 399 | 2 |
| sub | 400 | 0 | 399 | 0 |
| mul | 0 | 0 | 399 | 0 |
| mul_const | 0 | 0 | 399 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 399 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 401 | 7 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 400 | 400 | 399 | 0 |
| call | 0 | 804 | 0 | 8 |

### Functions for gramschmidt

| Operation | init_array | print_array | kernel_gramschmidt | main |
|---|---:|---:|---:|---:|
| assign | 154042 | 442 | 97201 | 5 |
| add | 48000 | 105600 | 48240 | 6 |
| sub | 0 | 0 | 0 | 0 |
| mul | 48000 | 0 | 48000 | 0 |
| mul_const | 48000 | 105600 | 0 | 3 |
| div | 0 | 0 | 48000 | 0 |
| div_const | 48000 | 0 | 0 | 0 |
| mod | 48000 | 105600 | 0 | 0 |
| cmp | 0 | 105600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 13 |
| if | 0 | 105600 | 0 | 1 |
| loop_for | 106040 | 106040 | 96240 | 0 |
| call | 0 | 211206 | 240 | 10 |

### Functions for lu

| Operation | init_array | print_array | kernel_lu | main |
|---|---:|---:|---:|---:|
| assign | 64482405 | 401 | 801 | 2 |
| add | 64000402 | 160000 | 0 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 64000000 | 0 | 0 | 0 |
| mul_const | 1 | 160000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 160000 | 0 | 0 |
| cmp | 0 | 160000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64320001 | 0 | 0 | 5 |
| if | 0 | 160000 | 0 | 1 |
| loop_for | 64481600 | 160400 | 400 | 0 |
| call | 2 | 320004 | 0 | 6 |

### Functions for ludcmp

| Operation | init_array | print_array | kernel_ludcmp | main |
|---|---:|---:|---:|---:|
| assign | 64483607 | 1 | 3203 | 5 |
| add | 64001202 | 0 | 400 | 5 |
| sub | 0 | 0 | 1 | 0 |
| mul | 64000000 | 0 | 0 | 0 |
| mul_const | 1 | 0 | 0 | 1 |
| div | 0 | 0 | 400 | 0 |
| div_const | 800 | 0 | 0 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 64320001 | 0 | 0 | 14 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 64482000 | 400 | 1200 | 0 |
| call | 2 | 804 | 0 | 12 |

### Functions for trisolv

| Operation | init_array | print_array | kernel_trisolv | main |
|---|---:|---:|---:|---:|
| assign | 1201 | 1 | 1201 | 4 |
| add | 0 | 0 | 0 | 4 |
| sub | 0 | 0 | 0 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 400 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 400 | 0 | 0 | 11 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 400 | 400 | 400 | 0 |
| call | 0 | 804 | 0 | 10 |

### Functions for deriche

| Operation | init_array | print_array | kernel_deriche | main |
|---|---:|---:|---:|---:|
| assign | 346322 | 721 | 6924259 | 6 |
| add | 345600 | 345600 | 4838402 | 8 |
| sub | 0 | 0 | 1204 | 0 |
| mul | 0 | 0 | 1036807 | 0 |
| mul_const | 691200 | 345600 | 5184004 | 4 |
| div | 0 | 0 | 1 | 0 |
| div_const | 345600 | 0 | 0 | 0 |
| mod | 345600 | 345600 | 0 | 0 |
| cmp | 0 | 345600 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 1 | 0 | 10 | 13 |
| if | 0 | 345600 | 0 | 1 |
| loop_for | 346320 | 346320 | 2077440 | 0 |
| call | 0 | 691204 | 9 | 12 |

### Functions for floyd-warshall

| Operation | init_array | print_array | kernel_floyd_warshall | main |
|---|---:|---:|---:|---:|
| assign | 500501 | 501 | 125250501 | 2 |
| add | 1000000 | 250000 | 250000000 | 2 |
| sub | 0 | 0 | 0 | 0 |
| mul | 250000 | 0 | 0 | 0 |
| mul_const | 0 | 250000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 1000000 | 250000 | 0 | 0 |
| cmp | 750000 | 250000 | 125000000 | 1 |
| logical | 500000 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 250000 | 250000 | 125000000 | 1 |
| loop_for | 250500 | 250500 | 125250500 | 0 |
| call | 0 | 500004 | 0 | 6 |

### Functions for nussinov

| Operation | init_array | print_array | kernel_nussinov | main |
|---|---:|---:|---:|---:|
| assign | 251002 | 502 | 501 | 3 |
| add | 500 | 0 | 500 | 3 |
| sub | 0 | 0 | 1 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 0 | 0 | 0 | 0 |
| mod | 500 | 0 | 0 | 0 |
| cmp | 0 | 0 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 0 | 0 | 1 |
| loop_for | 251000 | 500 | 500 | 0 |
| call | 0 | 4 | 0 | 8 |

### Functions for adi

| Operation | init_array | print_array | kernel_adi | main |
|---|---:|---:|---:|---:|
| assign | 40201 | 201 | 23760214 | 6 |
| add | 40000 | 40000 | 54885602 | 8 |
| sub | 40000 | 0 | 55044200 | 0 |
| mul | 0 | 0 | 7840800 | 0 |
| mul_const | 0 | 40000 | 54885604 | 4 |
| div | 0 | 0 | 15681600 | 0 |
| div_const | 40000 | 0 | 7 | 0 |
| mod | 0 | 40000 | 0 | 0 |
| cmp | 0 | 40000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 15681602 | 11 |
| if | 0 | 40000 | 0 | 1 |
| loop_for | 40200 | 40200 | 15721300 | 0 |
| call | 0 | 80004 | 0 | 12 |

### Functions for fdtd-2d

| Operation | init_array | print_array | kernel_fdtd_2d | main |
|---|---:|---:|---:|---:|
| assign | 144302 | 603 | 14396301 | 7 |
| add | 144000 | 144000 | 14268300 | 7 |
| sub | 0 | 0 | 47732300 | 0 |
| mul | 144000 | 0 | 0 | 0 |
| mul_const | 0 | 144000 | 14312100 | 3 |
| div | 0 | 0 | 0 | 0 |
| div_const | 144000 | 0 | 0 | 0 |
| mod | 0 | 144000 | 0 | 0 |
| cmp | 0 | 144000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 16 |
| if | 0 | 144000 | 0 | 1 |
| loop_for | 48300 | 144600 | 14396000 | 0 |
| call | 0 | 288008 | 0 | 12 |

### Functions for heat-3d

| Operation | init_array | print_array | kernel_heat_3d | main |
|---|---:|---:|---:|---:|
| assign | 129641 | 1641 | 11271001 | 4 |
| add | 128000 | 128000 | 98769600 | 6 |
| sub | 64000 | 0 | 77413800 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 64000 | 192000 | 65846400 | 4 |
| div | 0 | 0 | 0 | 0 |
| div_const | 64000 | 0 | 0 | 0 |
| mod | 0 | 64000 | 0 | 0 |
| cmp | 0 | 64000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 64000 | 0 | 1 |
| loop_for | 65640 | 65640 | 11270900 | 0 |
| call | 0 | 128004 | 0 | 7 |

### Functions for jacobi-1d

| Operation | init_array | print_array | kernel_jacobi_1d | main |
|---|---:|---:|---:|---:|
| assign | 801 | 1 | 79801 | 4 |
| add | 800 | 0 | 238800 | 2 |
| sub | 0 | 0 | 159400 | 0 |
| mul | 0 | 0 | 0 | 0 |
| mul_const | 0 | 0 | 79600 | 0 |
| div | 0 | 0 | 0 | 0 |
| div_const | 800 | 0 | 0 | 0 |
| mod | 0 | 400 | 0 | 0 |
| cmp | 0 | 400 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 400 | 0 | 1 |
| loop_for | 400 | 400 | 79700 | 0 |
| call | 0 | 804 | 0 | 8 |

### Functions for jacobi-2d

| Operation | init_array | print_array | kernel_jacobi_2d | main |
|---|---:|---:|---:|---:|
| assign | 125251 | 251 | 12350601 | 4 |
| add | 250000 | 62500 | 73804800 | 4 |
| sub | 0 | 0 | 37001800 | 0 |
| mul | 125000 | 0 | 0 | 0 |
| mul_const | 0 | 62500 | 12300800 | 2 |
| div | 0 | 0 | 0 | 0 |
| div_const | 125000 | 0 | 0 | 0 |
| mod | 0 | 62500 | 0 | 0 |
| cmp | 0 | 62500 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 8 |
| if | 0 | 62500 | 0 | 1 |
| loop_for | 62750 | 62750 | 12350500 | 0 |
| call | 0 | 125004 | 0 | 8 |

### Functions for seidel-2d

| Operation | init_array | print_array | kernel_seidel_2d | main |
|---|---:|---:|---:|---:|
| assign | 160401 | 401 | 15880301 | 3 |
| add | 320000 | 160000 | 221765600 | 2 |
| sub | 0 | 0 | 110962601 | 0 |
| mul | 160000 | 0 | 0 | 0 |
| mul_const | 0 | 160000 | 0 | 1 |
| div | 0 | 0 | 0 | 0 |
| div_const | 160000 | 0 | 15840400 | 0 |
| mod | 0 | 160000 | 0 | 0 |
| cmp | 0 | 160000 | 0 | 1 |
| logical | 0 | 0 | 0 | 1 |
| bitwise | 0 | 0 | 0 | 0 |
| unary | 0 | 0 | 0 | 5 |
| if | 0 | 160000 | 0 | 1 |
| loop_for | 160400 | 160400 | 15880300 | 0 |
| call | 0 | 320004 | 0 | 6 |

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

- correlation: [datamining/correlation/correlation.operations.MEDIUM.md](datamining/correlation/correlation.operations.MEDIUM.md), [datamining/correlation/correlation.operations.MEDIUM.pdf](datamining/correlation/correlation.operations.MEDIUM.pdf)
- covariance: [datamining/covariance/covariance.operations.MEDIUM.md](datamining/covariance/covariance.operations.MEDIUM.md), [datamining/covariance/covariance.operations.MEDIUM.pdf](datamining/covariance/covariance.operations.MEDIUM.pdf)
- case01: [dummy_tests/case01/case01.operations.MEDIUM.md](dummy_tests/case01/case01.operations.MEDIUM.md), [dummy_tests/case01/case01.operations.MEDIUM.pdf](dummy_tests/case01/case01.operations.MEDIUM.pdf)
- case02: [dummy_tests/case02/case02.operations.MEDIUM.md](dummy_tests/case02/case02.operations.MEDIUM.md), [dummy_tests/case02/case02.operations.MEDIUM.pdf](dummy_tests/case02/case02.operations.MEDIUM.pdf)
- case03: [dummy_tests/case03/case03.operations.MEDIUM.md](dummy_tests/case03/case03.operations.MEDIUM.md), [dummy_tests/case03/case03.operations.MEDIUM.pdf](dummy_tests/case03/case03.operations.MEDIUM.pdf)
- case04: [dummy_tests/case04/case04.operations.MEDIUM.md](dummy_tests/case04/case04.operations.MEDIUM.md), [dummy_tests/case04/case04.operations.MEDIUM.pdf](dummy_tests/case04/case04.operations.MEDIUM.pdf)
- case05: [dummy_tests/case05/case05.operations.MEDIUM.md](dummy_tests/case05/case05.operations.MEDIUM.md), [dummy_tests/case05/case05.operations.MEDIUM.pdf](dummy_tests/case05/case05.operations.MEDIUM.pdf)
- case06: [dummy_tests/case06/case06.operations.MEDIUM.md](dummy_tests/case06/case06.operations.MEDIUM.md), [dummy_tests/case06/case06.operations.MEDIUM.pdf](dummy_tests/case06/case06.operations.MEDIUM.pdf)
- case07: [dummy_tests/case07/case07.operations.MEDIUM.md](dummy_tests/case07/case07.operations.MEDIUM.md), [dummy_tests/case07/case07.operations.MEDIUM.pdf](dummy_tests/case07/case07.operations.MEDIUM.pdf)
- case08: [dummy_tests/case08/case08.operations.MEDIUM.md](dummy_tests/case08/case08.operations.MEDIUM.md), [dummy_tests/case08/case08.operations.MEDIUM.pdf](dummy_tests/case08/case08.operations.MEDIUM.pdf)
- case09: [dummy_tests/case09/case09.operations.MEDIUM.md](dummy_tests/case09/case09.operations.MEDIUM.md), [dummy_tests/case09/case09.operations.MEDIUM.pdf](dummy_tests/case09/case09.operations.MEDIUM.pdf)
- case10: [dummy_tests/case10/case10.operations.MEDIUM.md](dummy_tests/case10/case10.operations.MEDIUM.md), [dummy_tests/case10/case10.operations.MEDIUM.pdf](dummy_tests/case10/case10.operations.MEDIUM.pdf)
- gemm: [linear-algebra/blas/gemm/gemm.operations.MEDIUM.md](linear-algebra/blas/gemm/gemm.operations.MEDIUM.md), [linear-algebra/blas/gemm/gemm.operations.MEDIUM.pdf](linear-algebra/blas/gemm/gemm.operations.MEDIUM.pdf)
- gemver: [linear-algebra/blas/gemver/gemver.operations.MEDIUM.md](linear-algebra/blas/gemver/gemver.operations.MEDIUM.md), [linear-algebra/blas/gemver/gemver.operations.MEDIUM.pdf](linear-algebra/blas/gemver/gemver.operations.MEDIUM.pdf)
- gesummv: [linear-algebra/blas/gesummv/gesummv.operations.MEDIUM.md](linear-algebra/blas/gesummv/gesummv.operations.MEDIUM.md), [linear-algebra/blas/gesummv/gesummv.operations.MEDIUM.pdf](linear-algebra/blas/gesummv/gesummv.operations.MEDIUM.pdf)
- symm: [linear-algebra/blas/symm/symm.operations.MEDIUM.md](linear-algebra/blas/symm/symm.operations.MEDIUM.md), [linear-algebra/blas/symm/symm.operations.MEDIUM.pdf](linear-algebra/blas/symm/symm.operations.MEDIUM.pdf)
- syr2k: [linear-algebra/blas/syr2k/syr2k.operations.MEDIUM.md](linear-algebra/blas/syr2k/syr2k.operations.MEDIUM.md), [linear-algebra/blas/syr2k/syr2k.operations.MEDIUM.pdf](linear-algebra/blas/syr2k/syr2k.operations.MEDIUM.pdf)
- syrk: [linear-algebra/blas/syrk/syrk.operations.MEDIUM.md](linear-algebra/blas/syrk/syrk.operations.MEDIUM.md), [linear-algebra/blas/syrk/syrk.operations.MEDIUM.pdf](linear-algebra/blas/syrk/syrk.operations.MEDIUM.pdf)
- trmm: [linear-algebra/blas/trmm/trmm.operations.MEDIUM.md](linear-algebra/blas/trmm/trmm.operations.MEDIUM.md), [linear-algebra/blas/trmm/trmm.operations.MEDIUM.pdf](linear-algebra/blas/trmm/trmm.operations.MEDIUM.pdf)
- 2mm: [linear-algebra/kernels/2mm/2mm.operations.MEDIUM.md](linear-algebra/kernels/2mm/2mm.operations.MEDIUM.md), [linear-algebra/kernels/2mm/2mm.operations.MEDIUM.pdf](linear-algebra/kernels/2mm/2mm.operations.MEDIUM.pdf)
- 3mm: [linear-algebra/kernels/3mm/3mm.operations.MEDIUM.md](linear-algebra/kernels/3mm/3mm.operations.MEDIUM.md), [linear-algebra/kernels/3mm/3mm.operations.MEDIUM.pdf](linear-algebra/kernels/3mm/3mm.operations.MEDIUM.pdf)
- atax: [linear-algebra/kernels/atax/atax.operations.MEDIUM.md](linear-algebra/kernels/atax/atax.operations.MEDIUM.md), [linear-algebra/kernels/atax/atax.operations.MEDIUM.pdf](linear-algebra/kernels/atax/atax.operations.MEDIUM.pdf)
- bicg: [linear-algebra/kernels/bicg/bicg.operations.MEDIUM.md](linear-algebra/kernels/bicg/bicg.operations.MEDIUM.md), [linear-algebra/kernels/bicg/bicg.operations.MEDIUM.pdf](linear-algebra/kernels/bicg/bicg.operations.MEDIUM.pdf)
- doitgen: [linear-algebra/kernels/doitgen/doitgen.operations.MEDIUM.md](linear-algebra/kernels/doitgen/doitgen.operations.MEDIUM.md), [linear-algebra/kernels/doitgen/doitgen.operations.MEDIUM.pdf](linear-algebra/kernels/doitgen/doitgen.operations.MEDIUM.pdf)
- mvt: [linear-algebra/kernels/mvt/mvt.operations.MEDIUM.md](linear-algebra/kernels/mvt/mvt.operations.MEDIUM.md), [linear-algebra/kernels/mvt/mvt.operations.MEDIUM.pdf](linear-algebra/kernels/mvt/mvt.operations.MEDIUM.pdf)
- cholesky: [linear-algebra/solvers/cholesky/cholesky.operations.MEDIUM.md](linear-algebra/solvers/cholesky/cholesky.operations.MEDIUM.md), [linear-algebra/solvers/cholesky/cholesky.operations.MEDIUM.pdf](linear-algebra/solvers/cholesky/cholesky.operations.MEDIUM.pdf)
- durbin: [linear-algebra/solvers/durbin/durbin.operations.MEDIUM.md](linear-algebra/solvers/durbin/durbin.operations.MEDIUM.md), [linear-algebra/solvers/durbin/durbin.operations.MEDIUM.pdf](linear-algebra/solvers/durbin/durbin.operations.MEDIUM.pdf)
- gramschmidt: [linear-algebra/solvers/gramschmidt/gramschmidt.operations.MEDIUM.md](linear-algebra/solvers/gramschmidt/gramschmidt.operations.MEDIUM.md), [linear-algebra/solvers/gramschmidt/gramschmidt.operations.MEDIUM.pdf](linear-algebra/solvers/gramschmidt/gramschmidt.operations.MEDIUM.pdf)
- lu: [linear-algebra/solvers/lu/lu.operations.MEDIUM.md](linear-algebra/solvers/lu/lu.operations.MEDIUM.md), [linear-algebra/solvers/lu/lu.operations.MEDIUM.pdf](linear-algebra/solvers/lu/lu.operations.MEDIUM.pdf)
- ludcmp: [linear-algebra/solvers/ludcmp/ludcmp.operations.MEDIUM.md](linear-algebra/solvers/ludcmp/ludcmp.operations.MEDIUM.md), [linear-algebra/solvers/ludcmp/ludcmp.operations.MEDIUM.pdf](linear-algebra/solvers/ludcmp/ludcmp.operations.MEDIUM.pdf)
- trisolv: [linear-algebra/solvers/trisolv/trisolv.operations.MEDIUM.md](linear-algebra/solvers/trisolv/trisolv.operations.MEDIUM.md), [linear-algebra/solvers/trisolv/trisolv.operations.MEDIUM.pdf](linear-algebra/solvers/trisolv/trisolv.operations.MEDIUM.pdf)
- deriche: [medley/deriche/deriche.operations.MEDIUM.md](medley/deriche/deriche.operations.MEDIUM.md), [medley/deriche/deriche.operations.MEDIUM.pdf](medley/deriche/deriche.operations.MEDIUM.pdf)
- floyd-warshall: [medley/floyd-warshall/floyd-warshall.operations.MEDIUM.md](medley/floyd-warshall/floyd-warshall.operations.MEDIUM.md), [medley/floyd-warshall/floyd-warshall.operations.MEDIUM.pdf](medley/floyd-warshall/floyd-warshall.operations.MEDIUM.pdf)
- nussinov: [medley/nussinov/nussinov.operations.MEDIUM.md](medley/nussinov/nussinov.operations.MEDIUM.md), [medley/nussinov/nussinov.operations.MEDIUM.pdf](medley/nussinov/nussinov.operations.MEDIUM.pdf)
- adi: [stencils/adi/adi.operations.MEDIUM.md](stencils/adi/adi.operations.MEDIUM.md), [stencils/adi/adi.operations.MEDIUM.pdf](stencils/adi/adi.operations.MEDIUM.pdf)
- fdtd-2d: [stencils/fdtd-2d/fdtd-2d.operations.MEDIUM.md](stencils/fdtd-2d/fdtd-2d.operations.MEDIUM.md), [stencils/fdtd-2d/fdtd-2d.operations.MEDIUM.pdf](stencils/fdtd-2d/fdtd-2d.operations.MEDIUM.pdf)
- heat-3d: [stencils/heat-3d/heat-3d.operations.MEDIUM.md](stencils/heat-3d/heat-3d.operations.MEDIUM.md), [stencils/heat-3d/heat-3d.operations.MEDIUM.pdf](stencils/heat-3d/heat-3d.operations.MEDIUM.pdf)
- jacobi-1d: [stencils/jacobi-1d/jacobi-1d.operations.MEDIUM.md](stencils/jacobi-1d/jacobi-1d.operations.MEDIUM.md), [stencils/jacobi-1d/jacobi-1d.operations.MEDIUM.pdf](stencils/jacobi-1d/jacobi-1d.operations.MEDIUM.pdf)
- jacobi-2d: [stencils/jacobi-2d/jacobi-2d.operations.MEDIUM.md](stencils/jacobi-2d/jacobi-2d.operations.MEDIUM.md), [stencils/jacobi-2d/jacobi-2d.operations.MEDIUM.pdf](stencils/jacobi-2d/jacobi-2d.operations.MEDIUM.pdf)
- seidel-2d: [stencils/seidel-2d/seidel-2d.operations.MEDIUM.md](stencils/seidel-2d/seidel-2d.operations.MEDIUM.md), [stencils/seidel-2d/seidel-2d.operations.MEDIUM.pdf](stencils/seidel-2d/seidel-2d.operations.MEDIUM.pdf)
- polybench: [utilities/polybench.operations.MEDIUM.md](utilities/polybench.operations.MEDIUM.md), [utilities/polybench.operations.MEDIUM.pdf](utilities/polybench.operations.MEDIUM.pdf)
