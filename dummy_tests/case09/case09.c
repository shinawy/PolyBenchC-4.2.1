#include "case09.h"
int case09_kernel(void) {
  int arr[4] = {1, 2, 3, 4};
  int s = 0;
  for (int i = 0; i < 4; i++) {
    s += arr[i];
  }
  return s;
}
