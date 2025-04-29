
class Handlekurv:
    def __init__(self):
        self.innhold = []
        self.totalsum = 0

    def leggtil(self,nft):
        self.innhold.append(nft)
        self.totalsum += nft.pris

    def visinfo(self):
        for obj in self.innhold:
            print(obj)
        print(f"Total sum: {self.totalsum:.2f} kr")

class Nft:
    idtall = 0
    def __init__(self,tittel,artistnavn,eier):
        self.id = Nft.idtall
        Nft.idtall += 1
        self.pris = 0
        self.tittel = tittel
        self.artistnavn = artistnavn
        self.eier = eier

    def __str__(self):
        return f"{self.tittel} av {self.artistnavn} (id:{self.id}), eier: {self.eier}, pris: {self.pris:.2f} kr"


class DogeDog(Nft):
    antalligjen = 1

    def __new__(cls,eier):
        if cls.antalligjen > 0:
            cls.antalligjen -= 1
            return super().__new__(cls)
        else:
            print("Det finnes ikke noen ledige DogeDog igjen!")
            return None # hinder at objektet blir opprettet


    def __init__(self,eier):
        super().__init__("DogeDog","Roger",eier)
        self.pris = 40000000

    def oppdaterPris(self,pris):
        self.pris = pris
        # from random import random
        # self.varier_pris = ( 1+random() ) * self.varier_pris # Funksjon skal f.eks. gå på internett for å hente oppdatert pris. Eller beregne pris basert på en spesiell algoritme som gjort her.
        # self.pris = self.varier_pris

    def __str__(self):
        return f"{super().__str__()}, {DogeDog.antalligjen} igjen."

class BoredMonkey(Nft):
    antalligjen = 5

    def __new__(cls,eier,størrelse):
        if cls.antalligjen > 0:
            cls.antalligjen -= 1
            return super().__new__(cls)
        else:
            print("Det finnes ingen ledige BoredMonkey igjen")
            return None

    def __init__(self, eier, størrelse):
        super().__init__("BoredMonkey", "Svein", eier)
        self.pris = 10000
        self.størrelse = størrelse.lower()

        self.beregnPris()

    def beregnPris(self):
        if self.størrelse == "small":
            self.pris = self.pris
        elif self.størrelse == "medium":
            self.pris += 249
        elif self.størrelse == "large":
            self.pris += 999

    def __str__(self):
        return f"{super().__str__()}, størrelse: {self.størrelse}, {self.antalligjen} igjen."


h = Handlekurv()
d1 = DogeDog("Viktor")
d2 = DogeDog("Viktor")
b1 = BoredMonkey("Viktor","small")
b2 = BoredMonkey("Viktor","medium")
b3 = BoredMonkey("Viktor","large")
h.leggtil(d1)
h.leggtil(b1)
h.leggtil(b2)
h.leggtil(b3)
h.visinfo()
