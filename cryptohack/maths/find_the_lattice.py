from Crypto.Util.number import inverse, long_to_bytes

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

q, h = (7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800)
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

u = (1, h)
v = (0, q)

while True:
    if dot(v, v) < dot(u, u):
        u, v = v, u
    m = dot(u, v) // dot(u, u)
    if m == 0:
        break
    v = sub(v, mul(m, u))

f, g = u

def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

print(long_to_bytes(decrypt(q, h, f, g, e)))

v = vector([1, 2])
print(v)
