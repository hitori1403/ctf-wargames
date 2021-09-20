# cryptopals: Single-byte XOR cipher
# huycon

import binascii, math, string


def xor_decrypt(cipher: bytes, c: str):
    c = ord(c)
    plain = []
    for x in cipher:
        plain.append(x ^ c)
    
    return bytes(plain).decode()


# a-z
ENGLISH_FREQ = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074
]


def chi_square(s: str):
    freq = [0] * 26
    for c in s:
        if c.isalpha():
            freq[ord(c.lower()) - 97] += 1
        elif c not in string.printable:
            return math.inf

    chi2 = 0
    for c in string.ascii_lowercase:
        c = ord(c) - 97
        o = freq[c]
        e = ENGLISH_FREQ[c] * len(s)
        chi2 += (o - e)**2 / e

    return chi2


def main():
    cipher = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
    cipher = binascii.unhexlify(cipher)
 
    plain = ''
    best = math.inf

    for c in string.ascii_letters:
        m = xor_decrypt(cipher, c)
        likelihood = chi_square(m)
        
        if likelihood < best:
            best = likelihood
            plain = m

    print(plain)


if __name__ == '__main__':
    main()