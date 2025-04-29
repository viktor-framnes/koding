from pylab import*

a=3
k=0.5
n=0
s=0

while n<8:
        n=n+1
        #print(a, "er leddnummer", n, "i rekka")
        s=s+a
        a=a*k

       
print("Summen av de", n, "første leddene er", s)


