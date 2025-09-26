import tkinter as tk
import math

bredde = 1000
hoyde = 500
r = 15
muligeykoor = [hoyde/2-100,hoyde/2-50,hoyde/2,hoyde/2+50,hoyde/2+100]

class GameObject:
    def __init__(self, canvas, x, y, farge,liste=[]):
        self.canvas = canvas
        self.liste = liste
        self.x = x
        self.y = y
        self.tilstand = 0
        self.id = self.canvas.create_rectangle(x - r, y - r, x + r, y + r, fill=farge, outline="")
        
    def coords(self):
        return self.canvas.coords(self.id)

    def flytt_til(self, x, y):
        self.x, self.y = x, y
        self.canvas.coords(self.id, x - r, y - r, x + r, y + r)
 
class Båt(GameObject):
    def __init__(self, canvas,liste):
        startposx = 200+r+5
        startposy = hoyde/2 
        super().__init__(canvas, startposx, startposy, "brown")
        self.canvas.delete(self.id)
        punkter = [200+5,hoyde/2+50,200+5,hoyde/2-50,205+120,hoyde/2-50,205+120+30,hoyde/2,205+120,hoyde/2+50]
        self.id = self.canvas.create_polygon(punkter, fill="brown", outline="")

class Hund(GameObject):
    def __init__(self, canvas,liste):
        super().__init__(canvas, r+10, hoyde/2-100, "red")
        self.startposx = r+10
        self.startposy = hoyde/2-100

class Ulv(GameObject):
    def __init__(self, canvas,liste):
        super().__init__(canvas, r+10, muligeykoor[len(liste)-1], "grey")
        self.startposx = r+10
        self.startposy = hoyde/2-50

class Geit(GameObject):
    def __init__(self, canvas,liste):
        super().__init__(canvas, r+10, hoyde/2+50, "pink")
        self.startposx = r+10
        self.startposy = muligeykoor[3]

class Kål(GameObject):
    def __init__(self, canvas,liste):
        super().__init__(canvas, r+10, hoyde/2+100, "lightgreen")
        self.startposx = r+10
        self.startposy = muligeykoor[4]

class Bonde(tk.Tk):
    def __init__(self):
        super().__init__()
        self.kjorer = True
        self.x, self.y = 70, hoyde / 2
        self.dx = self.dy = 0
        self.ds = 6
        self.aktive_taster = []
        self.bærer = False
        self.hvilke = 0

        self.objekter = []

        self.resizable(False, False)
        self.minsize(bredde, hoyde)
        self.canvas = tk.Canvas(self, bg="lightblue", width=bredde, height=hoyde)
        self.canvas.pack(expand=True)

        self.canvas.create_rectangle(0, 0, 200, hoyde, fill="green", outline="")
        self.canvas.create_rectangle(bredde - 200, 0, bredde, hoyde, fill="green", outline="")
        self.leveringszone = self.canvas.create_rectangle(150,hoyde/2-25,200,hoyde/2+25,fill="",outline="black")
        self.spiller = self.canvas.create_rectangle(self.x - r, self.y - r, self.x + r, self.y + r, fill="brown", outline="")
        self.båtplasser = []
        self.båtkoords = [230, 265, 300]
        
        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)



        self.lag_objekter(Båt, self.objekter,len(self.objekter)+1)
        self.lag_objekter(Hund, self.objekter,len(self.objekter)+1)
        self.lag_objekter(Ulv, self.objekter,len(self.objekter)+2)
        self.lag_objekter(Geit, self.objekter,len(self.objekter)+1)
        self.lag_objekter(Kål, self.objekter,len(self.objekter)+1)

        self.bind("<Escape>",self.slipp)
        self.bind("<space>",self.velg)

        self.game_loop()

    def key_press(self, event):
        t = event.keysym
        if t in ["Up", "Down", "Left", "Right"]:
            if t in self.aktive_taster:
                self.aktive_taster.remove(t)
            self.aktive_taster.append(t)
        self.oppdater_rettning()

    def key_release(self, event):
        t = event.keysym
        if t in self.aktive_taster:
            self.aktive_taster.remove(t)
        self.oppdater_rettning()

    def oppdater_rettning(self):
        if not self.aktive_taster:
            self.dx = self.dy = 0
            return
        t = self.aktive_taster[-1]
        if len(self.aktive_taster) >= 2:
            f = self.aktive_taster[-2]
            z = t+f
            d = math.sqrt(8) 
            self.dx, self.dy = {
                "LeftUp": (-d, -d),
                "UpLeft": (-d, -d),
                "RightUp": (d, -d),
                "UpRight": (d, -d),
                "LeftDown": (-d, d),
                "DownLeft": (-d, d),
                "RightDown": (d, d),
                "DownRight": (d, d),
                "RightLeft": (self.ds,0),
                "LeftRight": (-self.ds,0),
                "UpDown": (0, -self.ds),
                "DownUp": (0, self.ds),
            }[z]
        else:
            self.dx, self.dy = {
                "Up": (0, -self.ds),
                "Down": (0, self.ds),
                "Left": (-self.ds, 0),
                "Right": (self.ds, 0)
            }[t]

    def overlapp(self, a, b):
        return a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <= b[3]

    def overlapper_noen(self, coords, objekter):
        return any(self.overlapp(coords, obj.coords()) for obj in objekter)

    def lag_objekter(self, klasse, liste, antall):
        while len(liste) < antall:
            obj = klasse(self.canvas,liste)
            if not self.overlapper_noen(obj.coords(), liste):
                liste.append(obj)
            else:
                self.canvas.delete(obj.id)

    def flytt_spiller(self):
        ny_x = self.x + self.dx
        ny_y = self.y + self.dy
        ny_coords = [ny_x - r, ny_y - r, ny_x + r, ny_y + r]
        # if not self.overlapper_noen(ny_coords, self.objekter):
        self.x = max(r, min(200 - r, ny_x))
        self.y = max(r, min(hoyde - r, ny_y))
        self.canvas.coords(self.spiller, self.x - r, self.y - r, self.x + r, self.y + r)



    def game_loop(self):
        if not self.kjorer:
            return

        self.flytt_spiller()
        spiller_coords = self.canvas.coords(self.spiller)

        if not self.bærer:
            for i, obj in enumerate(self.objekter):
                if self.overlapp(spiller_coords, obj.coords()):
                    self.bærer = True
                    obj.tilstand = 1
                    self.hvilke = i
                    break

        if self.bærer:
            self.objekter[self.hvilke].flytt_til(self.x-2*r,self.y)

        self.after(10, self.game_loop)

    def game_over(self):
        self.kjorer = False
        self.canvas.create_text(bredde / 2, hoyde / 2, text="Game over", fill="red", font=20)



    def slipp(self,e):
        for i, obj in enumerate(self.objekter):
            if obj.tilstand == 1:
                obj.tilstand = 0
                self.bærer = False
                obj.flytt_til(r+10,muligeykoor[i-1])


    def velg(self,e):
        if not self.bærer:
            return
        if self.overlapp(self.canvas.coords(self.spiller),self.canvas.coords(self.leveringszone)):
            if len(self.båtplasser) < 3:    
                for i, obj in enumerate(self.objekter):
                    if obj.tilstand == 1:
                        obj.tilstand = 0
                        self.bærer = False
                        obj.flytt_til(self.båtkoords[len(self.båtplasser)],hoyde/2)
                        self.båtplasser.append(obj)
            else:
                print("full båt")

if __name__ == "__main__":
    Bonde().mainloop()