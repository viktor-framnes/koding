from pylab import*

a=3
d=4
n=0
s=0



while a<=59:
        n=n+1
        print(a, "er leddnummer", n, "i rekka")
        s=s+a
        a=a+d
        

print("Summen av de", n, "første leddene er", s)

