# Yoire: automation/basic/1_fast_count.php
# woanmeo11

import requests, re

url = 'http://yoire.com/challenges/automation/basic/1_fast_count.php'
cookies = {'PHPSESSID': 'vm7maesian1h3q1hg3mcvecov4'}

r = requests.get(url, cookies=cookies)

content = re.findall('id=lines>(.*)</div><a name=sc>', r.text, re.DOTALL)[0]
line = content.count('\n') + 1

r = requests.post(url, cookies=cookies, data={'solution': str(line)})
print(r.text)
