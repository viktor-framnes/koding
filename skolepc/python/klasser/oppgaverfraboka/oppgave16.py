"""
Eksempel som viser arv fra én klasse til underklasser
"""
class Person:
    def __init__(self, fornavn, etternavn, alder = 18) -> None:
        """Konstruktør-metoden for klassen"""
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder

    def __str__(self) -> str:
        return f"{self.fornavn} {self.etternavn}, {self.alder} år"

class Elev(Person):
    def __init__(self, fornavn, etternavn, klasse, alder=18) -> None:
        super().__init__(fornavn, etternavn, alder)
        self.klasse = klasse

    def __str__(self) -> str:
        return super().__str__() + f", klasse {self.klasse} på {self.finnTrinn()}."

    def finnTrinn(self):
        faar = 2024 - self.alder
        if faar == 2006:
            return "vg3"
        elif faar == 2007:
            return "vg2"
        elif faar == 2008:
            return "vg1"
        else:
            return "ukjent trinn"
        
class Laerer(Person):
    def __init__(self, fornavn, etternavn, kontor: str, kontordager: list, alder, fag: list, klasse="") -> None:
        super().__init__(fornavn, etternavn, alder)
        self.kontor = kontor
        self.kontordager = kontordager
        self.fag = fag
        self.klasse = klasse
    
    def visKontorDager(self):
        dager = ""
        x = 1
        for dag in self.kontordager:
            if x == len(self.kontordager):
                dager += "og " + dag + "."
            else:
                dager += dag + ", "
            x += 1
        return dager
    
    def visFag(self):
        fag = ""
        z = 0
        for x in self.fag:
            z += 1
            if z == len(self.fag):
                fag += "og " + x + "."
            elif len(self.fag) == 2 and z == 1:
                fag += x + " "
            else:
                fag += x + ", "
        return fag
    def underviser(self,bestemtfag):
        if bestemtfag in self.fag:
            return True
        else:
            return False
        

    def __str__(self) -> str:
        return super().__str__() + ".\n" + f"Kontor {self.kontor} og jobber på {self.visKontorDager()} Har klasse {self.klasse} og fag: {self.visFag()}"
#print(help(Person)) 

def main():
    elev1 = Elev("viktor","framnes","3G")
    elev2 = Elev("Jan","Johan","2C",17)
    elev3 = Elev("Lars","Lars","1A",16)
    print(elev1)
    print(elev2)
    print(elev3)
    print()
    laerer1 = Laerer("synne","kolsås","03-03",["mandag","onsdag","fredag"],28,["norsk","samfunnsfag"],"3G")
    print(laerer1.underviser("engelsk"))
    print()
    print(laerer1)
if __name__ == "__main__":
    main()