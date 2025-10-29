import numpy as np
import math
# generisk iterativ fikspunktmetode
def fikspunkt(funksjon, initialverdi, toleranse = 1.0E-12, N = 500):
    følge = [initialverdi] 
    while True:
        følge.append(funksjon(følge[-1]))  # legg til funksjonsverdi av det som var sist i følgen
        if len(følge) == N: # vi avbryter etter N steg uansett
            print("Fant ikke fikspunkt for gitt startverdi Returnerer nåværende verdier.")
            return(følge)
        if abs(følge[-1]-følge[-2]) < toleranse: #abstand mellom de siste to er mindre enn toleranse
            return(følge)
        
f = lambda x: math.cos(x) 
print(len(fikspunkt(f,0.7)))

