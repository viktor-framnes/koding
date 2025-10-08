import matplotlib
import math # vi trenger tilgang til sinus-funksjonen math.sin()
import numpy as np
import matplotlib.pyplot as plt

# høyresida i rekursjonen
def f(x,r):
    return (1+r)*x
    # beregner følgen
def beregn_folge(
r, # vekstfaktor
u0, # initialverdi
nmax # antall iterasjoner
):
    u = np.zeros(nmax+1) # vi begynner med en vektor som har nuller overalt
    u[0] = u0
    for i in range(0, nmax):
        u[i+1] = f(u[i],r)
    return u # returnerer en vektor som representerer følgen
# lager plot
def plott_folge(u):
    naturlige_tall = np.arange(0.0, len(u), 1)
    # fikser litt på pyplot
    newparams = {'figure.figsize': (8.0, 4.0), 'axes.grid': True,
    'lines.markersize': 8, 'lines.linewidth': 2,
    'font.size': 14}
    plt.rcParams.update(newparams)
    plt.plot(naturlige_tall, u, 'bo') # plotter følgen for gitt vektor u
    plt.show()
    
u = beregn_folge(r=-1/2, u0=1, nmax=10)
w = beregn_folge(r=0, u0=1, nmax=10)
s = beregn_folge(r=1/2, u0=1, nmax=10)
plott_folge(u)
print(u)
plott_folge(w)
print(w)
plott_folge(s)
print(s)