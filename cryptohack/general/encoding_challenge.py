# Cryptohack: Encoding Challenge
# woanmeo11

import base64
import binascii
import codecs
import json

from pwn import *
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode(method, cipher):
    if method == 'base64':
        return base64.b64decode(cipher).decode()
    elif method == 'hex':
        return binascii.unhexlify(cipher).decode()
    elif method == 'rot13':
        return codecs.encode(cipher, 'rot_13')
    elif method == 'bigint':
        return long_to_bytes(int(cipher[2:], 16)).decode()
    elif method == 'utf-8':
        return ''.join([ chr(c) for c in cipher ])

while True:
    received = json_recv()
    print(json.dumps(received))
    
    if 'flag' in received:
        break

    method = received["type"]
    cipher = received["encoded"]
    to_send = { "decoded": decode(method, cipher) }

    json_send(to_send)
    print(json.dumps(to_send))
    print()

