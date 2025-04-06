

def paaske(aar):
    a = aar % 19
    b = aar // 100
    c = aar % 100
    d = b // 4
    e = b % 4
    f = (b+8) // 25
    g = (b-f+1) // 3
    h = (19*a+b-d-g+15) % 30
    i = c // 4
    k = c % 4
    l = (32+2*e+2*i-h-k) % 7
    m = (a+11*h+22*l) // 451
    n = (h+l-7*m+114) // 31
    p = (h+l-7*m+114) % 31

    maander = ["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]

    return f"{p+1}.{n}.{aar}, altså {p+1}. {maander[n-1]} {aar}"

print(paaske(2020))