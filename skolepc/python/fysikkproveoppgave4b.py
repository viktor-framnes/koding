from math import *

#Konstanter i oppgaven
m=0
g=9.81
vinkel=radians(41)
my=0.3

#Startsverdier for fart,posisjon, tid
t=0
v=0
s=0
dt=0.00001


while s<3.7:
    a=g*sin(vinkel)-my*g*cos(vinkel)
    v=v+a*dt
    s=s+v*dt
    t=t+dt


print(f"{v:.1f} er farten i m/s den har når den når kanten")   