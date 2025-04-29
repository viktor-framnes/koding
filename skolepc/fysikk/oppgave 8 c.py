


v = 2
s = 0.2
m = 0.4
dt = 0.01


while s > 0:
    a = 1.342-(v*0.2**4)/(6.8*10**-3)-1.29 
    v = v + a*dt
    s = s - v*dt

print(v)