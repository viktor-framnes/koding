import datetime as dt

class Flight:
    def __init__(self, flynummer, avreisetid, ankomsttid) -> None:
        self.flynummer = flynummer
        self.avreisetid = avreisetid
        self.ankomsttid = ankomsttid

    def setFlynummer(self,flynummer):
        self.flynummer = flynummer

    def getFlynummer(self):
        print(f"Flynummeret er {self.flynummer}")

    def setAvreise(self, tid):
        if tid > self.avreisetid:
            endring = tid - self.avreisetid
            self.ankomsttid = self.ankomsttid + endring
        else:
            endring = self.avreisetid - tid
            self.ankomsttid = self.ankomsttid - endring
        self.avreisetid = tid

    def getAvreise(self):
        print(f"Avreisetid til fly {self.flynummer} er {self.avreisetid}")

    def setAnkomst(self, tid):
        self.ankomsttid = tid
    
    def getAnkomsttid(self):
        print(f"Ankomsttid til fly {self.flynummer} er {self.ankomsttid}")

    def getFlightTime(self):
        tid = self.ankomsttid - self.avreisetid
        print(f"Flyturen tar {(tid.seconds / 60):.0f} minutter")


def main():
    fly1 = Flight("0154",dt.datetime(2024,3,1,12,30),dt.datetime(2024,3,1,14,30))
    # fly1.setFlynummer("0154")
    fly1.getFlynummer()
    # fly1.setAvreise(2024,3,1,12,30)
    fly1.getAvreise()
    # fly1.setAnkomst(2024,3,1,14,30)
    fly1.getAnkomsttid()
    fly1.getFlightTime()

if __name__ == "__main__":
    main()    