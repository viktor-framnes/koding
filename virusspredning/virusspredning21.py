import random
import tkinter as tk
import time

class Person():
    def __init__(self):
        self.dagerSmittet = 0
        self.tilstand = 0
        
class PopulasjonMedtkinter():
    def __init__(self,n):
        self.lengde = n
        
        self.window = tk.Tk()
        self.window.minsize(810,830)
        self.bredde = 1000
        self.hoyde = 1000
        self.frame = tk.Frame(self.window)
        tk.Button(self.window, text="Start", command=lambda: self.kjor()).pack(expand=True)
        self.frame.pack(expand=True)

        self.personer = [[Person() for i in range(self.lengde)] for j in range(self.lengde)]
        [[self.lagblokk(i,j) for i in range(self.lengde)] for j in range(self.lengde)]

        #start posisjon
        midten = int((self.lengde-1)/2)
        #midten
        self.sykBlokk(midten,midten)
        #N
        self.smittetBlokk(midten-1,midten)
        #S
        self.smittetBlokk(midten+1,midten)
        #V
        self.smittetBlokk(midten,midten-1)
        #Ø
        self.smittetBlokk(midten,midten+1)
        
    def lagblokk(self,i,j):
        blokk = tk.Canvas(self.frame,bg="#d6d5d5",width=self.bredde*0.03,height=self.hoyde*0.03)
        blokk.grid(row=i,column=j)

    #forskjellige typer tilstander
    def smittetBlokk(self,i,j,dager=1):
        self.personer[i][j].dagerSmittet = dager
        blokk = tk.Canvas(self.frame,bg="#ff9696",width=self.bredde*0.03,height=self.bredde*0.03)
        blokk.create_line(8,8,26,26,fill="black",width=2)
        blokk.grid(row=i,column=j)
        self.personer[i][j].tilstand = 1
        blokk.update_idletasks()

    def sykBlokk(self,i,j,dager=4):
        self.personer[i][j].dagerSmittet = dager
        blokk = tk.Canvas(self.frame,bg="red",width=self.bredde*0.03,height=self.bredde*0.03)
        blokk.create_line(8,26,26,8,fill="white",width=2)
        blokk.grid(row=i,column=j)
        self.personer[i][j].tilstand = 2
        blokk.update_idletasks()

    def friskMedInumitetBlokk(self,i,j):
        blokk = tk.Canvas(self.frame,bg="#8d8d8d",width=self.bredde*0.03,height=self.bredde*0.03)
        blokk.create_oval(14,14,20,20,fill="black")
        blokk.grid(row=i,column=j)
        self.personer[i][j].tilstand = 3
        blokk.update_idletasks()

    def dodBlokk(self,i,j):
        blokk = tk.Canvas(self.frame,bg="black",width=self.bredde*0.03,height=self.bredde*0.03)
        blokk.create_oval(14,14,20,20,fill="white")
        blokk.grid(row=i,column=j)
        self.personer[i][j].tilstand = 4
        blokk.update_idletasks()


    def spredning(self):
        indekser = []

        for i in range(self.lengde):
            for j in range(self.lengde):
                if self.personer[i][j].tilstand == 1 or self.personer[i][j].tilstand == 2 or self.personer[i][j].tilstand == 3:
                    indekser.append((i,j))

        for i in range(len(indekser)):
            y, x = indekser[i]

            if (self.personer[y][x].tilstand in [0,3,4]):
                continue
          
            if (y < 0 or y+1 > self.lengde or x < 0 or x+1 > self.lengde):
                continue
            
            if y > 0 and self.personer[y-1][x].tilstand == 0: #N
                if random.random() < 0.3:
                    self.smittetBlokk((y-1),x)
            if x < self.lengde-1 and self.personer[y][x+1].tilstand == 0: #Ø
                if random.random() < 0.3:
                    self.smittetBlokk(y,(x+1))
            if y < self.lengde-1 and self.personer[y+1][x].tilstand == 0: #S
                if random.random() < 0.3:
                    self.smittetBlokk((y+1),x)
            if x > 0 and self.personer[y][x-1].tilstand == 0: #V
                if random.random() < 0.3:
                    self.smittetBlokk(y,(x-1))

        

    def oppdaterTilstand(self):
        for i in range(self.lengde):
            for j in range(self.lengde):
                if self.personer[i][j].tilstand == 1 or self.personer[i][j].tilstand == 2 or self.personer[i][j].tilstand == 3:
                    self.personer[i][j].dagerSmittet += 1
                    if self.personer[i][j].tilstand == 1:
                        if self.personer[i][j].dagerSmittet > 3:
                            self.personer[i][j].tilstand = 2
                            self.sykBlokk(i,j)
                    elif self.personer[i][j].tilstand == 2:
                        if self.personer[i][j].dagerSmittet <= 7:
                            if random.randint(0,100) == 9:
                                self.personer[i][j].tilstand = 4
                                self.dodBlokk(i,j)
                        else:
                            self.personer[i][j].tilstand = 3
                            self.friskMedInumitetBlokk(i,j)

    def kjor(self):
        for i in range(16):
            print(f"dag {i+1}")
            self.oppdaterTilstand()
            self.spredning()
            time.sleep(1)
    

populasjon1 = PopulasjonMedtkinter(21)
populasjon1.window.mainloop() 