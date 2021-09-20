# Wechall: Training: Programming 1
# woanmeo11

import requests

url = 'http://www.wechall.net/challenge/training/programming1/index.php?action=request'
cookie = dict(WC = '13273756-58714-32q8rdENXH1fwZhv') # get from browser (cookie extensions)
r = requests.get(url, cookies = cookie)

key = r.text
url = 'http://www.wechall.net/challenge/training/programming1/index.php?answer='
r = requests.get(url + key, cookies = cookie)
