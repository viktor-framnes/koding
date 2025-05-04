import tkinter as tk
import random
import math

bredde = 1000
hoyde = 500
r = 15

class GameObject:
    def __init__(self, canvas, x, y, farge):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = self.canvas.create_rectangle(x - r, y - r, x + r, y + r, fill=farge, outline="")

    def coords(self):
        return self.canvas.coords(self.id)

    def flytt_til(self, x, y):
        self.x, self.y = x, y
        self.canvas.coords(self.id, x - r, y - r, x + r, y + r)

class Ghost(GameObject):
    def __init__(self, canvas):
        x = random.randint(200 + r, bredde - 200 - r)
        y = random.randint(r, hoyde - r)
        super().__init__(canvas, x, y, "purple")
        self.dx = 1
        self.dy = 1

    def oppdater(self):
        self.x += self.dx
        self.y += self.dy

        if self.y + r >= hoyde or self.y - r <= 0:
            self.dy *= -1
        if self.x - r <= 200 or self.x + r >= bredde - 200:
            self.dx *= -1

        self.flytt_til(self.x, self.y)

class Hinder(GameObject):
    def __init__(self, canvas):
        x = random.randint(200 + r, bredde - 200 - r)
        y = random.randint(r, hoyde - r)
        super().__init__(canvas, x, y, "grey")

class Sau(GameObject):
    def __init__(self, canvas):
        x = random.randint(bredde - 200 + r, bredde - r)
        y = random.randint(r, hoyde - r)
        super().__init__(canvas, x, y, "yellow")

class Manic(tk.Tk):
    def __init__(self):
        super().__init__()
        self.kjorer = True
        self.x, self.y = 50, hoyde / 2
        self.dx = self.dy = 0
        self.ds = 4
        self.poeng = 0
        self.sauberer = False
        self.hvilke = 0
        self.aktive_taster = []

        self.ghoster = []
        self.hindre = []
        self.sauer = []

        self.resizable(False, False)
        self.minsize(bredde, hoyde)
        self.canvas = tk.Canvas(self, bg="black", width=bredde, height=hoyde)
        self.canvas.pack(expand=True)

        self.canvas.create_rectangle(0, 0, 200, hoyde, fill="red", outline="")
        self.canvas.create_rectangle(bredde - 200, 0, bredde, hoyde, fill="blue", outline="")
        self.spiller = self.canvas.create_rectangle(self.x - r, self.y - r, self.x + r, self.y + r, fill="green", outline="")
        self.tekst = self.canvas.create_text(50, 50, text=f"{self.poeng}", fill="black", font=("Pursia", 20, "bold"))

        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)

        self.lag_objekter(Sau, self.sauer, 3)
        self.lag_objekter(Hinder, self.hindre, 3)
        # self.lag_objekter(Ghost, self.ghoster, 1)

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
            obj = klasse(self.canvas)
            if not self.overlapper_noen(obj.coords(), liste):
                liste.append(obj)
            else:
                self.canvas.delete(obj.id)

    def flytt_spiller(self):
        ny_x = self.x + self.dx
        ny_y = self.y + self.dy
        ny_coords = [ny_x - r, ny_y - r, ny_x + r, ny_y + r]
        if not self.overlapper_noen(ny_coords, self.hindre):
            self.x = max(r, min(bredde - r, ny_x))
            self.y = max(r, min(hoyde - r, ny_y))
            self.canvas.coords(self.spiller, self.x - r, self.y - r, self.x + r, self.y + r)

    def sjekk_kollisjoner(self):
        spiller_coords = self.canvas.coords(self.spiller)

        if self.sauberer:
            for i, sau in enumerate(self.sauer):
                if i != self.hvilke and self.overlapp(spiller_coords, sau.coords()):
                    self.game_over()

        for ghost in self.ghoster:
            if self.overlapp(spiller_coords, ghost.coords()):
                self.game_over()

    def yay(self):
        self.poeng += 1
        self.canvas.delete(self.sauer[self.hvilke].id)
        self.sauer.pop(self.hvilke)
        self.ds = 4
        self.lag_objekter(Sau, self.sauer, len(self.sauer) + 1)
        self.lag_objekter(Hinder, self.hindre, len(self.hindre) + 1)
        self.lag_objekter(Ghost, self.ghoster, len(self.ghoster) + 1)
        self.canvas.itemconfig(self.tekst, text=f"{self.poeng}")
        self.sauberer = False

    def game_loop(self):
        if not self.kjorer:
            return

        # print(self.aktive_taster)

        self.flytt_spiller()
        self.sjekk_kollisjoner()

        spiller_coords = self.canvas.coords(self.spiller)
        if not self.sauberer:
            for i, sau in enumerate(self.sauer):
                if self.overlapp(spiller_coords, sau.coords()):
                    self.sauberer = True
                    self.ds = 2.5
                    self.hvilke = i
                    break

        for ghost in self.ghoster:
            ghost.oppdater()

        if self.sauberer:
            self.sauer[self.hvilke].flytt_til(self.x + 2 * r, self.y)
            if self.x < 185:
                self.yay()

        self.after(10, self.game_loop)

    def game_over(self):
        self.kjorer = False
        self.canvas.itemconfig(self.tekst, text=f"{self.poeng}")
        self.canvas.create_text(bredde / 2, hoyde / 2, text="Game over", fill="red", font=20)

if __name__ == "__main__":
    Manic().mainloop()
