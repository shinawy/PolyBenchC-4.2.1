#include "case08.h"
static int case08_helper(int x) {
  return x + 1;
}

int case08_kernel(void) {
  int s = 0;
  for (int i = 0; i < 3; i++) {
    s = s + case08_helper(i);
  }
  return s;
}
