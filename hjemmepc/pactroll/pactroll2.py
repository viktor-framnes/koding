import tkinter as tk
import random

hoyde = 400
bredde = 400
r = 15

vindu = tk.Tk()
vindu.minsize(bredde,hoyde)

canvas = tk.Canvas(vindu)
canvas.configure(
    background="black",
    height=bredde,
    width=hoyde
)
canvas.pack()


x = bredde/2
y = hoyde/2
spiller = canvas.create_rectangle(x-r,y-r,x+r,y+r,fill="green")
dx = 0
dy = 0
ds = 3
kjorer = True

def hoyreklikk(e):
    bytteretning(ds,0)
def venstreklikk(e):
    bytteretning(-ds,0)
def nedklikk(e):
    bytteretning(0,ds)
def oppklikk(e):
    bytteretning(0,-ds)

vindu.bind("<KeyPress-Left>", venstreklikk)
vindu.bind("<KeyPress-Right>", hoyreklikk)
vindu.bind("<KeyPress-Up>", oppklikk)
vindu.bind("<KeyPress-Down>", nedklikk)

def bytteretning(nydx,nydy):
    global dx
    global dy
    dx = nydx
    dy = nydy

def sjekkkolisjon():
    global x
    global y
    global r
    global dx
    global dy
    global bredde
    global hoyde

    if ((y-r) <= 0) or ((y+r)) >= hoyde:
        gameover()

    if ((x-r) <=0) or ((x+r)) >= bredde:
        gameover()

def gameover():
    global kjorer
    global canvas
    global hoyde
    global bredde
    kjorer = False
    canvas.create_text(x, y, text="Game over", fill="red")


def gameloop():
    global x
    global y
    if kjorer == True:
        canvas.move(spiller,dx,dy)
        x += dx
        y += dy
        sjekkkolisjon()
        vindu.after(20,gameloop)

class Matbit():
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)
        self.matID = canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="yellow")

    
for i in range(3):
    Matbit()
gameloop()
vindu.mainloop()
