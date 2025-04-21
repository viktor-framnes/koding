
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
        self.sauberer = False
        self.hvilke = 0
        self.poeng = 0

        self.ghoster = []
        self.ghostpos = []
        self.hinderpos = []
        self.sauer = []
        self.saupos = []



        self.resizable(False, False)
        self.minsize(bredde,hoyde)
        self.canvas = tk.Canvas(self,bg="black",width=bredde,height=hoyde)
        self.canvas.pack(expand=True)
        self.venstrebrett = self.canvas.create_rectangle(0,0,200,hoyde,fill="red",outline="")
        self.hoyrebrett = self.canvas.create_rectangle(bredde-200,0,bredde,hoyde,fill="blue",outline="")
        self.spiller = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="green",outline="")
        self.tekst = self.canvas.create_text(50,50,text=f"{self.poeng}",fill="black",font=("Pursia",20,"bold"))
        # self.canvas.tag_raise(self.tekst)

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
        # sjekker spiller med vegger
        if self.x+r >= bredde:
            self.x = bredde - r
        if self.y+r >= hoyde:
            self.y = hoyde - r
        if self.x-r <= 0:
            self.x = r
        if self.y-r <= 0:
            self.y = r

        spiller = self.canvas.coords(self.spiller)

        if self.sauberer:
            for sau_coords in self.saupos:
                if self.saupos[self.hvilke] == sau_coords:
                    continue
                if self.overlapp(spiller,sau_coords):
                    self.game_over()   

        for teller, i in enumerate(self.ghoster):
            overlappX = spiller[2] >= self.ghostpos[teller][0] and spiller[0] <= self.ghostpos[teller][2]
            overlappY = spiller[1] <= self.ghostpos[teller][3] and spiller[3] >= self.ghostpos[teller][1]
            if overlappX and overlappY:
                self.game_over()

            if i.y + r >= hoyde:
                i.dy = -i.dy
                i.y = hoyde - r
            if i.x - r <= 200:
                i.dx = -i.dx
                i.x = r+200
            if i.y - r <= 0:
                i.dy = -i.dy
                i.y = r
            if i.x + r >= bredde-200:
                i.dx = -i.dx
                i.x = bredde - r - 200
                

    def overlapp(self,a,b):
        return (
            a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <=b[3]
        )

    def lagSau(self,i=3):
        laget = 0
        while laget < i:
            blokk = Sau(self.canvas)
            nypos = self.canvas.coords(blokk.Sau_id)
            overlapp = any(self.overlapp(nypos,pos) for pos in self.saupos)

            if overlapp:
                self.canvas.delete(blokk.Sau_id)
                continue
            else:
                self.saupos.append(nypos)
                self.sauer.append(blokk)
                laget += 1
    
    def lagHinder(self,i=3):
        laget = 0
        while laget < i:
            blokk = Hinder(self.canvas)
            nypos = self.canvas.coords(blokk.hinder_id)
            overlapp = any(self.overlapp(nypos,pos) for pos in self.hinderpos)

            if overlapp:
                self.canvas.delete(blokk.hinder_id)
                continue
            else:
                self.hinderpos.append(nypos)
                laget += 1

    def lagGhost(self,i=1):
        laget = 0
        while laget < i:
            blokk = Ghost(self.canvas)
            nypos = self.canvas.coords(blokk.ghost_id)
            overlapp = any(self.overlapp(nypos,pos) for pos in self.ghostpos)

            if overlapp:
                self.canvas.delete(blokk.ghost_id)
                continue
            else:
                self.ghostpos.append(nypos)
                self.ghoster.append(blokk)
                laget += 1

    def flyttGhost(self):
        for teller, i in enumerate(self.ghoster):
            i.x += i.dx
            i.y += i.dy
            self.canvas.coords(i.ghost_id, i.x - r, i.y - r, i.x + r, i.y + r)
            self.ghostpos[teller] = self.canvas.coords(i.ghost_id)

    def yay(self):
        self.poeng += 1
        self.canvas.delete(self.sauer[self.hvilke].Sau_id)
        self.sauer.pop(self.hvilke)
        self.saupos.pop(self.hvilke)
        self.ds = 4
        self.lagSau(1)
        self.lagHinder(1)
        self.lagGhost()
        self.canvas.itemconfig(self.tekst,text=f"{self.poeng}")
        self.sauberer = False


    def game_loop(self):
        if self.kjorer:
            ny_x = self.x + self.dx
            ny_y = self.y + self.dy

            # Midlertidige koordinater
            ny_coords = [ny_x - r, ny_y - r, ny_x + r, ny_y + r]

            # Sjekk om ny posisjon kolliderer med noen hinder
            kollisjon = False
            for hinder_coords in self.hinderpos:
                if self.overlapp(ny_coords, hinder_coords):
                    kollisjon = True
                    break

            # Hvis ingen kollisjon, så oppdater posisjon
            if not kollisjon:
                self.x = ny_x
                self.y = ny_y

            self.sjekkKolisjon()

            if self.sauberer != True:
                mid_coords = self.canvas.coords(self.spiller)
                for teller, sau_coords in enumerate(self.saupos):
                    if self.overlapp(mid_coords,sau_coords):
                        self.sauberer = True
                        self.ds = 2.5
                        self.hvilke = teller


            self.flyttGhost()
            self.canvas.coords(self.spiller, self.x - r, self.y - r, self.x + r, self.y + r)
            if self.sauberer:
                self.canvas.coords(self.sauer[self.hvilke].Sau_id, self.x + r, self.y - r, self.x + 3*r, self.y + r)
                if self.x < 185:
                    self.yay()
            self.after(10, self.game_loop)



    def game_over(self):
        self.kjorer = False
        self.canvas.itemconfig(self.tekst,text=f"{self.poeng}")
        self.canvas.create_text(bredde/2,hoyde/2,text="Game over",fill="red",font=20)


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
        self.ghost_id = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="purple",outline="")
        self.dx = 1
        self.dy = 1



_ = Manic()
_.lagSau()
_.lagGhost()
_.lagHinder()
_.mainloop()