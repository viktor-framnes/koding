

class Vitazoo():
    def __init__(self) -> None:
        self.områder = {}

    def legg_til_område(self,område:object):
        if område.navn in self.områder:
            print(f"Området er i zooen")
        else:
            self.områder[område.navn] = område
            print(f"Området er lagt til, {område.navn}")

    def fjern_område(self,område):
        if område.navn in self.områder:
            self.områder.pop(område.navn)
            print(f"området: {område.navn} er fjernet")
        else:
            print("området finnes ikke") 
        
    def finn_dyr_i_område(self, dyr: object) -> object | bool:                
        for områdeNavn, område in self.områder.items():
            if dyr in område.dyr_i_område:
                print(f"{dyr} finnes i område {områdeNavn}")
                return dyr
        print("Dyret ble ikke funnet i noen områder")
        return False            
            
    def flytt_dyr(self,dyr,nytt_område) -> bool:
        if self.finn_dyr_i_område(dyr) != False:
            for område in self.områder.values():
                if dyr in område.dyr_i_område:
                    område.dyr_i_område.remove(dyr)
            for områdeNavn in self.områder.keys():
                if nytt_område == områdeNavn:
                    self.områder[områdeNavn].legg_til_dyr(dyr)
            return True
        else:
            print("Dyret er ikke i et område")
            return False
    
    def __str__(self) -> str:
        pass






class Område():
    def __init__(self,navn,dyr:list) -> None:
        self.navn = navn
        self.dyr_i_område = dyr

    def legg_til_dyr(self,dyr):
        if dyr in self.dyr_i_område:
            print("Dyret er allerede i området")
        else:
            self.dyr_i_område.append(dyr)
    
    def fjern_dyr(self,dyr):
        if dyr in self.dyr_i_område:
            self.dyr_i_område.remove(dyr)
        else:
            print("dyret er ikke i området")

    def __str__(self) -> str:
        return f"Området {self.navn} har disse dyrene: {self.dyr_i_område}"

class Dyr():
    def __init__(self,art,id,teller = 0) -> None:
        self.teller = teller #Denne har jeg ikke fikset
        self.art = art
        self.id = id

    def settId(self,id:int):
        self.id = id

    def __str__(self) -> str:
        return f"Art: {self.art}, id: {self.id}, teller: {self.teller}"

def main():
    vitazoo = Vitazoo()
    ekkorn = Dyr("ekkorn",14)
    bjorn = Dyr("bjørn",10)
    isbjorn = Dyr("isbjørn",16)
    pingvin = Dyr("pingvin",9)
    arktisk = Område("arktisk",[isbjorn,pingvin])
    skog = Område("skog",[ekkorn,bjorn])
    vitazoo.legg_til_område(skog)
    vitazoo.legg_til_område(arktisk)
    # vitazoo.fjern_område(skog)
    vitazoo.finn_dyr_i_område(bjorn)
    vitazoo.flytt_dyr(isbjorn,"skog")
    
if __name__ == "__main__":
    main()