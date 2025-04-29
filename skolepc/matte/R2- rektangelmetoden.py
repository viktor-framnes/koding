# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 10:52:53 2023

@author: ingrik1404
"""
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
    rektangel=f(x)*delta_x
    areal=areal+rektangel
    x=x+delta_x

print("Arealet blir tilnærmet lik",areal)

