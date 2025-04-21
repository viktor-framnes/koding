from pylab import *

m = 0.4
L = 0.3
R = 1.5
F = 5.0
B = 2.5
t = 0
v = 0
dt = 0.001
x = []
y = []
s = 0

while s<L:
    a = F/m-(v*B**2*L**2)/(R*m)
    v = v + a*dt
    s = v*t
    t = t + dt
    x.append(t)
    y.append(a)

plot(x,y)
xlabel("Tid i sekunder")
ylabel("Akselerasjon i m/s^2")
show()
