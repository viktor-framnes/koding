import tkinter as tk
import random
import time

tilstander = ["friskUtenImunitet","smittet","syk","friskMedImunitet","død"]

class Personspredning(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(200,200)
        self.bredde = 1000
        self.tilstand = tilstander[0]
        self.lb = tk.Label(self,text=tilstander[0])
        self.lb.pack(side="top")
        self.canvas = tk.Canvas(self,bg="lightgrey",width=self.bredde*0.08,height=self.bredde*0.08)
        self.canvas.pack(expand=True)
        tk.Button(self, text="Start", command=lambda: kjor()).pack(side="bottom")

    def tilstand0(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="lightgrey")
        self.lb.configure(text="friskUtenImunitet")
        self.canvas.update()

    def tilstand1(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="#ff9696")
        self.canvas.create_line(12,12,70,70,fill="black",width=5)
        self.lb.configure(text="smittet")
        self.canvas.update()

    def tilstand2(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="red")
        self.canvas.create_line(12,70,70,12,fill="white",width=5)
        self.lb.configure(text="syk")
        self.canvas.update()

    def tilstand3(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="#414141")
        self.canvas.create_oval(38,38,48,48,fill="black")
        self.lb.configure(text="friskMedImunitet")
        self.canvas.update()

    def tilstand4(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="black")
        self.canvas.create_oval(38,38,48,48,fill="white")
        self.lb.configure(text=f"Død")
        self.canvas.update()

    def smitte(self):
        if self.tilstand == "friskUtenImunitet":
            self.tilstand = tilstander[1]
            self.dagerSmittet = 0

    def oppdaterTilstand(self):
        if self.tilstand == "friskUtenImunitet":
            self.tilstand0()

        elif self.tilstand == "smittet":
            self.dagerSmittet += 1
            if self.dagerSmittet > 3:
                self.tilstand = tilstander[2]
                self.tilstand2()
            else:
                self.tilstand1()
                
        elif self.tilstand == "syk":
            self.tilstand2()
            self.dagerSmittet += 1
            if self.dagerSmittet <= 7:
                if random.randint(0,100) == 9:
                    self.tilstand = tilstander[4]
                    self.tilstand4()
            else:
                self.tilstand = tilstander[3]
                self.tilstand3()
                

    def __str__(self):
        return f"Personens tilstand er {self.tilstand}"

def kjor():
    print(b)
    b.smitte()
    for i in range(8):
        b.oppdaterTilstand()
        print(f"dag {i+1}")
        print(b)
        time.sleep(1)

b = Personspredning()
b.mainloop()



    


