
class Handlekurv:
    def __init__(self):
        self.innhold = []

    def leggtil(self,nft,str=""):
        Nft.nftid += 1
        if nft.tittel == "BoredMonkey":
            nft.getpris(str)
            self.innhold.append(nft)
        else:
            if DogeDog.antalligjen < 1:
                print("Det er tomt")
            else:
                self.innhold.append(nft)
                DogeDog.antalligjen -= 1

    def beregnPris(self):
        totpris = 0
        for nft in self.innhold:
            totpris += nft.pris
        return totpris

    def visinfo(self):
        x = ", ".join(self.innhold)
        print(x,end=" og koster ")
        print(f"{self.beregnPris():.2f} kr")        
            

class Nft:
    nftid = 1
    def __init__(self):
        self.nftid = Nft.nftid

class BoredMonkey(Nft):
    antalligjen = 5
    def __init__(self,tittel="BoredMonkey"):
        super().__init__()
        self.pris = 10000
        self.tittel = tittel

    def getpris(self,str):
        if str.lower() == "medium":
            self.pris = 10249
        elif str.lower() == "large":
            self.pris = 10999

class DogeDog(Nft):
    antalligjen = 1
    def __init__(self,tittel="DogeDog"):
        super().__init__()
        self.pris = 40000000
        self.tittel = tittel

    def oppdaterpris(self,pris):
        self.pris = pris


d1 = DogeDog()
d2 = DogeDog()
h = Handlekurv()
h.leggtil(d1)
h.leggtil(d2)
h.visinfo()