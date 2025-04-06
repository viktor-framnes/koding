teller = 0
for i in range(0,999):
    h = i #int(input())
    t = h
    s = 0
    r = 0
    while h != 0:
        r = h % 10
        s = s * 10 + r
        h = h // 10
    if t == s:
        print(True, t)
        teller += 1
    else:
        print(False, t)
print(teller)