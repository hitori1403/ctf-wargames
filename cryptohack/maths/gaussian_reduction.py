# Cryptohack: Gaussian Reduction
# woanmeo11

def sub(u, v):
    w = []
    for a, b in zip(u, v):
        w.append(a - b)
    return w

def mul(k, v):
    w = []
    for a in v:
        w.append(k * a)
    return w 

def dot(u, v):
    res = 0
    for a, b in zip(u, v):
        res += a * b
    return res

v = (846835985, 9834798552)
u = (87502093, 123094980)

while True:
    if dot(v, v) < dot(u, u):
        u, v = v, u
    m = dot(u, v) // dot(u, u)
    if m == 0:
        break
    v = sub(v, mul(m, u))

print(dot(u, v))
