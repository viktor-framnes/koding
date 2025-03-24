# implementer en klasse "populasjon" som skal holde orden på et bestemt antall personer og smitte fra en person
# til naboer. I denne opggaven regnes to ruter som naboer bare dersom de ligger inntil hverandre vannrett eller
# loddrett, men ikke på skrå. Hver person har altså fire naboer.
# implementer funksjonalitet for å overføre smitte fra en smittet eller syk person til alle naboer som er friske
# uten immunitet, slik som i figur 2. Sannsynligheten for å bli smittet av en nabo er 30 prosent (0.3)
import random
import tkinter as tk

class PopulasjonMedtkinter():
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
        
        self.window = tk.Tk()
        self.window.geometry("1010x1000")
        self.bredde = 1000
        self.hoyde = 1000

        self.frame = tk.Frame(self.window)
        self.frame.configure(
            background="blue",
            height= self.hoyde,
            width= self.bredde
        )
        self.frame.pack(expand=True)

        for i in range(11):
            for j in range(11):
                self.lagblokk(i,j)

        #start posisjon
        #midten
        self.sykBlokk(5,5)
        #N
        self.smittetBlokk(4,5)
        #S
        self.smittetBlokk(6,5)
        #V
        self.smittetBlokk(5,4)
        #Ø
        self.smittetBlokk(5,6)
        

    def lagblokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="grey",width=self.bredde*0.08,height=self.hoyde*0.08)
        self.blokk.grid(row=i,column=j)

    # def oppdaterblokk(self,i,j):

    #forskjellige typer tilstander
    def smittetBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="#ff9696",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_line(12,12,70,70,fill="black",width=5)
        self.blokk.grid(row=i,column=j)

    def sykBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="red",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_line(12,70,70,12,fill="white",width=5)
        self.blokk.grid(row=i,column=j)

    def friskMedInumitetBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="#414141",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_oval(38,38,48,48,fill="black")
        self.blokk.grid(row=i,column=j)

    def dodBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="black",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_oval(38,38,48,48,fill="white")
        self.blokk.grid(row=i,column=j)

    #viser brettet
    def vis(self):
        self.window.mainloop()

    def tegnBrett(self):
        for rad in self.brett:
            for i in range(0,len(rad)-1):
                print(f"{rad[i]:4}",end="")
            print(f"{rad[-1]:4}")
        print("\n")


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
                            self.smittetBlokk((y-1),x)
                else:
                    pass
            except IndexError:
                pass
            # Sør
            try:
                if self.brett[y+1][x] == 0:
                    if random.random() < 0.3:
                        self.brett[y+1][x] = 1  
                        self.smittetBlokk((y+1),x)
            except IndexError:
                pass
            # Øst
            try:
                if self.brett[y][x+1] == 0:
                    if random.random() < 0.3:
                        self.brett[y][x+1] = 1
                        self.smittetBlokk(y,(x+1))
            except IndexError:
                pass
            # Vest
            try:
                if x > 0:
                    if self.brett[y][x-1] == 0:
                        if random.random() < 0.3:
                            self.brett[y][x-1] = 1
                            self.smittetBlokk(y,(x-1))
                else:
                    pass
            except IndexError:
                pass

    # Ting som må fikses i rekkefølge:
    # 1. opppdatere tilstand funksjon for å bli syk, død eller imun
    # 2. animasjon av spredningen ikke bare slutten
    # 3. tilpasse størrelser sånt at det funker med forskjellig populasjoner
        
    # def oppdaterTilstand(self):
    #     for i in range(self.lengde):
    #         for j in range(self.lengde):

def main():

    populasjon1 = PopulasjonMedtkinter(11)
    for i in range(8):
        print(f"dag {i+1}")
        populasjon1.spredning()
        populasjon1.tegnBrett()
    populasjon1.vis()   
    
if __name__ == "__main__":
    main()