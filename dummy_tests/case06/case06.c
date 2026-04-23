#include "case06.h"
int case06_kernel(int a, int b) {
  int c = (a & b) | (a ^ b);
  if ((a > 0) && (b > 0)) {
    c = c << 1;
  }
  return c;
}
