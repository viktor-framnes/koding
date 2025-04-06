
class Produksjonslinje():
    def __init__(self) -> None:
        self.produksjon = []

    def leggTilBil(self,bil):
        if bil in self.produksjon:
            return "Den er der allerde"
        else:
            self.produksjon.append(bil)

    def visProduksjonslinje(self):
        print("Produksjonslinjen består av disse bilene:")
        for i in self.produksjon:
            print(i)

class Standar():
    def __init__(self,modell:str,batteri:object,nettovekt:int,id:int) -> None:
        self.modell = modell
        self.batteri = batteri
        self.nettovekt = nettovekt
        self.id = id

    def totalVekt(self) -> int:
        totalvekt = int(self.nettovekt) + int(self.batteri.getVekt())
        return totalvekt
    
    def batteriBytte(self,batteri2):
        if batteri2.getId() == self.batteri.getId():
            return f"Det er samme batteri"
        else:
            self.batteri = batteri2
            buffer = self.batteri.getId()
            return f"Bytter batteri med id {buffer} med {self.batteri.getId()}"

    def __str__(self) -> str:
        return f"Standar bil modell {self.modell}, batteri med kapasitet {self.batteri.kapasitet} kWh og id {self.batteri.getId()}, total vekt på {self.totalVekt()} kg, nettovekt på {self.nettovekt} kg, id: {self.id} og ingen ekstrautstyr \n"
        
class Luksus(Standar):
    def __init__(self, modell, batteri, nettovekt, id,felgstr:int,skinnseter:bool,selvkjøring:bool) -> None:
        super().__init__(modell, batteri, nettovekt, id)
        self.felgstr = felgstr
        self.skinnseter = skinnseter
        self.selvkjøring = selvkjøring

    def kjørselv(self):
        return f"bilen kræsjet, ikke stol på selvkjørte biler"

    def __str__(self) -> str:
        return f"Luksus bil modell {self.modell}, batteri med kapasitet {self.batteri.kapasitet} kWh og id {self.batteri.getId()}, total vekt på {self.totalVekt()} kg, nettovekt på {self.nettovekt} kg, id: {self.id} og status på ekstra utstyr, felgestørrelse: {self.felgstr}, skinnseter: {self.skinnseter}, selvkjøring: {self.selvkjøring} \n"

class Batteri():
    def __init__(self,kapasitet:int,vekt:int,produksjonsdato:str,id:int) -> None:
        self.kapasitet = kapasitet
        self.vekt = vekt
        self.produksjonsdato = produksjonsdato
        self.id = id

    def getKapasitet(self) -> int:
        return self.kapasitet
    
    def getVekt(self) -> int:
        return self.vekt
    
    def getId(self) -> int:
        return self.id
    
def main():
    p1 = Produksjonslinje()
    p2 = Produksjonslinje()

    batteri1 = Batteri(60,500,2001,1)
    batteri2 = Batteri(100,750,2011,2)
    batteri3 = Batteri(120,1000,2020,3)
    
    bil1 = Standar("i1",batteri1,5000,1)
    bil2 = Luksus("i2",batteri2,6000,2,32,True,True)
    bil3 = Luksus("i3",batteri3,7000,3,36,False,True)
    bil4 = Standar("i4",batteri1,4000,4)
    bil5 = Standar("i5",batteri1,2000,5)

    p1.leggTilBil(bil1)
    p1.leggTilBil(bil2)
    p1.leggTilBil(bil4)
    p2.leggTilBil(bil3)
    p2.leggTilBil(bil5)

    # print(p1.leggTilBil(bil1))

    p1.visProduksjonslinje()
    print()
    # p2.visProduksjonslinje()
    # print()
    print(bil1.batteriBytte(batteri2))
    print()
    p1.visProduksjonslinje()
    # print(bil3.kjørselv())

if __name__ == "__main__":
    main()