import tkinter as tk

#Lage et vindu
window = tk.Tk()
window.title("Dinospill")
window_width = 600
window_height = 400
window.minsize(window_width,window_height)


# Lager et tegnebrett til animering
canvas = tk.Canvas(window,width=window_width,height=window_height,bg="white")
canvas.pack()

#tegner bakken
bakke_hoyde = window_height-50
canvas.create_line(0,bakke_hoyde,window_width,bakke_hoyde,width=5)

# status på om spillet kjører
game_running = True

# lager dino class for animasjon av dinosauren(en kloss)
class Dino:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = 30
        self.y = bakke_hoyde
        self.hoyde = 40
        self.bredde = 40
        #lager dinoen
        self.dinoId = canvas.create_rectangle(self.x,
                                              self.y-self.hoyde,
                                              self.x+self.bredde,
                                              self.y-2,
                                              fill="blue")
        self.hopper = False
        self.dukker = False

    #Funksjon som definerer og animerer hopp
    def hopp(self):
        #hindre at figuren hopper og dukker samtidig
        if self.hopper or self.dukker:
            return
        self.hopper = True
        self.hopp_max = bakke_hoyde - 150
        self.start_y = self.y
        self.hoppefart = -10 # negativ fordi y-aksen er posistiv nedover 

        def animer_hopp():
            if self.hopper:
                # flytt Dino oppover (-) så lenge den er under maks høyde
                if self.hoppefart < 0 and self.y > self.hopp_max:
                    self.y += self.hoppefart
                elif self.hoppefart > 0 and self.y < self.start_y:
                    self.y += self.hoppefart
                else:
                    self.hoppefart = -self.hoppefart # Endrer retning på farten

                if self.y >= self.start_y:
                    self.y = self.start_y
                    self.hopper = False

                canvas.coords(self.dinoId, 
                            self.x,
                            self.y-self.hoyde,
                            self.x+self.bredde,
                            self.y-2)

                if self.hopper:
                    window.after(20,animer_hopp)

        animer_hopp()

    def dukk(self,start=True):
        if self.hopper:
            return
        if start:
            self.dukker = True
            self.hoyde = self.hoyde/2
            canvas.coords(self.dinoId,
                          self.x-5,
                          self.y,
                          self.x+self.bredde+5,
                          self.y-2-self.hoyde) # -self.høyde
        else:
            self.dukker = False
            self.hoyde = 40
            canvas.coords(self.x,
                        self.y-self.hoyde,
                        self.x+self.bredde,
                        self.y-2,)



dino = Dino(canvas)

#definerer hendelser for trykk på knapper
def on_up_key(e):
    if game_running:
        dino.hopp()
def on_down_key(e):
    if game_running:
        dino.dukk(start=True)
def on_down_key_release(e):
    if game_running:
        dino.dukk(start=False)


#binder taster til funksjon
window.bind("<Up>",on_up_key)
window.bind("<Down>",on_down_key)
window.bind("<KeyRelease-Down>",on_down_key_release)


window.mainloop()