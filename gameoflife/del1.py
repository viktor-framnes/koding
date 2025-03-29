import tkinter as tk
import random

class Celle:
    def __init__(self):
        self.tilstand = 0

class Brett(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(700,700)
        self.configure(bg="lightgrey")
        self.farger = ["white","black"]     
        tk.Button(self,text="Tøm",command=lambda:self.tom()).pack(expand=True)

        self.frame = tk.Frame(self)
        self.frame.configure(
            bg="blue"
        )
        self.frame.pack(expand=True)

        self.celler = [[Celle() for i in range(30)] for j in range(30)]

        for i in range(30):
            for j in range(30):
                if random.random() < 0.3:
                    farge = self.farger[1]
                else:
                    farge = self.farger[0]
                self.lagCelle(i,j,farge)

    def lagCelle(self,i,j,farge):
        self.cell = tk.Canvas(self.frame,bg=farge,width=15,height=15,highlightthickness=1)
        self.cell.grid(row=i,column=j)

    def tom(self):
        for i in range(30):
            for j in range(30):
                self.cell = tk.Canvas(self.frame,bg=self.farger[0],width=15,height=15,highlightthickness=1)
                self.cell.grid(row=i,column=j)


a = Brett()
a.mainloop()