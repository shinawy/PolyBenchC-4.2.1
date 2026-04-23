#include "case05.h"
int case05_kernel(void) {
  int s = 0;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
      s += i * j;
    }
  }
  return s;
}
