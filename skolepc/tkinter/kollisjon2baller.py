import tkinter as tk

window = tk.Tk()

# konstanter for window
bredde = 500
hoyde = 600
canvasbredde = 500
canvashoyde = 500
window.minsize(bredde,hoyde)

# frame 1
ramme1 = tk.Frame(window)
ramme1.pack()

# header
header = tk.Canvas(ramme1,
                   width=bredde,
                   height=100)
header.pack()
overskrift = tk.Label(header,
                      text="Kollisjon mellom to baller",
                      font=("Arial",20))
overskrift.pack()

# hovedramme
ramme2 = tk.Frame(window)
ramme2.pack()
canvas = tk.Canvas(ramme2,width=canvasbredde,height=canvashoyde,background="lightblue")
canvas.pack()

# ball klasse, informasjon om x-posisjon, y-posisjon, retning osv.
class Ball:
    def __init__(self,navn,
                xpos = canvasbredde/2,
                ypos = canvashoyde/2,
                deltax = 1,
                deltay = 0,
                fill = "yellow",
                outline="white"
                ):
        self.radius = 5
        self.x = xpos
        self.y = ypos
        self.dx = deltax
        self.dy = deltay
        self.fill = fill
        self.outline = outline
        self.tag = navn

    def sjekk_kollisjon(self, baller):
        """Sjekker kollisjon med alle vegger"""
        global isRunning
        # bunnen
        if self.y + self.radius >= canvashoyde:
            self.dy = -self.dy
            # Flytter seg selv HELT vekk fra vegg i tilfelle den setter seg fast.
            self.y = canvashoyde - self.radius
        # venstre
        if self.x - self.radius <= 0:
            self.dx = -self.dx
            self.x = self.radius
        # topp
        if self.y - self.radius <= 0:
            self.dy = -self.dy
            self.y = self.radius
        # høyre
        if self.x + self.radius >= canvasbredde:
            self.dx = -self.dx
            self.x = canvasbredde - self.radius
        # Sjekk kollisjon mot alle andre baller i listen
        for ball in baller:
            if ball.tag == self.tag:  # Hvis ballen som sjekkes er seg selv.
                continue
            # Beregner avstand mellom sirklene med pythagoras.
            dx = abs(ball.x - self.x)
            dy = abs(ball.y - self.y)
            d = (dx**2 + dy**2)**0.5
            if d <= ball.radius + self.radius:
                print(f"{self.tag} mot {ball.tag}")
                # forenklet bevegelsesmengde
                self.x -= self.dx
                ball.x -= ball.dx
                self.y -= self.dy
                ball.y -= ball.dy
                # bytter fart
                tempx = self.dx
                tempy = self.dy
                self.dx = ball.dx
                self.dy = ball.dy
                ball.dx = tempx
                ball.dy = tempy

                """Alternativ løsning:"""
                # # Flytt sirklene like langt vekk til hver side før fart settes motsatt.
                # self.x -= self.dx
                # self.dx = -self.dx
                # self.y -= self.dy
                # self.dy = -self.dy
                # ball.x -= ball.dx
                # ball.dx = -ball.dx
                # ball.y -= ball.dy
                # ball.dy = -ball.dy


    def tegnBall(self):
        canvas.create_oval(self.x-self.radius, # positiv retning for x er mot høyre 
                           self.y-self.radius, # positiv retning for y er ned over
                           self.x+self.radius,
                           self.y+self.radius,
                           fill = self.fill,
                           outline = self.outline,
                           tags=self.tag                           
                           )
    def fjernBall(self):
        canvas.delete(self.tag)

    def oppdaterBall(self):
        self.x += self.dx
        self.y += self.dy

ball1 = Ball("ball1",canvasbredde/1.5,canvashoyde/2,-3,1)
ball2 = Ball("ball2",canvasbredde/4,canvashoyde/2,3,-1,"blue")
# ball3 = Ball("ball3",canvasbredde/4,canvashoyde/4,3,2,"green")
# ball4 = Ball("ball4",canvasbredde/0.5,canvashoyde/2,-3,1,"red")
# ball5 = Ball("ball5",canvasbredde/3,canvashoyde/2,3,-1,"orange")
# ball6 = Ball("ball6",canvasbredde/2,canvashoyde/4,3,2,"purple")
# ball7 = Ball("ball7",canvasbredde/3.5,canvashoyde/2,-3,1,"black")
# ball8 = Ball("ball8",canvasbredde/2.5,canvashoyde/2,3,-1,"grey")
# ball9 = Ball("ball9",canvasbredde/1.25,canvashoyde/4,3,2,"lightgrey")
# ball10 = Ball("ball10",canvasbredde/1.5,canvashoyde/2,-3,1)
# ball11 = Ball("ball11",canvasbredde/4,canvashoyde/1.5,3,-1,"blue")
# ball12 = Ball("ball12",canvasbredde/4,canvashoyde/2.5,3,2,"green")
# ball13 = Ball("ball13",canvasbredde/0.5,canvashoyde/3.5,-3,1,"red")
# ball14 = Ball("ball14",canvasbredde/3,canvashoyde/3,3,-1,"orange")
# ball15 = Ball("ball15",canvasbredde/2,canvashoyde/4.2,3,2,"purple")
# ball16 = Ball("ball16",canvasbredde/3.5,canvashoyde/5,-3,1,"black")
# ball17 = Ball("ball17",canvasbredde/2.5,canvashoyde/1,3,-1,"grey")
# ball18 = Ball("ball18",canvasbredde/1.25,canvashoyde/0.5,3,2,"lightgrey")

# baller = [ball1,ball2,ball3,ball4,ball5,ball6,ball7,ball8,ball9,ball10,ball11,ball12,ball13,ball14,ball15,ball16,ball17,ball18]
baller = [ball1,ball2]

# avslutt footer
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer,text="Avslutt")
avslutt.pack()

# funksjonalitet til avslutt knapp
def avsluttKnapp(e):
    window.destroy()

avslutt.bind("<Button-1>",avsluttKnapp)

# animasjon
isRunning = True
while isRunning:
    # tegner ballene
    for ball in baller:
        ball.tegnBall() 
        ball.oppdaterBall()
    canvas.after(10)
    canvas.update()

    # fjerner ballene
    for ball in baller:
        ball.fjernBall()
        ball.oppdaterBall

    # sjekker for kollisjon
    for ball in baller:
        ball.sjekk_kollisjon(baller)



window.mainloop()