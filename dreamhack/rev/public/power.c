#include <stdint.h>

unsigned long long power(unsigned long long a, unsigned long long x,
                         unsigned long long n) {
  unsigned long long p = 1;
  for (int i = 0; i < x; ++i) {
    p = p * a % n;
  }
  return p;
}
