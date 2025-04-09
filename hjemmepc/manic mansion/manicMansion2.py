import tkinter as tk

bredde = 1000
hoyde = 500
r = 15

class Manic(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.kjorer = True
        self.x = bredde/2
        self.y = hoyde/2
        self.dx = 0
        self.dy = 0
        self.ds = 2
        self.matpos = []
        self.blokker = []
        
        self.resizable(False, False)
        self.canvas = tk.Canvas(self,bg="black",width=bredde,height=hoyde)
        self.minsize(bredde,hoyde)
        self.canvas.pack(expand=True)
        self.spiller = self.canvas.create_rectangle(self.x-r,self.y-r,self.x+r,self.y+r,fill="green")


        self.bind("<KeyPress-Left>", lambda _: self.byttRettning(-self.ds, 0))
        self.bind("<KeyPress-Right>", lambda _: self.byttRettning(self.ds, 0))
        self.bind("<KeyPress-Up>", lambda _: self.byttRettning(0, -self.ds))
        self.bind("<KeyPress-Down>", lambda _: self.byttRettning(0, self.ds))
        self.bind("<KeyRelease-Left>", lambda _: self.stopp())
        self.bind("<KeyRelease-Right>", lambda _: self.stopp())
        self.bind("<KeyRelease-Up>", lambda _: self.stopp())
        self.bind("<KeyRelease-Down>", lambda _: self.stopp())

        self.game_loop()

    def sjekkKolisjon(self):
        # sjekker kolisjon med veggene
        if self.x+r >= bredde:
            self.byttRettning(-self.ds, 0)  # Snu til venstre
        if self.y+r >= hoyde:
            self.byttRettning(0, -self.ds)  # Snu oppover
        if self.x-r <= 0:
            self.byttRettning(self.ds, 0)  # Snu til høyre
        if self.y-r <= 0:
            self.byttRettning(0, self.ds)  # Snu nedover

    def byttRettning(self, dx, dy):
        self.ds = 2
        self.dx = dx
        self.dy = dy
        
    def stopp(self):
        self.dx = 0
        self.dy = 0
    

    def game_loop(self):
        if self.kjorer:
            self.sjekkKolisjon()
            self.x += self.dx
            self.y += self.dy
            self.canvas.move(self.spiller, self.dx, self.dy)
            self.after(10,self.game_loop)
        
    def game_over(self):
        self.kjorer = False
        self.canvas.create_text(bredde/2,hoyde/2,text="Game over",fill="red",font=20)


_ = Manic()
_.mainloop()


