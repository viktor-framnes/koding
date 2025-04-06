import random


class Akvarium:
    def __init__(self,l,b,h) -> None:
        self.lengde = l
        self.bredde = b
        self.hoyde = h
        self.fisker = []

    def beregnVolum(self):
        return self.lengde * self.bredde * self.hoyde
    
    def vannVolum(self):
        return self.beregnVolum() * 0.9
    
    def vannHoyde(self):
        return self.vannVolum() / (self.bredde * self.lengde)
    
    def leggtilfisk(self,fisk):
        if fisk.lengdeVoksen < self.lengde:
            self.fisker.append(fisk)
            return f"Fisken {fisk.navn} er lagt til"
        else:
            return f"Fisken passer ikke, du trenger et akvarium som er minst {fisk.lengdeVoksen} cm langt"

class Fisk:
    def __init__(self,navn,lengdeVoksen,vektVoksen,favmat) -> None:
        self.navn = navn
        self.lengdeVoksen = lengdeVoksen
        self.vektVoksen = vektVoksen
        self.favmat = favmat

    def spis(self):
        return "fisken liker å spise"
    
    def __str__(self) -> str:
        return f"navn: {self.navn}, lengde: {self.lengdeVoksen} cm, vekt: {self.vektVoksen} kg, favmat: {self.favmat}"

class Hvithai(Fisk):
    def __init__(self, navn, lengdeVoksen, vektVoksen, favmat) -> None:
        super().__init__(navn, lengdeVoksen, vektVoksen, favmat)
        self.vitenskapligNavn = "Carcharodon carcharias"

    def hoppe(self):
        return random.randint(0,1)

    def __str__(self) -> str:
        return super().__str__() + f", vitenskaplig navn: {self.vitenskapligNavn}, triks: {self.hoppe()}"

class Rognkjeks(Fisk):
    def __init__(self, navn, lengdeVoksen, vektVoksen, favmat) -> None:
        super().__init__(navn, lengdeVoksen, vektVoksen, favmat)
        self.vitenskapligNavn = "Cyclopterus lumpus"
        self.sugd = False

    def sugFast(self):
        self.sugd = not self.sugd
        return self.sugd
    
    def __str__(self) -> str:
        return super().__str__() + f", vitenskaplig navn: {self.vitenskapligNavn}, triks: {self.sugFast()}"

def main():
    ak1 = Akvarium(40,15,25)
    hai1 = Hvithai("Viktor",500,3000,"kanin")
    # print(hai1)
    rogn1 = Rognkjeks("Lester",10,5,"lus")
    # print(rogn1)
    print()
    # print(ak1.leggtilfisk(hai1))
    print(ak1.leggtilfisk(rogn1))
    print(ak1.fisker[0])
    

if __name__ == "__main__":
    main()