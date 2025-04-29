from pylab import*

def rekke(n):
    if n==1:
        return 2
    else: 
        return rekke(n-1)+5+(3*(n-2))

a = 0
for i in range(1,11):
    a += rekke(i)
    print(a, i)