import tkinter as tk

class Spill(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(500,500)
        self.resizable(False,False)

        self.frame = tk.Frame(self,width=500,height=500)
        self.frame.pack()

        self.blokker = [[self.lagblokk(i,j) for i in range(25)] for j in range(25)]

        self.spillerposx = 0
        self.spillerposy = 12
        self.lagspiller(self.spillerposy,self.spillerposx)

        self.bind("<Left>",lambda _:self.flyttspiller(self.spillerposy,self.spillerposx-1))
        self.bind("<Right>",lambda _:self.flyttspiller(self.spillerposy,self.spillerposx+1))
        self.bind("<Up>",lambda _:self.flyttspiller(self.spillerposy-1,self.spillerposx))
        self.bind("<Down>",lambda _:self.flyttspiller(self.spillerposy+1,self.spillerposx))


    def lagspiller(self,i,j):
        blokk = tk.Canvas(self.frame,width=20,height=20,bg="red",highlightthickness=1)
        blokk.grid(row=i,column=j)

    def flyttspiller(self,i,j,):
        if i < 0 or j < 0 or i > 24 or j > 24:
            return
        
        blokk = tk.Canvas(self.frame,width=20,height=20,bg="white",highlightthickness=1,highlightbackground="lightgrey")
        blokk.grid(row=self.spillerposy,column=self.spillerposx)
            
        blokk = tk.Canvas(self.frame,width=20,height=20,bg="red",highlightthickness=1)
        blokk.grid(row=i,column=j)
        self.spillerposx = j
        self.spillerposy = i

    def lagblokk(self,i,j):
        blokk = tk.Canvas(self.frame,width=20,height=20,bg="white",highlightthickness=1,highlightbackground="lightgrey")
        blokk.grid(row=i,column=j)


Spill().mainloop()