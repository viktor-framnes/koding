from pylab import *

g = 9.81
v = 0
t = 0
dt = 0.1
vinkel = radians(30)

while t < 3:
    a = g*sin(vinkel)
    v = v+a*dt
    t + t+dt

print(v)