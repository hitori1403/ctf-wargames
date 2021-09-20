# Mod-x: level 2
# woanmeo11

c = ''
with open('the_FILE.enc') as f:
    c = f.read()

for i in range(255):
    m = ''
    k = ord(c[0]) - i
    try:
        for x in c:
            m += chr(ord(x) - k)
    except:
        continue
    if m.isascii():
        print(m)
