# hax.tor.hu: level11
# woanmeo11

import requests, re, hashlib

url = 'https://hax.tor.hu/level11/'
cookies = {'HAXTOR': '58nb1hosdsah5td3hm04pgpcc7'}

r = requests.get(url, cookies=cookies, verify=False)

plain_text = re.findall('hash for: "<b>(.*)</b>', r.text)[0].replace(' ','')
answer = hashlib.md5(plain_text.encode()).hexdigest()

r = requests.get(url, params={'pw': answer}, cookies=cookies, verify=False)
