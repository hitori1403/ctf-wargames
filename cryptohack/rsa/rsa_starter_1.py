# Cryptohack - RSA Starter 1
# woanmeo11

def power(a, n, m):
    res = 1
    while n:
        if n & 1:
            res = res * a % m
        a = a * a % m
        n >>= 1
    return res

print(power(101, 17, 22663))
