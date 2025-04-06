import tkinter as tk
from random import randint

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 500
canvas_height = 500
canvas_width = windowWidth
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.

# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,height=canvas_height, background="green")
canvas.pack()


class Spill:
    def __init__(self, objekter=[]) -> None:
        self.objekter = objekter
        self.player = None
    
    def tegn(self):
        """ Tegner alle objekter i listen"""
        self.player.tegn()
    
    def fjernOgOppdater(self):
        """# Fjern alle objekter i listen og oppdater"""
        for obj in self.objekter:
            obj.fjern()
            obj.oppdater()  # Oppdaterer posisjon og eventuelt fart.
        self.player.fjern()
        self.player.oppdater()
    
    def kollisjon(self):
        """Sjekker kollisjon med vegger og med andre objekter."""
        for obj in self.objekter:
            obj.sjekkKollisjonVegger()
        self.player.sjekkKollisjonVegger()
        # Sjekker kollisjon mellom objekt og heksa ved å sende ved en liste med objekter som kollisjon skal sjekkes for.
        for obj in self.objekter:
            self.player.sjekkKollisjon(self,obj)
    
    def slett(self,objekt):
        self.objekter.remove(objekt)
    

class Objekt:
    """
        Firkantet objekt som er superklasse.
        Inneholder basismetodene som tegning, fjerning, kollisjonshåndtering.
        Kollisjon må håndteres ved å se på overlapp av to rektangler. Ikke Pythagoras som for sirkel.
    """
    def __init__(self, navn,
                 xpos=canvas_width/2,
                 ypos=canvas_height/2,
                 x_fart=0, y_fart=0,
                 fill="#ffff00", outline="#ffff00",
                 lengde = 20, bredde = 15):
        self.l = lengde
        self.b = bredde  # bredde
        self.x = xpos
        self.y = ypos  # Plasserer i midten av vinduet
        self.fill = fill
        self.outline = outline
        self.x_fart = x_fart
        self.y_fart = y_fart
        self.x_retning = 1
        self.y_retning = 0
        self.tag = navn

    def __str__(self):
        return f"{self.tag}"

    def sjekkKollisjonVegger(self):
        """Sjekker kollisjon med alle vegger"""
        global isRunning
        # bunnen
        if self.y + self.b >= canvas_height:
            self.y_retning = -1
            # Flytter seg selv HELT vekk fra vegg i tilfelle den setter seg fast.
            self.y = canvas_height - self.b
        # venstre
        if self.x - self.l <= 0:
            self.x_retning = 1
            self.x = self.l
        # topp
        if self.y - self.b <= 0:
            self.y_retning = 1
            self.y = self.b
        # høyre
        if self.x + self.l >= canvas_width:
            self.x_retning = -1
            self.x = canvas_width - self.l
            

    def tegn(self):
        canvas.create_rectangle(self.x-self.l, self.y-self.b,
                           self.x+self.l, self.y+self.b,
                           fill=self.fill, outline=self.outline, tags=self.tag)

    def fjern(self):
        canvas.delete(self.tag)

    def oppdater(self):
        self.x += self.x_fart
        self.y += self.y_fart

class Player(Objekt):
    def __init__(self):
        self.x_retning = 1
        self.y_retning = 0
        super().__init__("Player", 40,canvas_height-40, 2, 2, "dodgerblue", "dodgerblue", 20, 20)
    
    def oppdater(self):
        self.x += self.x_fart * self.x_retning
        self.y += self.y_fart * self.y_retning
    

spill = Spill()

spill.player = Player()

def handle_avslutt(event):
    window.destroy()


def processKeypress(evt):
    key = evt.keysym
    print(f'key: {key}')
    if key == "Left":
        spill.player.x_retning = -1
        spill.player.y_retning = 0
    elif key == "Up":
        spill.player.x_retning = 0
        spill.player.y_retning = -1
    elif key == "Right":
        spill.player.x_retning = 1
        spill.player.y_retning = 0
    elif key == "Down":
        spill.player.x_retning = 0
        spill.player.y_retning = 1


# Tastetrykk
window.bind("<Key>",processKeypress)


# Her animinerer vi
teller = 0
isRunning = True
while isRunning == True:
    # Tegn alle objekter i listen
    spill.tegn()
    canvas.after(1)  # venter 100 ms
    canvas.update()
    # Fjern alle sirkler i listen og oppdater posisjoner og fart for objeker
    spill.fjernOgOppdater()
    # Sjekker kollisjon med vegger og med andre objekter.
    spill.kollisjon()
    teller += 1

spill.tegn()


window.mainloop()