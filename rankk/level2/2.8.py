# Rankk: 2.8 - Prime time
# woanmeo11

import math

def is_prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
i = 2
s = 0
while n:
    if is_prime(i):
       n -= 1
       s += i
    i += 1
print(s)
