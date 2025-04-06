"""
Klassen elev
"""

class Elev:
    def __init__(self,fornavn,faar) -> None:
        self.fornavn = fornavn
        self.faar = faar
    def __str__(self):
        return f"{self.fornavn}, født {self.faar}"

# Liste til å fylle opp med elev-objekter
klasse3G = []

# Lage mange elev-objekter med for-løkke
# for i in range(30):
    # elev = Elev(f"elev{i}",i+2000)
    # klasse3G.append(elev)

def legg_til(navn,faar):
    klasse3G.append(Elev(navn,faar))