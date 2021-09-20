# Hackthissite: Realistic 6
# woanmeo11

from string import ascii_letters

c = []
with open('cipher.txt', 'r') as f:
    c = f.read().replace('\n', '').split('.')

c = [int(x) for x in c[1:]]
c = [sum(c[i:i + 3]) for i in range(0, len(c), 3)]

for m in ascii_letters:
    plain = ''
    k = c[0] - ord(m)
    try:
        for x in c:
            plain += chr(x - k)
    except:
        continue
    print(k, plain, '\n')
