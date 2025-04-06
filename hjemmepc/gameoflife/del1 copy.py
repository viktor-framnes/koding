import tkinter as tk
import random

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

class Brett(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(700,500)
        self.configure(bg="lightgrey")
        self.knapper = tk.Frame(self)
        self.knapper.pack(expand=True)
        tk.Button(self.knapper,text="Tøm",command=lambda:self.tom()).pack(side="left")
        tk.Button(self.knapper,text="Start",command=lambda:self.start()).pack()
        self.frame = tk.Frame(self)
        self.frame.pack(expand=True)

        self.celler = [[Celle(self.frame) for i in range(20)] for j in range(20)]

        for i in range(20):
            for j in range(20):
                if random.random() < 0.3:
                    farge = "black"
                else:
                    farge = "white"
                self.celler[i][j].lagCelle(i,j,farge)

    def tom(self):
        for i in range(20):
            for j in range(20):
                self.celler[i][j].cell.config(bg="white")
                self.celler[i][j].tilstand = 0


    def tegnBrett(self):
        for rad in self.brettKopi:
            for i in range(0,len(rad)-1):
                print(f"{rad[i]:4}",end="")
            print(f"{rad[-1]:4}")
        print("\n")

    def start(self):
        self.brettKopi = []
        for i in range(20):
            self.brettKopi.append([0]*20)
        teller = 0


        for i in range(20):
            for j in range(20):
                try:
                    #N
                    if self.celler[i-1][j].tilstand == 1:
                        teller += 1
                    #S
                    if self.celler[i+1][j].tilstand == 1:
                        teller += 1
                    #Ø
                    if self.celler[i][j+1].tilstand == 1:
                        teller += 1
                    #V
                    if self.celler[i][j-1].tilstand == 1:
                        teller += 1
                    #NØ
                    if self.celler[i-1][j+1].tilstand == 1:
                        teller += 1
                    #NV
                    if self.celler[i-1][j-1].tilstand == 1:
                        teller += 1
                    #SØ
                    if self.celler[i+1][j+1].tilstand == 1:
                        teller += 1
                    #SV
                    if self.celler[i+1][j-1].tilstand == 1:
                        teller += 1
                except IndexError:
                    pass

                if teller > 3:
                    self.brettKopi[i][j] = 0
                elif teller == 2 or teller == 3:
                    self.brettKopi[i][j] = 1
                elif teller < 2:
                    self.brettKopi[i][j] = 0
        self.tegnBrett()



a = Brett()
a.mainloop()


