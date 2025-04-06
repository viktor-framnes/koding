# Oppgave 9
# Del 1
# funksjonalitet for at nye personer starter som friske uten immunitet og kan bli smittet av andre.
# etter tre dager som smittet blir personen syke, og etter fire dagers sykdom blir de friske med immunitet.
# Sannsynligheten for død mens en person er syk, skal være 1 prosent (0,01) hver dag mens de er syke. 
# Definer klassen med passende datafelter og metoder.

import random 

tilstander = {
    0:"friskUtenImunitet", # lys grå
    1:"smittet", # rosa med svart skråstrek
    2:"syk", # rød med hvit skråstrek
    3:"friskMedImunitet", # mørk grå med svart prikk
    4:"død" # svart med hvit prikk
}

class Person():
    def __init__(self):
        self.tilstand = tilstander[0]

        
    def smitte(self):
        if self.tilstand == "friskUtenImunitet":
            self.tilstand = tilstander[1]
            self.dagerSmittet = 0

    def oppdaterTilstand(self):
        if self.tilstand == "smittet":
            self.dagerSmittet += 1
            if self.dagerSmittet > 3:
                self.tilstand = "syk"

        elif self.tilstand == "syk":
            self.dagerSmittet += 1
            if self.dagerSmittet <= 7:
                if random.randint(0,100) == 73:
                    self.tilstand = "død"
            else:
                self.tilstand = "firskMedImunitet"
    
    def __str__(self):
        return f"Personens tilstand er {self.tilstand}"

def main():
    person1 = Person()
    print(person1)
    person1.smitte()
    for i in range(8):
        person1.oppdaterTilstand()
        print(f"dag {i+1}")
        print(person1)

        

if __name__ == "__main__":
    main()
