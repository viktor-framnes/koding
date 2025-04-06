"""
Mitt første ekte python-program.
En quiz med spørsmål og svar.
"""

class Quiz:
    def __init__(self):
        self.navn = "Viktor"
        self.questions = [
            ["Er hovedstaden i Norge Oslo?","ja"],
            ["Er 1 + 1 = 2?","ja"],
            ["Er det bare fire land i Norden?","nei"],
            ["Hva heter hovedstaden til Italia?","roma"],
            ["Ble jeg født i 2006?","ja"]
            ]

    def nyttSpm(self):
        if len(self.questions) > 0:
            return self.questions.pop()
        else:
            return "Error! Ikke flere spørsmål!"

    def sjekkSvar(self,spm,brukersvar):
        if brukersvar.lower() == spm[1].lower():
            print("Hurra! Det var riktig")
        else:
            print("Sorry, feil svar :(")

q = Quiz()
print(q.navn)
spm = q.nyttSpm() # Legger et nytt spørsmål inn i variabel spm
print(spm[0])
svar = input("Svar på spørsmålet: ")
print(f"Du svarte: {svar}")
q.sjekkSvar(spm,svar)

# Henter spørsmål
spm2 = q.nyttSpm()
print(spm2[0])
# Svarer på det
svar2 = input("Svar på spørsmålet: ")
# Sjekker svar
q.sjekkSvar(spm2,svar2)

spm3 = q.nyttSpm()
print(spm3[0])
svar3 = input("Svar på spørsmålet: ")
q.sjekkSvar(spm3,svar3)

spm4 = q.nyttSpm()
print(spm4[0])
svar4 = input("Svar på spørsmålet: ")
q.sjekkSvar(spm4,svar4)

spm5 = q.nyttSpm()
print(spm5[0])
svar5 = input("Svar på spørsmålet: ")
q.sjekkSvar(spm5,svar5)

