import numpy as np
import matplotlib.pyplot as plt

def f(x,r, k):
    return x+r*x*(k-x)


def beregn_folge(
r, 
u0, 
nmax, 
k, 
):
    u = np.zeros(nmax+1) 
    u[0] = u0
    for i in range(0, nmax):
        u[i+1] = f(u[i],r,k)
    return u 

def plott_folge(u,w):
    naturlige_tall = np.arange(0.0, len(u), 1)

    newparams = {'figure.figsize': (8.0, 4.0), 'axes.grid': True,
    'lines.markersize': 8, 'lines.linewidth': 2,
    'font.size': 14}
    plt.rcParams.update(newparams)
    plt.plot(naturlige_tall, u, 'bo') 
    plt.plot(naturlige_tall, w, 'ro') 
    plt.show()

u = beregn_folge(4,0.100,10,3/4)
w = beregn_folge(4,0.101,10,3/4)

plott_folge(u,w)

