# ThisisLegal: Programming Challenge 1
# woanmeo11

import requests, re

url1 = 'https://thisislegal.com/includes/randCode.php'
url2 = 'https://thisislegal.com/challenge/programming/1'
cookies = {'PHPSESSID': 'ot0ja5ondqrjli4e0esfv56efi'}

r = requests.get(url1, cookies=cookies)
code = re.findall(': (.*) \.', r.text)[0]

r = requests.get(url2 + '/' + code, cookies=cookies)
print(r.text)
