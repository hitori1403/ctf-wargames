# cryptopals: Detect single-character XOR
# huycon

from math import inf
from binascii import unhexlify


plain = ''
best_score = inf
# [a-z]
ENGLISH_FREQ = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074
]


def decrypt(cipher: bytes, i: int) -> bytes:
    plain = []
    for j in cipher:
        plain.append(i ^ j)
    return bytes(plain)


def get_score(cipher: bytes) -> float:
    freq = [0] * 26
    for c in cipher:
        if c != 10 and (c < 32 or 127 < c):
            return inf
        if 65 <= c and c <= 90:
            freq[c - 65] += 1
        elif 97 <= c and c <= 122:
            freq[c - 97] += 1
        
    differ = 0
    for i in range(26):
        o = freq[i]
        e = ENGLISH_FREQ[i]
        differ += abs(o/len(cipher) - e)

    return differ


def brute_xor(cipher: bytes):
    global plain, best_score
    cipher = unhexlify(cipher)

    for i in range(32, 127):
        m = decrypt(cipher, i)
        score = get_score(m)

        if score < best_score:
            best_score = score
            plain = m


def main():
    with open('4.txt', 'rb') as reader:
        for line in reader.readlines():
            brute_xor(line.strip())

    print(plain.decode())


if __name__ == '__main__':
    main()