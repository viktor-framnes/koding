import tkinter as tk
import random

bredde = 1000
hoyde = 500
r = 15

class Manic(tk.Tk):
    def __init__(self):
        super().__init__()
        self.kjorer = True
        self.x, self.y = 50, hoyde / 2
        self.dx = self.dy = 0
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
        self.minsize(bredde, hoyde)
        self.canvas = tk.Canvas(self, bg="black", width=bredde, height=hoyde)
        self.canvas.pack(expand=True)

        self.canvas.create_rectangle(0, 0, 200, hoyde, fill="red", outline="")
        self.canvas.create_rectangle(bredde - 200, 0, bredde, hoyde, fill="blue", outline="")
        self.spiller = self.canvas.create_rectangle(self.x - r, self.y - r, self.x + r, self.y + r, fill="green", outline="")
        self.tekst = self.canvas.create_text(50, 50, text=f"{self.poeng}", fill="black", font=("Pursia", 20, "bold"))

        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)

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
        if t == "Up": self.dx, self.dy = 0, -self.ds
        elif t == "Down": self.dx, self.dy = 0, self.ds
        elif t == "Left": self.dx, self.dy = -self.ds, 0
        elif t == "Right": self.dx, self.dy = self.ds, 0

    def sjekkKolisjon(self):
        # Vegg-kollisjon
        self.x = min(max(self.x, r), bredde - r)
        self.y = min(max(self.y, r), hoyde - r)

        spiller = self.canvas.coords(self.spiller)

        if self.sauberer:
            for i, sau_coords in enumerate(self.saupos):
                if i == self.hvilke:
                    continue
                if self.overlapp(spiller, sau_coords):
                    self.game_over()

        for i, ghost in enumerate(self.ghoster):
            if self.overlapp(spiller, self.ghostpos[i]):
                self.game_over()

            if ghost.y + r >= hoyde:
                ghost.dy *= -1
                ghost.y = hoyde - r
            if ghost.x - r <= 200:
                ghost.dx *= -1
                ghost.x = 200 + r
            if ghost.y - r <= 0:
                ghost.dy *= -1
                ghost.y = r
            if ghost.x + r >= bredde - 200:
                ghost.dx *= -1
                ghost.x = bredde - 200 - r

    def overlapp(self, a, b):
        return a[2] >= b[0] and a[0] <= b[2] and a[3] >= b[1] and a[1] <= b[3]

    def lagSau(self, i=3):
        while i:
            blokk = Sau(self.canvas)
            nypos = self.canvas.coords(blokk.Sau_id)
            if any(self.overlapp(nypos, pos) for pos in self.saupos):
                self.canvas.delete(blokk.Sau_id)
                continue
            self.saupos.append(nypos)
            self.sauer.append(blokk)
            i -= 1

    def lagHinder(self, i=3):
        while i:
            blokk = Hinder(self.canvas)
            nypos = self.canvas.coords(blokk.hinder_id)
            if any(self.overlapp(nypos, pos) for pos in self.hinderpos):
                self.canvas.delete(blokk.hinder_id)
                continue
            self.hinderpos.append(nypos)
            i -= 1

    def lagGhost(self, i=1):
        while i:
            blokk = Ghost(self.canvas)
            nypos = self.canvas.coords(blokk.ghost_id)
            if any(self.overlapp(nypos, pos) for pos in self.ghostpos):
                self.canvas.delete(blokk.ghost_id)
                continue
            self.ghoster.append(blokk)
            self.ghostpos.append(nypos)
            i -= 1

    def flyttGhost(self):
        for i, ghost in enumerate(self.ghoster):
            ghost.x += ghost.dx
            ghost.y += ghost.dy
            self.canvas.coords(ghost.ghost_id, ghost.x - r, ghost.y - r, ghost.x + r, ghost.y + r)
            self.ghostpos[i] = self.canvas.coords(ghost.ghost_id)

    def yay(self):
        self.poeng += 1
        self.canvas.delete(self.sauer[self.hvilke].Sau_id)
        self.sauer.pop(self.hvilke)
        self.saupos.pop(self.hvilke)
        self.ds = 4
        self.lagSau(1)
        self.lagHinder(1)
        self.lagGhost()
        self.canvas.itemconfig(self.tekst, text=f"{self.poeng}")
        self.sauberer = False

    def game_loop(self):
        if not self.kjorer:
            return

        ny_x, ny_y = self.x + self.dx, self.y + self.dy
        ny_coords = [ny_x - r, ny_y - r, ny_x + r, ny_y + r]

        if not any(self.overlapp(ny_coords, h) for h in self.hinderpos):
            self.x, self.y = ny_x, ny_y

        self.sjekkKolisjon()

        if not self.sauberer:
            spiller_coords = self.canvas.coords(self.spiller)
            for i, sau_coords in enumerate(self.saupos):
                if self.overlapp(spiller_coords, sau_coords):
                    self.sauberer = True
                    self.ds = 2.5
                    self.hvilke = i

        self.flyttGhost()
        self.canvas.coords(self.spiller, self.x - r, self.y - r, self.x + r, self.y + r)

        if self.sauberer:
            self.canvas.coords(
                self.sauer[self.hvilke].Sau_id, self.x + r, self.y - r, self.x + 3*r, self.y + r)
            if self.x < 185:
                self.yay()

        self.after(10, self.game_loop)

    def game_over(self):
        self.kjorer = False
        self.canvas.itemconfig(self.tekst, text=f"{self.poeng}")
        self.canvas.create_text(bredde / 2, hoyde / 2, text="Game over", fill="red", font=20)


class Sau:
    def __init__(self, canvas):
        self.x = random.randint(bredde - 200 + r, bredde - r)
        self.y = random.randint(r, hoyde - r)
        self.Sau_id = canvas.create_rectangle(self.x - r, self.y - r, self.x + r, self.y + r, fill="yellow", outline="")


class Hinder:
    def __init__(self, canvas):
        self.x = random.randint(200 + r, bredde - 200 - r)
        self.y = random.randint(r, hoyde - r)
        self.hinder_id = canvas.create_rectangle(self.x - r, self.y - r, self.x + r, self.y + r, fill="grey", outline="")


class Ghost:
    def __init__(self, canvas):
        self.x = random.randint(200 + r, bredde - 200 - r)
        self.y = random.randint(r, hoyde - r)
        self.ghost_id = canvas.create_rectangle(self.x - r, self.y - r, self.x + r, self.y + r, fill="purple", outline="")
        self.dx = self.dy = 1


if __name__ == "__main__":
    spill = Manic()
    spill.lagSau()
    spill.lagGhost()
    spill.lagHinder()
    spill.mainloop()
