# Cryptohack: Round Keys
# woanmeo11

from structure_of_aes import matrix2bytes

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    return [[s3 ^ k3 for s3, k3 in zip(s2, k2)] for s2, k2 in zip(s, k)]

if __name__ == '__main__':
    print(matrix2bytes(add_round_key(state, round_key)))
