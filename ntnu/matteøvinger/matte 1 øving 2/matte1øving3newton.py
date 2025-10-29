import numpy as np
import math
# generisk newtons metode
def newton(F, dF, a, toleranse = 1.0E-3, N = 500):
    Fa = F(a)
    dFa = dF(a)
    n = 0
    punkter = [(a, Fa)] 
    while abs(Fa-0) >= toleranse and n < N: # vi gjor dette mens |F(x)-0|>=toleranse og n<N
        a = a-Fa/dFa   # ny initialverdi
        n = n+1        # ny n
        Fa = F(a)      # ny F(x)
        dFa = dF(a)    # ny dF(x)
        punkter.append((a, Fa))
    if n >= N:
        print("Fant ikke fikspunkt for gitt startverdi. Returnerer naavaerende verdier.")
        return punkter
    else: 
        return punkter
    
    
# definerer funksjonen vi skal bruke
def F(x):
    return (9*(x**3))+(7*x)-math.e**(-2)*(x**7) # vi bruker f(x)

def dF(x):
    return 14*math.e**((-2)*(x**7))*(x**6)*(math.log(math.e))+27*x**2+7 # vi bruker f'(x)

a_0 = 2 # en mulig initialverdi

# finner fikspunkt med gitt initialverdi
punkter = newton(F, dF, a_0)

# skriver ut punkter
n = 0
for punkt in punkter:
    print("n = {:3d},\t x = {:1.15f},\t F(x) = {:1.15f}".format(n,*punkt))
    n = n+1