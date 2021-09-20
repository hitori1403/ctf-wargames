# hax.tor.hu: level7
# woanmeo11

c = 'b1 a5 93 a5 e2 a5 f6 a5 c6 a5 b6 a5 11 a5 f3 a5 32 a5'
c = c.split(' ')

for x in c:
    x = int(x, 16)
    x ^= 0xa5
    x = ((x << 4) | (x >> 4)) & 0xff
    print(chr(x), end='')
