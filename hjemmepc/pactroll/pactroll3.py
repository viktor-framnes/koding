#importerer de bibliotekene vi trenger
import tkinter as tk
import random
 
# setter noen globale variabler som skal brukes både i pactroll klassen og matbit klassen
r = 15
hoyde = 400
bredde = 400
 
class Pactroll:
    def __init__(self):
        self.vindu = tk.Tk() # lager vinduet alt ligger oppi
        self.vindu.minsize(bredde,hoyde) # setter en minste størrelse lik canvaset sånt man ikke kan gjøre vinduet mindre en spillet
 
        self.canvas = tk.Canvas(self.vindu) # lager et canvas inni self.vindu, hvor vi tegner alt vi trenger i spillet. lerretet til spilelt
        self.canvas.config( # endrer canvas'et til det oppgaven vil
            background="black",
            height=hoyde,
            width=bredde
        )
        self.canvas.pack() # må pack() for å få den inn i vindu
 
        self.x = bredde/2 # setter startposisjon til spiller i x retning
        self.y = bredde/2 # setter startposisjon til spiller i y retning
        self.dx = 0 # setter start fart i x retning
        self.dy = 0 # setter start fart i y retning
        self.ds = 3 # setter farten til spiller
        self.kjorer = True # varibel for å vite som spille skal kjøres eller avsluttes
        self.spiller = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="green") # tegner spiller inn i canvaset og plasserer den i midten
 
        # binder piltaste trykk med deres funksjon, må huske å ikke ha () etter funksjonen når man binder. f.eks. self.venstreklikk() blir feil
        self.vindu.bind("<KeyPress-Left>", self.venstreklikk)
        self.vindu.bind("<KeyPress-Right>", self.hoyreklikk)
        self.vindu.bind("<KeyPress-Up>", self.oppklikk)
        self.vindu.bind("<KeyPress-Down>", self.nedklikk)
 
        self.gameloop() # har self.gameloop() på slutten av konstruktøren får å starte spillet, smart å ha den på slutten
 
    def bytteretning(self,nydx,nydy): # funksjon for å bytte fartsretningen til spiller. henter inn en ny fartsretning som parametere (nydx og nydy)
        # setter ny fartsretning
        self.dx = nydx
        self.dy = nydy
 
    # binder hver knapp opp til bytteretning() med parameterne som gjør at spiller går der vi vil.
    def hoyreklikk(self,e):
        self.bytteretning(self.ds,0)
    def venstreklikk(self,e):
        self.bytteretning(-self.ds,0)
    def nedklikk(self,e):
        self.bytteretning(0,self.ds)
    def oppklikk(self,e):
        self.bytteretning(0,-self.ds)
 
    # funksjon for å sjekke for kolisjon med vegger
    def sjekkkolison(self):
        if ((self.y-r) <= 0) or ((self.y+r)) >= hoyde: # sjekker om y-r er lik toppen (0) eller om y+r er lik bunnen av brettet (400 eller hoyde).
            self.gameover() # avslutter spiller med gameover funksjonen vi lagde
 
        if ((self.x-r) <=0) or ((self.x+r)) >= bredde: # samme bare med x i stedet. Må da bytte hoyde med bredde
            self.gameover() # avslutter spiller med gameover funksjonen vi lagde
 
    # game over funksjon
    def gameover(self):
        self.kjorer = False # avslutter spiller
        self.canvas.create_text(bredde/2,hoyde/2,text="Game over",fill="red") # lager game over teksten satt midt i canvaset
 
    # gameloopen som gjør at spilles kjøres
    def gameloop(self):
        if self.kjorer == True: # sjekker om spilles skal kjøres
            self.canvas.move(self.spiller,self.dx,self.dy) # flytter spilleren
            self.x += self.dx # endrer x koordinaten lik det vi flytta spilleren med, sånt vi har kontroll over hvor spilleren er
            self.y += self.dy # lik bare med y koordinaten
            self.sjekkkolison() # sjekker for kolisjon etter hver gang vi flytter spilleren
            self.vindu.after(20,self.gameloop) # venter bitte litt før vi kjører spillet igjen
 
# siden vi skal lage flere matbiter, så lager vi en oppskrift for matbitene (altså klassen Matbit)
class Matbit():
    def __init__(self,canvas): # bestemmer egenskapene til matbiten
        # setter x og y koordinatene et tilfeldig sted på canvas'et
        self.x = random.randint(0, bredde)  
        self.y = random.randint(0, hoyde)
        self.matID = canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="yellow") # lager tegner matbiten på canvas'et med x og y koordinatene vi bestemte rett over og gir den fargen gul
 
 
# tester programmet
_ = Pactroll() # siden Pactroll nå er en klasse må vi lage den først
for i in range(3):
    Matbit(_.canvas) # så lager vi 3 matbiter med en forløkke, må ha med hvor de skal lages, altså canvas'et til vinduet
_.vindu.mainloop() # kjører vinduet