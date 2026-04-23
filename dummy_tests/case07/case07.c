#include "case07.h"
int case07_kernel(int a) {
  int b = -a;
  int c = a / 2;
  int d = a % 3;
  return b + c + d;
}
