class Handlekurv:
    def __init__(self):
        self.innhold = []

    def leggtil(self,nft):
        if DogeDog.antalligjen > 0:
            self.innhold.append(nft)
            Nft.idtall += 1
            DogeDog -= 1
        else:
            print("det er ikke flere igjen")

    def fjern(self):
        pass

    def totpris(self):
        totpris = 0
        for nft in self.innhold:
            totpris += nft.getpris()
        return totpris 

    def visinfo(self):
        return f"Handlelisten: {self.innhold} og koster {self.getpris} kr"

class Nft:
    idtall = 0
    def __init__(self):
        self.id = Nft.idtall
        self.pris = 0
        self.tittel = ""
        self.artistnavn = ""
        self.eier = ""

class DogeDog(Nft):
    antalligjen = 1
    def __init__(self,eier):
        super().__init__()
        self.pris = 40000000
        self.tittel = "DogeDog"
        self.artistnavn = "Roger"
        self.eier = eier

    def oppdaterpris(self,pris):
        self.pris = pris


d1 = DogeDog("viktor")
h = Handlekurv()
h.leggtil(d1)
h.visinfo()
