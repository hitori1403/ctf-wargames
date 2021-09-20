# Defendtheweb: Captcha 1
# woanmeo11

import requests, cv2, pytesseract, re

sess = requests.Session()
sess.post('https://defendtheweb.net/auth', data={'username': 'woanmeo11', 'password': ''})

while True:
    response = sess.get('https://defendtheweb.net/playground/captcha1')

    token = re.findall('token" value="(.*)" maxlength', response.text)[1]
    image = sess.get('https://defendtheweb.net/extras/playground/captcha/captcha1.php')

    with open('img.png', 'wb') as f:
        f.write(image.content)

    image = cv2.imread('img.png')
    captcha = pytesseract.image_to_string(image)

    captcha = captcha.replace(' ', '')[::-1][2:]
    response = sess.post('https://defendtheweb.net/playground/captcha1', data={'token': token, 'answer': captcha})

    print(captcha)
    if 'Congratulations' in response.text:
        print('ok')
        break
    else:
        print('fail')
