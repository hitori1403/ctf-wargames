# cryptopals: Implement repeating-key XOR
# huycon

from binascii import hexlify
from itertools import cycle


def encrypt(plain: bytes, key: bytes) -> str:
    cipher = [i ^ j for i, j in zip(plain, cycle(key))]
    return hexlify(bytes(cipher)).decode()


def main():
    plain = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    print(encrypt(plain, key))


if __name__ == '__main__':
    main()