import random
import tkinter as tk
import time

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
        self.window.minsize(710,730)
        self.bredde = 1000
        self.hoyde = 1000

        self.frame = tk.Frame(self.window)
        self.frame.configure(
            background="blue",
            height= self.hoyde,
            width= self.bredde
        )
        tk.Button(self.window, text="Start", command=lambda: kjor()).pack(expand=True)
        self.frame.pack(expand=True)



        for i in range(11):
            for j in range(11):
                self.Person(i,j,self.window)
                

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
        self.blokk = tk.Canvas(self.frame,bg="grey",width=self.bredde*0.05,height=self.hoyde*0.05)
        self.blokk.grid(row=i,column=j)


    #forskjellige typer tilstander
    def friskUtenImunitet(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="grey",width=self.bredde*0.05,height=self.hoyde*0.05)
        self.blokk.grid(row=i,column=j)
        self.blokk.update()

    def smittetBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="#ff9696",width=self.bredde*0.05,height=self.bredde*0.05)
        self.blokk.create_line(8,8,46,46,fill="black",width=3.3)
        self.blokk.grid(row=i,column=j)
        self.blokk.update()

    def sykBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="red",width=self.bredde*0.05,height=self.bredde*0.05)
        self.blokk.create_line(8,46,46,8,fill="white",width=3.3)
        self.blokk.grid(row=i,column=j)
        self.blokk.update()

    def friskMedInumitetBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="#414141",width=self.bredde*0.05,height=self.bredde*0.05)
        self.blokk.create_oval(23,23,32,32,fill="black")
        self.blokk.grid(row=i,column=j)
        self.blokk.update()

    def dodBlokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="black",width=self.bredde*0.05,height=self.bredde*0.05)
        self.blokk.create_oval(23,23,32,32,fill="white")
        self.blokk.grid(row=i,column=j)
        self.blokk.update()

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
        self.Person.oppdaterTilstand()

    class Person():
        def __init__(self,i,j,forelder):
            self.dagerSyk = 0
            self.bredde = 1000
            self.hoyde = 1000
            self.tilstander = ["friskUtenImunitet","smittet","syk","friskMedImunitet","død"]
            self.tilstand = self.tilstander[0]

        def lagBlokk(self):
            for i in range(11):
                for j in range(11):
                    self.Person(i,j,self.window)


        def oppdaterTilstand(self):
            if self.tilstand == "friskUtenImunitet":
                PopulasjonMedtkinter.friskMedInumitetBlokk()

            elif self.tilstand == "smittet":
                self.dagerSmittet += 1
                if self.dagerSmittet > 3:
                    self.tilstand = self.tilstander[2]
                    PopulasjonMedtkinter.sykBlokk()
                else:
                    PopulasjonMedtkinter.smittetBlokk()
                        
            elif self.tilstand == "syk":
                PopulasjonMedtkinter.sykBlokk()
                self.dagerSmittet += 1
                if self.dagerSmittet <= 7:
                    if random.randint(0,100) == 9:
                        self.tilstand = self.tilstander[4]
                        PopulasjonMedtkinter.dodBlokk()
                else:
                    self.tilstand = self.tilstander[3]
                    PopulasjonMedtkinter.friskMedInumitetBlokk()


def kjor():
    for i in range(8):
        print(f"dag {i+1}")
        populasjon1.spredning()
        populasjon1.tegnBrett()
        time.sleep(1)
    

populasjon1 = PopulasjonMedtkinter(11)
populasjon1.window.mainloop() 
    
