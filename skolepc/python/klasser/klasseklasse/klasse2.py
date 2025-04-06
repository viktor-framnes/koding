from Elev import Elev


class Klasse:
    def __init__(self,navn) -> None:
        self.navn = navn
        self.elever = []
    def legg_til(self,elevobjekt):
        self.elever.append(elevobjekt)

kl3G = Klasse("3G")
elev = Elev("Viktor",2006)
kl3G.legg_til(elev) # printer ut alle elevene i listen