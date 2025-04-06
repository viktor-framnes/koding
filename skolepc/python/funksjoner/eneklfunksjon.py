"""
Enekl funksjon i python
"""
from math import log10

# I python må funksjoner deklareres øverst i koden

# Funksjon som beregner sum av to tall
def sum(a,b):
    # Return returnerer en ting
    return a + b

def hello_world():
    print("Hello world")

sum(1,4)
print(f"1 + 4 = {sum(1,4)}")

hello_world()

print(f"hello_world gir returverdi: {hello_world()}")

# Lag kalkulatorfunsjoner som utfører
# +, -, *, /
# og tierlogaritmen

def pluss(a,b):
    return a + b
def minus(a,b):
    return a - b
def gange(a,b):
    return a * b
def deling(a,b):
    return a/b
def log(a):
    return log10(a)