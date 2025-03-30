import random
import tkinter as tk
import time

class Celle:
    def __init__(self,forelder):
        self.tilstand = 0
        self.forelder = forelder

    def lagCelle(self,i,j,farge):
        if farge == "black":
            self.tilstand = 1
        self.pixel = tk.PhotoImage(width=1, height=1)
        self.cell = tk.Button(self.forelder,bg=farge,image=self.pixel,width=15,height=15,highlightthickness=1,command=self.klikket)
        self.cell.grid(row=i,column=j)
    
    def klikket(self):
        if self.tilstand == 0:
            self.cell.config(bg="black")
            self.tilstand = 1
        else:
            self.cell.config(bg="white")
            self.tilstand = 0

class Gameoflife(tk.Tk):
    def __init__(self,lengde):
        self.lengde = lengde

        tk.Tk.__init__(self)
        self.minsize(800,700)
        self.configure(bg="lightgrey")
        self.knapper = tk.Frame(self)
        self.knapper.pack(expand=True)
        tk.Button(self.knapper,text="Tøm",command=lambda:self.tom()).pack(side="left")
        tk.Button(self.knapper,text="Start",command=lambda:self.kjor()).pack()
        self.frame = tk.Frame(self)
        self.frame.pack(expand=True)

        self.celler = [[Celle(self.frame) for i in range(self.lengde)] for j in range(self.lengde)]

        for i in range(self.lengde):
            for j in range(self.lengde):
                if random.random() < 0.3:
                    farge = "black"
                else:
                    farge = "white"
                self.celler[i][j].lagCelle(i,j,farge)

    def tom(self):
        for i in range(self.lengde):
            for j in range(self.lengde):
                self.celler[i][j].cell.config(bg="white")
                self.celler[i][j].tilstand = 0

    def kjor(self):
            for n in range(self.lengde):
                for m in range(self.lengde):
                    naboer = self.tellnaboer(n,m)
                    if self.celler[n][m].tilstand == 1:
                        if naboer in [2,3]: 
                            self.celler[n][m].tilstand = 3
                    elif naboer == 3:
                        self.celler[n][m].tilstand = 2

            for n in range(self.lengde):
                for m in range(self.lengde):
                    if self.celler[n][m].tilstand == 1:
                        self.celler[n][m].tilstand = 0
                        self.celler[n][m].cell.config(bg="white")
                    elif self.celler[n][m].tilstand in [2,3]:
                        self.celler[n][m].tilstand = 1
                        self.celler[n][m].cell.config(bg="black")


    def tellnaboer(self,n,m):
        naboer = 0
        for i in range(n-1,n+2):
            for j in range(m-1,m+2):
                if ((i==n and j==m) or i<0 or j<0 or i==self.lengde or j==self.lengde):
                    continue
                if self.celler[i][j].tilstand in [1,3]:
                    naboer += 1
        return naboer

    

if __name__ == "__main__":
    x = Gameoflife(30)
    x.mainloop()
