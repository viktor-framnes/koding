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
        self.ds = 2
        self.aktive_taster = []
        self.saupos = []
        self.sauer = []
        self.hinderpos = []
        self.hindrer = []

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
        for i in range(len(self.hinderpos)):
            overlappX = spiller[2] >= self.hinderpos[i][0] and spiller[0] <= self.hinderpos[i][2]
            overlappY = spiller[1] <= self.hinderpos[i][3] and spiller[3] >= self.hinderpos[i][1]

            if overlappX and overlappY:
                self.game_over()

    def game_loop(self):
        if self.kjorer:
            self.sjekkKolisjon()
            self.x += self.dx
            self.y += self.dy
            self.canvas.coords(self.spiller, self.x - r, self.y - r, self.x + r, self.y + r)
            self.after(10, self.game_loop)

    def game_over(self):
        self.kjorer = False
        self.canvas.create_text(bredde/2,hoyde/2,text="Game over",fill="red",font=20)

    def lagSau(self,i=3):
        laget = 0

        while laget < i:
            blokk = Sau(self.canvas)
            nysaupos = self.canvas.coords(blokk.Sau_id)

            def overlapp(a,b):
                return (
                    a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <=b[3]
                )
            
            overlappSau = any(overlapp(nysaupos,pos) for pos in self.saupos)

            if overlappSau:
                self.canvas.delete(blokk.Sau_id)
                print("hey")
                continue
            else:
                self.saupos.append(nysaupos)
                self.sauer.append(blokk)
                laget += 1

    def lagHinder(self,i=3):
        laget = 0

        while laget < i:
            blokk = Hinder(self.canvas)
            nyhinderpos = self.canvas.coords(blokk.hinder_id)

            def overlapp(a,b):
                return (
                    a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <=b[3]
                )
            
            overlappHinder = any(overlapp(nyhinderpos,pos) for pos in self.hinderpos)

            if overlappHinder:
                self.canvas.delete(blokk.hinder_id_id)
                print("hey")
                continue
            else:
                self.hinderpos.append(nyhinderpos)
                self.hindrer.append(blokk)
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


_ = Manic()
_.lagSau()
_.lagHinder()
_.mainloop()
