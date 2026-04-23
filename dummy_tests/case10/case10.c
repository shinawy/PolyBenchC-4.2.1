#include "case10.h"
int case10_kernel(void) {
  int x = 0;
  for (int i = 0; i < CASE10_N; i++) {
    x += i * CASE10_SCALE;
  }
  return x;
}
