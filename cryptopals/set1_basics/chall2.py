# cryptopals: Fixed XOR
# huycon

from binascii import hexlify, unhexlify

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

a = unhexlify(a)
b = unhexlify(b)

c = bytes(i ^ j for i, j in zip(a, b))
c = hexlify(c)

print(c.decode())