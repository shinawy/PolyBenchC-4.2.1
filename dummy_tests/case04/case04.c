#include "case04.h"
int case04_kernel(void) {
  int sum = 0;
  for (int i = 0; i < 4; i++) {
    sum += i;
  }
  return sum;
}
