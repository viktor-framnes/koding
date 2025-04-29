from pylab import*


def f(x):
    return x**2-1

a=-2
b=2
n=1000

delta_x=(b-a)/n
areal=0
x=a

for i in range(n):
    y=f(x)
    trapes=(f(x)+f(x+delta_x))/2*delta_x
    areal=areal+trapes
    x=x+delta_x


print("Arealet blir tilnærmet lik",areal)