


v = 0
s = 1000*10**3
gamma = 6.67*10**-11
m = 7.35*10**22
r = s + 1737*10**3
dt = 0.01

while s > 0:
    a = gamma*(m/r**2)
    v = v + a*dt
    s = s - v*dt

print(v)