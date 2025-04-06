# implementer en klasse "populasjon" som skal holde orden på et bestemt antall personer og smitte fra en person
# til naboer. I denne opggaven regnes to ruter som naboer bare dersom de ligger inntil hverandre vannrett eller
# loddrett, men ikke på skrå. Hver person har altså fire naboer.
# implementer funksjonalitet for å overføre smitte fra en smittet eller syk person til alle naboer som er friske
# uten immunitet, slik som i figur 2. Sannsynligheten for å bli smittet av en nabo er 30 prosent (0.3)
import random

class Populasjon():
    def __init__(self,n):
        self.lengde = n
        self.brett = []
        for i in range(self.lengde):
            self.brett.append([0]*self.lengde)
        self.brett[int(((self.lengde-2)/2)+1)][int(((self.lengde-2)/2)+1)] = 2 # midten
        self.brett[int(((self.lengde-2)/2)+1)][int(((self.lengde-2)/2)+2)] = 1 # øst
        self.brett[int(((self.lengde-2)/2)+1)][int(((self.lengde-2)/2))] = 1 # vest
        self.brett[int(((self.lengde-2)/2))][int(((self.lengde-2)/2)+1)] = 1 # nord
        self.brett[int(((self.lengde-2)/2)+2)][int(((self.lengde-2)/2)+1)] = 1 # sør
        

    def tegnBrett(self):
        for rad in self.brett:
            for i in range(0,len(rad)-1):
                print(f"{rad[i]:4}",end="")
            print(f"{rad[-1]:4}")
        print("\n")

    # def tegnBrett(self):
    #     for x in self.brett:
    #         print(x)

    def spredning(self):
        indekser = []

        for i in range(self.lengde):
            for j in range(self.lengde):
                if self.brett[i][j] == 1 or self.brett[i][j] == 2:
                    indekser.append(str(i) + " " + str(j))


        for i in range(len(indekser)):
            y, x = map(int,indekser[i].split())
            # Nord
            try:
                if y > 0:
                    if self.brett[y-1][x] == 0:
                        if random.random() < 0.3:
                            self.brett[y-1][x] = 1
                            # self.smittet()
                else:
                    pass
            except IndexError:
                pass
            # Sør
            try:
                if self.brett[y+1][x] == 0:
                    if random.random() < 0.3:
                        self.brett[y+1][x] = 1  
                        # self.smittet()
            except IndexError:
                pass
            # Øst
            try:
                if self.brett[y][x+1] == 0:
                    if random.random() < 0.3:
                        self.brett[y][x+1] = 1
                        # self.smittet()
            except IndexError:
                pass
            # Vest
            try:
                if x > 0:
                    if self.brett[y][x-1] == 0:
                        if random.random() < 0.3:
                            self.brett[y][x-1] = 1
                            # self.smittet()
                else:
                    pass
            except IndexError:
                pass


def main():
    populasjon1 = Populasjon(21)
    for i in range(20):
        populasjon1.tegnBrett()
        populasjon1.spredning()
    
if __name__ == "__main__":
    main()





# Testing:

# # lage et brett med n og m 

# n = 5
# m = 5

# brett = []
# for i in range(m):
#     brett.append([0]*n)

# for x in brett:
#     print(x)