# Cryptohack: Gram Schmidt
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

v = [ (4,1,3,-1), (2,1,-3,4), (1,0,-2,7), (6, 2, 9, -5) ]
u = []

for i in range(4):
    u.append(v[i])
    for j in range(i):
        m = dot(v[i], u[j]) / dot(u[j], u[j])
        u[i] = sub(u[i], mul(m, u[j]))

print('%.5f'%u[3][1])
