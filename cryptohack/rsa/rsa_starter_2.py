# Cryptohack - RSA Starter 2
# woanmeo11

m = 12
p = 17
q = 23
e = 65537

n = p * q
c = pow(m, e, n)

print(c)
