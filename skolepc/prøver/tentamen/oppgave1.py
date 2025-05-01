""""
Siden dett er et datasystem til AviaNor regner jeg med at de har selv kontroll på hvilke lufthavner de opererer ved
og at de derfor selv også når skal sette opp en rute, klarer å lage rute listen med lufthavner som de selv har kontroll på.

"""


class Transportsystem:
    def __init__(self): # systemets oversikt over alle fly, ruter og lufthavner de har i systemet
        self.alleFly = []
        self.lufthavner = []
        self.ruter = []

    def leggtilLufthavn(self,lufthavn:str): # når AviaNor skal operere ved en flyplass må de legge den inn ved å bruke denne metoden
        if lufthavn not in self.lufthavner: # sjekker om det ikke finnes alt
            self.lufthavner.append(lufthavn)
        else:
            print("Den finnes i systemet")

    def leggtilRute(self,rute:list): # denne lar AviaNor sette opp en ny rute med ruten som en liste med rekkefølge og hvilke lufthavener
        if rute not in self.ruter: # sjekker om det ikke finnes alt
            self.ruter.append(rute)
        else:
            print("Ruten finnes alt")

    def leggtil(self,fly:object): # legger til fly i systemet
        self.alleFly.append(fly)

    def tildelRute(self,fly,rute): # tildeler et fly en rute
        self.alleFly[fly.id].rute = f"Rutenummer {rute+1} som går gjennom {self.ruter[rute]}"

    def visinfo(self): # skriver ut alle fly i systemet
        print("Alle fly i systemet:")
        for fly in self.alleFly:
            print(fly)
            if fly.rute != "":
                print(f"og flyet har rute: {fly.rute}") # hvis flyet har en rute, så skriver den ut den også

    def visRuter(self): # skriver ut alle ruter som er lagt inn
        print("Alle ruter som er lagt inn")
        for i, rute in enumerate(self.ruter):
            print(f"Rutenummer: {i+1} har rute gjennom disse flyplassene i denne rekkefølgen: {rute}")

class Fly:
    idtall = 0
    def __init__(self,modell:str,seter:int,rekke:float,kommersiell:bool,motor:str):
        Fly.idtall += 1
        self.id = Fly.idtall
        self.modell = modell
        self.seter = seter
        self.rekke = rekke
        self.motor = motor
        self.kommersiell = kommersiell
        self.rute = ""

    def __str__(self):
        return f"Modell: {self.modell} med seter {self.seter}, id: {self.id}, rekkevidde på {self.rekke} km og {self.motor} motor"
    

class Forretningsfly(Fly):
    def __init__(self, modell:str, seter:int, rekke:float, lydisolasjon:bool,lokaler:bool,satellitt:bool,kommersiell=True,motor="Jet"):
        super().__init__(modell, seter, rekke, kommersiell,motor)
        self.lydisolasjon = lydisolasjon
        self.lokaler = lokaler
        self.satellitt = satellitt

    def __str__(self):
        return f"{super().__str__()}, lydisolasjon: {self.lydisolasjon}, lokaler: {self.lokaler}, satelittkommunikasjon: {self.satellitt}"

class Passasjerfly(Fly):
    def __init__(self, modell:str, seter:int, rekke:float, kommersiell=True,motor="Turboprop"):
        super().__init__(modell, seter, rekke,kommersiell,motor)

    def __str__(self):
        return super().__str__()

class Treningsfly(Fly):
    antalligjen = 1
    def __new__(cls,rekke:float,motor="Propell"): # passer på at det ikke kan bli lagd flere enn et treningsfly
        if cls.antalligjen > 0:
            cls.antalligjen -= 1
            return super().__new__(cls)
        else:
            print("Du kan bare lage ett treningsfly")
            return None

    def __init__(self, rekke:float, motor="Propell"):
        super().__init__("Cessna 172 Skyhawk fra 2001", 4, rekke, False,motor)
        self.dobbelkontroll = True
        self.registreringsnummer = "LN-ABX"


    def __str__(self):
        return f"{super().__str__()}, dobbelkontroll: {self.dobbelkontroll}, registreringsnummer: {self.registreringsnummer}"



if __name__ == "__main__":
    t = Transportsystem()
    fly1 = Forretningsfly("G3 180 2025",8,1200,True,True,True)
    fly2 = Passasjerfly("Boeng 520 2023",220,15000)
    fly3 = Treningsfly(120)
    fly4 = Treningsfly(120)
    t.leggtil(fly1)
    t.leggtil(fly2)
    t.leggtil(fly3)
    t.leggtilLufthavn("Gardemoen")
    t.leggtilLufthavn("Bergen lufthavn")
    t.leggtilLufthavn("Trondheim lufthavn")
    t.leggtilLufthavn("Ålesund lufthavn")
    t.leggtilLufthavn("Florø lufthavn")
    t.leggtilRute([t.lufthavner[0],t.lufthavner[3],t.lufthavner[2]]) # fare for indexError hvis du tar større indeks enn det er i listen, men Avianor vet godt selv hvilke lufthavner som de kan lage rute av.
    t.leggtilRute([t.lufthavner[0],t.lufthavner[1],t.lufthavner[4],t.lufthavner[2]]) # de kan heller bare skrive inn manuelt lufthavnen, denne metoden var for å forhindre at man lager en rute med lufthavner som ikke er i systemet
    t.tildelRute(fly1,0)
    t.tildelRute(fly2,1)
    t.visinfo()
    t.visRuter()