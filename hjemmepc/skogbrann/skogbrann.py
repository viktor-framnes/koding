import random
import tkinter as tk
import time

n = 30

class Skog:
    def __init__(self):
        self.tilstand = 0

class Simulasjon(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(800,800)
        self.frame = tk.Frame(self)
        self.frame.pack(expand=True)
        self.trær = [[Skog() for _ in range(n)] for _ in range(n)]
        [[self.lagblokk(i,j) for i in range(n)] for j in range(n)]
        tk.Button(self, text="Start", command=lambda: self.loop()).pack(expand=True)


    def lagblokk(self,i,j):
        blokk = tk.Canvas(self.frame,bg="#d6d5d5", width=20,height=20,highlightthickness=1)
        blokk.grid(row=i,column=j)

    def tre(self,i,j):
        blokk = tk.Canvas(self.frame,bg="green",width=20,height=20,highlightthickness=1)
        blokk.grid(row=i,column=j)
        self.trær[i][j].tilstand = 1
        blokk.update_idletasks()

    def nydag(self):
        for i in range(n):
            for j in range(n):
                if self.trær[i][j].tilstand == 0:
                    if random.random() < 0.6:
                        self.tre(i,j)

    def loop(self):
        for i in range(2):
            print(f"dag {i+1}")
            self.nydag()
            time.sleep(0.5)

Simulasjon().mainloop()