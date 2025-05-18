# Pn-1 + 5 (n-1)


def funk(n):
    if n == 1:
        return 1
    return funk(n-1)+5*(n-1)

print(funk(100))