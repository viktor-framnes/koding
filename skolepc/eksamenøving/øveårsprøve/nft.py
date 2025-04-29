class Nft:
    def __init__(self, tittel, artist, nft_id, eier, pris):
        self.tittel = tittel
        self.artist = artist
        self.nft_id = nft_id
        self.pris = pris
        self.eier = eier

    def getPris(self):
        return self.pris

    def __str__(self):
        return f"{self.tittel} av {self.artist} (id:{self.nft_id}), eier: {self.eier}, pris: {self.pris:.2f} kr"

class BoredMonkey(Nft):
    antall_igjen = 5

    def __init__(self, nft_id, eier, størrelse, pris=100000):
        super().__init__("BoredMonkey", "Seneca", nft_id, eier, pris)
        self.størrelse = størrelse
        self.pris = pris
        if BoredMonkey.antall_igjen > 0:    # Fjerner ledige BoredMonkey ved et kjøp.
            BoredMonkey.antall_igjen -= 1
        else:
            print("Det finnes ikke noen ledige bilder igjen!")
            return None
        self.beregn_pris()


    def beregn_pris(self):
        if self.størrelse == "small":
            self.pris = self.pris
        elif self.størrelse == "medium":
            self.pris += 249
        elif self.størrelse == "large":
            self.pris += 999

    def __str__(self):
        return f"{super().__str__()}, størrelse: {self.størrelse.capitalize()}, {self.antall_igjen} igjen."

class DogeDog(Nft):
    antall_igjen = 1

    def __init__(self, nft_id, eier, pris=4000000):
        super().__init__("Doge Dog", "Druide", nft_id, eier, pris)
        self.varier_pris = pris
        if DogeDog.antall_igjen > 0:    # Fjerner ledige BoredMonkey ved et kjøp.
            DogeDog.antall_igjen -= 1
        else:
            print("Det finnes ikke noen ledige bilder igjen!")
            return None
        self.oppdater_pris()

    def oppdater_pris(self):
        from random import random
        self.varier_pris = ( 1+random() ) * self.varier_pris # Funksjon skal f.eks. gå på internett for å hente oppdatert pris. Eller beregne pris basert på en spesiell algoritme som gjort her.
        self.pris = self.varier_pris

    def setPris(self,nypris):
        self.varier_pris = nypris

    def __str__(self):
        return f"{super().__str__()}, {self.antall_igjen} igjen."

class Handlekurv:
    def __init__(self):
        self.innhold = []
        self.totalsum = 0

    def legg_til(self, objekt):
        self.innhold.append(objekt)
        self.totalsum += objekt.pris

    def vis_info(self):
        for objekt in self.innhold:
            print(objekt)
        print(f"Total sum: {self.totalsum:.2f} kr")



teller = 2
if BoredMonkey.antall_igjen > 0:
    bm1 = BoredMonkey(teller, "Henrik", "large")
    teller += 1 # øker telleren
#print(bm1) # Skriver ut "BoredMonkey #1 av Kunstner X (id:bm123) - Large (100999 kr), eier: John. 5 igjen."

if DogeDog.antall_igjen > 0:
    dd1 = DogeDog(1,"Henrik")
#print(dd1) # Skriver ut "Doge Dog av Druide (id:1) - 4000000 kr, eier: Henrik. 0 igjen."

nft1 = Nft("Nft #1", "Kunstner Z", 3, "Bob", 1000)

# Legg bildene i handlekurv
handlekurv = Handlekurv()

handlekurv.legg_til(bm1)
handlekurv.legg_til(dd1)
handlekurv.legg_til(nft1)

# Skriv ut all informasjon om objektene i handlekurven
handlekurv.vis_info()

