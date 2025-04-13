import tkinter as tk
import random

bredde = 400
hoyde = 400
r = 15

class Pactroll(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.kjorer = True
        self.x = bredde/2
        self.y = hoyde/2
        self.dx = 0
        self.dy = 0
        self.ds = 3
        self.matpos = []
        self.blokker = []
        self.resizable(False, False)
        

        self.canvas = tk.Canvas(self,bg="black",width=bredde,height=hoyde)
        self.minsize(bredde,hoyde)
        self.canvas.pack(expand=True)
        self.troll = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="green")


        self.bind("<KeyPress-Left>", lambda _: self.byttRettning(-self.ds, 0))
        self.bind("<KeyPress-Right>", lambda _: self.byttRettning(self.ds, 0))
        self.bind("<KeyPress-Up>", lambda _: self.byttRettning(0, -self.ds))
        self.bind("<KeyPress-Down>", lambda _: self.byttRettning(0, self.ds))

        self.game_loop()

    def sjekkKolisjon(self):
        # sjekker kolisjon med veggene
        if self.x+r >= bredde:
            self.game_over()
        if self.y+r >= hoyde:
            self.game_over()
        if self.x-r <= 0:
            self.game_over()
        if self.y-r <= 0:
            self.game_over()

        # kolisjon med mat bit
        trollpos = self.canvas.coords(self.troll)
        for i in range(len(self.matpos)):
            overlappX = trollpos[2] >= self.matpos[i][0] and trollpos[0] <= self.matpos[i][2]
            overlappY = trollpos[1] <= self.matpos[i][3] and trollpos[3] >= self.matpos[i][1]

            if overlappX and overlappY:
                if self.dx < 0:  # Beveger seg til venstre
                    self.byttRettning(self.ds, 0)  # Snu til høyre
                elif self.dx > 0:  # Beveger seg til høyre
                    self.byttRettning(-self.ds, 0)  # Snu til venstre
                elif self.dy < 0:  # Beveger seg oppover
                    self.byttRettning(0, self.ds)  # Snu nedover
                elif self.dy > 0:  # Beveger seg nedover
                    self.byttRettning(0, -self.ds)  # Snu oppover

                if self.blokker[i].tilstand == 0:
                    # Flytt trollet bort fra matbiten
                    self.x += self.dx
                    self.y += self.dy
                    self.canvas.move(self.troll, self.dx, self.dy)
                    self.ds += 0.2
                    self.lagMat()
                    self.blokker[i].hinder()
                else:
                    self.game_over()
                            

    def byttRettning(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def game_loop(self):
        if self.kjorer:
            self.sjekkKolisjon()
            self.x += self.dx
            self.y += self.dy
            self.canvas.move(self.troll, self.dx, self.dy)
            self.after(20,self.game_loop)
        
    def game_over(self):
        self.kjorer = False
        self.canvas.create_text(bredde/2,hoyde/2,text="Game over",fill="red",font=20)

    def lagMat(self, antall=1, maks_forsok=100):
        forsok = 0
        laget = 0

        while laget < antall and forsok < maks_forsok:
            forsok += 1
            blokk = Mat(self.canvas)
            ny_pos = self.canvas.coords(blokk.Mat_id)
            troll_pos = self.canvas.coords(self.troll)

            def overlapper(a, b):
                return (
                    a[2] >= b[0] and a[0] <= b[2] and
                    a[3] >= b[1] and a[1] <= b[3]
                )

            overlapp_med_troll = overlapper(ny_pos, troll_pos)
            overlapp_med_mat = any(overlapper(ny_pos, pos) for pos in self.matpos)

            if overlapp_med_troll or overlapp_med_mat:
                self.canvas.delete(blokk.Mat_id)
                continue  # prøv på nytt
            else:
                self.matpos.append(ny_pos)
                self.blokker.append(blokk)
                laget += 1



class Mat:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = random.randint(0+r,bredde-r)
        self.y = random.randint(0+r,hoyde-r)
        self.Mat_id = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="yellow")
        self.tilstand = 0
        
    def hinder(self):
        self.tilstand = 1
        self.canvas.itemconfig(self.Mat_id,fill="grey")

_ = Pactroll()
_.lagMat(3)
_.mainloop()


