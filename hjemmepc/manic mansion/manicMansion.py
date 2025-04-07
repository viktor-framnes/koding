import tkinter as tk

bredde = 1200
hoyde = 700
r = 20

class Manic(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(bredde,hoyde)
        self.maxsize(bredde,hoyde)
        self.venstreCanvas = tk.Canvas(self,bg="blue",width=200,height=hoyde,highlightthickness=0)
        self.venstreCanvas.pack(side="left")
        self.midtCanvas = tk.Canvas(self,bg="black",width=bredde-400,height=hoyde,highlightthickness=0)
        self.midtCanvas.pack(side="left")
        self.hoyreCanvas = tk.Canvas(self,bg="red",width=200,height=hoyde,highlightthickness=0)
        self.hoyreCanvas.pack(side="left")

        self.objekter = []
        self.spiller = Spillobject(self.venstreCanvas)
        self.kjorer = True

        self.bind("<KeyPress-Left>", lambda _: self.spiller.flytt(-self.spiller.ds, 0))
        self.bind("<KeyPress-Right>", lambda _: self.spiller.flytt(self.spiller.ds, 0))
        self.bind("<KeyPress-Up>", lambda _: self.spiller.flytt(0, -self.spiller.ds))
        self.bind("<KeyPress-Down>", lambda _: self.spiller.flytt(0, self.spiller.ds))

    def game_loop(self):
        if self.kjorer:
            self.spiller.x += self.spiller.dx
            self.spiller.y += self.spiller.dy


class Spillobject:
    def __init__(self,canvas):
        self.brett = canvas
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.ds = 3
        self.spiller_id = self.brett.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="yellow")


    def plassering(self,x,y):
        pass

    def flytt(self,x,y):
        self.dx = x
        self.dy = y

class Menneske(Spillobject):
    def __init__(self):
        super().__init__()
        self.fart = 0
        self.poeng = 0
        self.taSau = False

    def beveg(self,avstand,retning):
        pass

    def reduserfart(self,nyfart):
        pass

    def økpoeng(self,n):
        pass

    def bærsau(self,sau):
        pass

    def sjekkKollisjon(self):
        pass

class Spøkelse(Spillobject):
    def endreRetning(self):
        pass

class Hindring(Spillobject):
    pass

class Sau(Spillobject):
    def __init__(self):
        super().__init__()
        self.blirBåret = False

    def blirLøftet(self):
        pass

    def fjernSau(self):
        pass

x = Manic()
x.mainloop()