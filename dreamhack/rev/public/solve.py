from Crypto.Util.number import long_to_bytes, inverse
from ctypes import *


def power(a, x, n):
    p = 1
    for _ in range(x):
        p = (p * a & ((1 << 64) - 1)) % n
    return p


lib = cdll.LoadLibrary("./power.so")
lib.power.restype = c_ulonglong
lib.power.argtypes = [c_ulonglong] * 3

p = 65287
q = 65419
n = p * q
e = 201326609

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

with open("./out.bin", "rb") as f:
    enc = f.read()

for i in range(0, len(enc), 8):
    c = int.from_bytes(enc[i : i + 8][::-1])
    print(long_to_bytes(lib.power(c, d, n)).decode()[::-1], end="", flush=True)
