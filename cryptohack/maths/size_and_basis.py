# Cryptohack: Size and Basis
# woanmeo11

import math

def sqr(v):
    res = 0
    for a in v:
        res += a * a
    return res

v = (4, 6, 2, 5)
print(int(math.sqrt(sqr(v))))

