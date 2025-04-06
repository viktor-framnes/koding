class Batteri():
    def __init__(self, batteriID:str,energikapasitet:float):
        self.batteriID = batteriID
        self.energinivå = 100
        self.energikapasitet = energikapasitet

    def ladOpp(self,energi:float) -> None:
        if (self.energinivå + (energi / self.energikapasitet * 100)) > 100:
            print("batteriet er for liten for å lade så mye")
        else:
            self.energinivå += energi / self.energikapasitet * 100 
        

    def brukEnergi(self,energi:float) -> None:
        if (self.energinivå - (energi / self.energikapasitet * 100)) < 0:
            print("du har ikke så mye energi å bruke") 
        else:
            self.energinivå -= energi / self.energikapasitet * 100

    def visEnergiNivå(self) -> float:
        return f"{self.energinivå}%"


def main():
    bt1 = Batteri(1,2000)
    print(bt1.visEnergiNivå())
    bt1.brukEnergi(3000)
    print(bt1.visEnergiNivå())
    bt1.ladOpp(100)
    print(bt1.visEnergiNivå())

if __name__ == "__main__":
    main()
