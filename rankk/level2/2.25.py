# Rankk: 2.25 - Series
# woanmeo11

mod = 10**10
res = 0
for i in range(1, 923):
    res = (res + pow(i, i, mod)) % mod
print(res)
