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
        if self.x+r >= bredde:
            self.game_over()
        if self.y+r >= hoyde:
            self.game_over()
        if self.x-r <= 0:
            self.game_over()
        if self.y-r <= 0:
            self.game_over()
            

    def byttRettning(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def game_loop(self):
        if self.kjorer:
            self.x += self.dx
            self.y += self.dy
            self.canvas.move(self.troll, self.dx, self.dy)
            self.sjekkKolisjon()
            self.after(20,self.game_loop)
        
    def game_over(self):
        self.kjorer = False
        self.canvas.create_text(bredde/2,hoyde/2,text="Game over",fill="red",font=20)

    def lagMat(self,i=1):
        for _ in range(i):
            self.blokk = Mat(self.canvas)
            nyMatpos = self.canvas.coords(self.blokk.Mat_id)
            trollpos = self.canvas.coords(self.troll)

            overlappX = trollpos[2] >= nyMatpos[0] and trollpos[0] <= nyMatpos[2]
            overlappY = trollpos[1] <= nyMatpos[3] and trollpos[3] >= nyMatpos[1]

            print(nyMatpos)
            print(trollpos)

            # if overlappX and overlappY:
            #     self.canvas.delete(self.blokk.Mat_id)
            #     self.lagMat()
            # else:
            #     if self.canvas.coords(self.blokk.Mat_id) not in self.matpos:
            #         self.matpos.append(self.canvas.coords(self.blokk.Mat_id))

            for a in range(len(self.matpos)):
                overlappX = nyMatpos[2] >= self.matpos[a][0] and nyMatpos[0] <= self.matpos[a][2]
                overlappY = nyMatpos[1] <= self.matpos[a][3] and nyMatpos[3] >= self.matpos[a][1]
                if overlappX and overlappY:
                    print("hey")
                    self.canvas.delete(self.blokk.Mat_id)
                    self.lagMat()
                else:
                    if self.canvas.coords(self.blokk.Mat_id) not in self.matpos:
                        self.matpos.append(self.canvas.coords(self.blokk.Mat_id))
            if len(self.matpos) == 0:
                self.matpos.append(self.canvas.coords(self.blokk.Mat_id))


class Mat:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = random.randint(0+r,bredde-r)
        self.y = random.randint(0+r,hoyde-r)
        self.Mat_id = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="yellow")
        


_ = Pactroll()
_.lagMat(3)
print(_.matpos)
_.mainloop()