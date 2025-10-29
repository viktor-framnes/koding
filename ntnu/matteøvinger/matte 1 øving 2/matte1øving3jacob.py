import numpy as np

# generisk iterativ fikspunktmetode
def jacobi(A, b, a, toleranse = 1.0E-12, K = 500):
    n = a.size               # antall elementer i a_0
    D = np.diag(A)*np.eye(n) # lager diagonalmatrisa
    Dinv = np.linalg.inv(D)  # lager inversen til diagonalmatrisa, dette er ikke dyrt siden den er diagonal
    L = np.tril(A,-1)        # lager L-matrisa
    U = np.triu(A,1)         # lager U-matrisa
    k = 0
    
    r = b-A@a # her bruker vi en annen notasjon for matrisemultiplikasjon når vi regner ut r
    feil = np.linalg.norm(r,ord=np.inf) # vi måler forskjellen mellom Ax og b i sup-normen
    
    while feil >= toleranse and k < K: # vi gjør dette mens ||Ax-b||>=toleranse og k<K
        a = Dinv@(b-(L+U)@a) # ny initialverdi
        k = k+1    # ny k
        r = b-A@a  # ny r
        feil = np.linalg.norm(r,ord=np.inf) # ny err
    if k >= K:
        print("Fant ikke fikspunkt for gitt startverdi. Returnerer nåværende verdier.")
        return a, feil, k
    else: 
        return a, feil, k
    
# definerer matrisa, høyresida og initialvektoren vi skal bruke
A1 = np.array([[9.,2.,-1.],[1.,8.,1.],[3.,2.,6.]])
b1 = np.array([[3.],[5.],[4.]]) # b som kolonnevektor 
a1 = np.array([[0.],[0.],[0.]]) # a0 som kolonnevektor

# finner fikspunkt med gitt initialvektor
a, feil, k = jacobi(A1, b1, a1)

print(f"Løsning: {a}")
print(f"Feil: {feil}")
print(f"Iterasjoner: {k}")