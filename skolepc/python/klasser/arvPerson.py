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
    def __init__(self, fornavn, etternavn, alder=18) -> None:
        super().__init__(fornavn, etternavn, alder)

    def __str__(self) -> str:
        return super().__str__() + f", klasse {self.klasse}."

class Laerer(Person):
    def __init__(self, fornavn, etternavn, kontor: str, kontordager: list, alder=18) -> None:
        super().__init__(fornavn, etternavn, alder)
        self.kontor = kontor
        self.kontordager = kontordager
    
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

    def __str__(self) -> str:
        return super().__str__() + f", kontor \n {self.kontor} og jobber på {self.visKontorDager()}"
#print(help(Person)) 

def main():
    elev1 = Person("Viktor","Framnes",18)
    # elev2 = Elev("Jan","Johansen","3STG",42)
    # laerer1 = Laerer("Lars","Larsen","03-25",["mandag","tirsdag","torsdag","fredag"],45)
    print(elev1)
    # print(elev2)
    # print(laerer1)


if __name__ == "__main__":
    main()