import tkinter as tk
import random


bredde = 1000
hoyde = 500
r = 15

class Manic(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.kjorer = True
        self.x = 50
        self.y = hoyde/2
        self.dx = 0
        self.dy = 0
        self.ds = 4
        self.aktive_taster = []
        self.blokkpos = []
        self.sauer = []
        self.hindrer = []
        self.ghoster = []

        self.resizable(False, False)
        self.canvas = tk.Canvas(self,bg="black",width=bredde,height=hoyde)
        self.minsize(bredde,hoyde)
        self.canvas.pack(expand=True)
        self.hoyrebrett = self.canvas.create_rectangle(0,0,200,hoyde,fill="red",outline="")
        self.hoyrebrett = self.canvas.create_rectangle(bredde-200,0,bredde,hoyde,fill="blue",outline="")
        self.spiller = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="green",outline="")

        # Bind keypress og keyrelease
        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)

        self.game_loop()

    def key_press(self, event):
        t = event.keysym
        if t in ["Up", "Down", "Left", "Right"]:
            if t in self.aktive_taster:
                self.aktive_taster.remove(t)  # Fjern den hvis den allerede er der
            self.aktive_taster.append(t)     # Legg den til sist (nyeste tast)
        self.oppdater_rettning()


    def key_release(self, event):
        t = event.keysym
        if t in self.aktive_taster:
            self.aktive_taster.remove(t)
        self.oppdater_rettning()


    def oppdater_rettning(self):
        if not self.aktive_taster:
            self.dx, self.dy = 0, 0
            return

        t = self.aktive_taster[-1]  # Sist trykkede tast
        if t == "Up":
            self.dx, self.dy = 0, -self.ds
        elif t == "Down":
            self.dx, self.dy = 0, self.ds
        elif t == "Left":
            self.dx, self.dy = -self.ds, 0
        elif t == "Right":
            self.dx, self.dy = self.ds, 0


    def sjekkKolisjon(self):
        if self.x+r >= bredde:
            self.x = bredde - r
        if self.y+r >= hoyde:
            self.y = hoyde - r
        if self.x-r <= 0:
            self.x = r
        if self.y-r <= 0:
            self.y = r

        spiller = self.canvas.coords(self.spiller)
        for i in range(len(self.blokkpos)):
            overlappX = spiller[2] >= self.blokkpos[i][0] and spiller[0] <= self.blokkpos[i][2]
            overlappY = spiller[1] <= self.blokkpos[i][3] and spiller[3] >= self.blokkpos[i][1]

            if overlappX and overlappY:
                # self.x -= self.dx
                # self.y -= self.dy
                pass

        for i in self.ghoster:
            if i.y + r >= hoyde:
                i.dy = -i.dy
                i.y = hoyde - r
            if i.x - r <= 200:
                i.dx = -i.dx
                i.x = r+200
            # topp
            if i.y - r <= 0:
                i.dy = -i.dy
                i.y = r
            # høyre
            if i.x + r >= bredde-200:
                i.dx = -i.dx
                i.x = bredde - r - 200
                
            for ghost in self.ghoster:
                # Beregner avstand mellom sirklene med pythagoras.
                dx = abs(ghost.x - i.x)
                dy = abs(ghost.y - i.y)
                d = (dx**2 + dy**2)**0.5
                if d <= 2*r:
                    # forenklet bevegelsesmengde
                    i.x -= i.dx
                    ghost.x -= ghost.dx
                    i.y -= i.dy
                    ghost.y -= ghost.dy
                    # bytter fart
                    i.dx, ghost.dx = ghost.dx, i.dx
                    i.dy, ghost.dy = ghost.dy, i.dy


    def game_loop(self):
        if self.kjorer:
            self.sjekkKolisjon()
            self.flyttGhost()
            self.x += self.dx
            self.y += self.dy
            self.canvas.coords(self.spiller, self.x - r, self.y - r, self.x + r, self.y + r)            
            # for i in self.ghoster:
            #     i.x += i.dx
            #     i.y += i.dy
            #     self.canvas.coords(i,i.x - r, i.y - r, i.x + r, i.y + r)
            self.after(10, self.game_loop)

    def game_over(self):
        self.kjorer = False
        self.canvas.create_text(bredde/2,hoyde/2,text="Game over",fill="red",font=20)

    def flyttGhost(self):
        for i in self.ghoster:
            i.x += i.dx
            i.y += i.dy
            self.canvas.coords(i.ghost_id, i.x - r, i.y - r, i.x + r, i.y + r)            



    def lagSau(self,i=3):
        laget = 0

        while laget < i:
            blokk = Sau(self.canvas)
            nypos = self.canvas.coords(blokk.Sau_id)

            def overlapp(a,b):
                return (
                    a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <=b[3]
                )
            
            overlapp = any(overlapp(nypos,pos) for pos in self.blokkpos)

            if overlapp:
                self.canvas.delete(blokk.Sau_id)
                continue
            else:
                self.blokkpos.append(nypos)
                self.sauer.append(blokk)
                laget += 1

    def lagHinder(self,i=3):
        laget = 0

        while laget < i:
            blokk = Hinder(self.canvas)
            nypos = self.canvas.coords(blokk.hinder_id)

            def overlapp(a,b):
                return (
                    a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <=b[3]
                )
            
            overlapp = any(overlapp(nypos,pos) for pos in self.blokkpos)

            if overlapp:
                self.canvas.delete(blokk.hinder_id)
                continue
            else:
                self.blokkpos.append(nypos)
                self.hindrer.append(blokk)
                laget += 1

    def lagGhost(self, i=1):
        laget = 0

        while laget < i:
            blokk = Ghost(self.canvas)
            nypos = self.canvas.coords(blokk.ghost_id)

            def overlapp(a,b):
                return (
                    a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <=b[3]
                )
            
            overlapp = any(overlapp(nypos,pos) for pos in self.blokkpos)

            if overlapp:
                self.canvas.delete(blokk.ghost_id)
                continue
            else:
                self.blokkpos.append(nypos)
                self.ghoster.append(blokk)
                laget += 1

        # for _ in range(i):
        #     self.blokk = Sau(self.canvas)
        #     nySaupos = self.canvas.coords(self.blokk.Sau_id)
        #     # spillerpos = self.canvas.coords(self.spiller)            

        #     for a in range(len(self.saupos)):
        #         overlappX = nySaupos[2] >= self.saupos[a][0] and nySaupos[0] <= self.saupos[a][2]
        #         overlappY = nySaupos[1] <= self.saupos[a][3] and nySaupos[3] >= self.saupos[a][1]
        #         if overlappX and overlappY:
        #             self.canvas.delete(self.blokk.Sau_id)
        #             print("hey")
        #             self.lagSau()
        #         else:
        #             if self.canvas.coords(self.blokk.Sau_id) not in self.saupos:
        #                 self.saupos.append(self.canvas.coords(self.blokk.Sau_id))
        #                 self.sauer.append(self.blokk)
        #     if len(self.saupos) == 0:
        #         self.saupos.append(self.canvas.coords(self.blokk.Sau_id))
        #         self.sauer.append(self.blokk)
        # print(self.sauer)


class Sau:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = random.randint(bredde-200+r,bredde-r)
        self.y = random.randint(0+r,hoyde-r)
        self.Sau_id = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="yellow",outline="")

class Hinder:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = random.randint(200+r,bredde-200-r)
        self.y = random.randint(0+r,hoyde-r)
        self.hinder_id = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="grey",outline="")

class Ghost:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = random.randint(200+r,bredde-200-r)
        self.y = random.randint(0+r, hoyde-r)
        self.dx = 1
        self.dy = 1
        self.ghost_id = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="purple",outline="")


_ = Manic()
_.lagSau()
_.lagGhost()
_.lagHinder()
_.mainloop()
