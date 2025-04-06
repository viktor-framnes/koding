
def beregn(n):
    s = 0
    for i in range(1,n):
        if i % 2 == 0:
            s += i
        else:
            s -= i
    return s
print(beregn(7))