import numpy as np
import matplotlib.pyplot as plt

def f(x,r):
    return (1+r)*x

def beregn_folge(
r, 
u0, 
nmax 
):
    u = np.zeros(nmax+1) 
    u[0] = u0
    for i in range(0, nmax):
        u[i+1] = f(u[i],r)
    return u 

def plott_folge(u):
    naturlige_tall = np.arange(0.0, len(u), 1)
    newparams = {'figure.figsize': (8.0, 4.0), 'axes.grid': True,
    'lines.markersize': 8, 'lines.linewidth': 2,
    'font.size': 14}
    plt.rcParams.update(newparams)
    plt.plot(naturlige_tall, u, 'bo')
    plt.show()

u = beregn_folge(r=1/2, u0=1, nmax=10)
w = beregn_folge(r=0, u0=1, nmax=10)
v = beregn_folge(r=-1/2, u0=1, nmax=10)
plott_folge(u)
plott_folge(w)
plott_folge(v)
print(u)