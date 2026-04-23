#include "case03.h"
int case03_kernel(int a, int b) {
  int c = 0;
  if (a > b) {
    c = a - b;
  } else {
    c = b - a;
  }
  return c;
}
