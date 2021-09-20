# Wechall: Prime Factory
# woanmeo11

import math

def sum_digit(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

cnt = 0
i = 1000000
while cnt < 2:
    if is_prime(i) and is_prime(sum_digit(i)):
        print(i, end='')
        cnt += 1
    i += 1
 
