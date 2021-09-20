# Cryptohack - RSA Starter 4
# woanmeo11

def extended_gcd(a, b):
    if b % a == 0:
        return (1, 0)
    x, y = extended_gcd(b, a % b)
    return (y, x - (a // b)*y)

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

phi = (p - 1) * (q - 1)
d = extended_gcd(e, phi)[0]

print(d)
