import tkinter as tk

class Spill(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(500, 500)
        self.resizable(False, False)

        self.frame = tk.Frame(self, width=500, height=500)
        self.frame.pack()

        self.blokker = [[self.lagblokk(i, j) for j in range(50)] for i in range(50)]

        self.spillerposx = 0
        self.spillerposy = 12
        self.oppdater_spillerposisjon()

        self.retninger = [[-1,0],[1,0],[0,-1],[0,1]]
        self.aktivretning = self.retninger[1]

        self.bind("<Left>", lambda _: self.setretning(self.retninger[0]))
        self.bind("<Right>", lambda _: self.setretning(self.retninger[1]))
        self.bind("<Up>", lambda _: self.setretning(self.retninger[2]))
        self.bind("<Down>", lambda _: self.setretning(self.retninger[3]))


        self.gameloop()

    def setretning(self,retning):
        self.aktivretning = retning

    def lagblokk(self, i, j):
        blokk = tk.Canvas(self.frame, width=10, height=10, bg="white", highlightthickness=1, highlightbackground="lightgrey")
        blokk.grid(row=i, column=j)
        return blokk

    def oppdater_spillerposisjon(self):
        self.blokker[self.spillerposy][self.spillerposx].configure(bg="red")

    def flytt(self, retning):
        ny_x = self.spillerposx + retning[0]
        ny_y = self.spillerposy + retning[1]

        if 0 <= ny_x < 50 and 0 <= ny_y < 50:
            self.blokker[self.spillerposy][self.spillerposx].configure(bg="white")
            self.spillerposx = ny_x
            self.spillerposy = ny_y
            self.blokker[self.spillerposy][self.spillerposx].configure(bg="red")

    def gameloop(self):
        
        self.flytt(self.aktivretning)

        self.after(200, self.gameloop)



Spill().mainloop()
