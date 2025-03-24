import random 
import tkinter as tk

tilstander = {
    0:"friskUtenImunitet", # lys grå
    1:"smittet", # rosa med svart skråstrek
    2:"syk", # rød med hvit skråstrek
    3:"friskMedImunitet", # mørk grå med svart prikk
    4:"død" # svart med hvit prikk
}

class Person():
    def __init__(self):
        self.tilstand = tilstander[0]
        self.window = tk.Tk()
        self.window.geometry("755x110")
        self.lengde = 100
        self.bredde = 1000
        self.tilstand0()

    def tilstand0(self):
        canvas = tk.Canvas(self.window,bg="lightgrey",width=self.bredde*0.08,height=self.bredde*0.08)
        canvas.pack(side="left",expand=True)

    def tilstand1(self):
        canvas = tk.Canvas(self.window,bg="#ff9696",width=self.bredde*0.08,height=self.bredde*0.08)
        canvas.pack(side="left",expand=True)

        canvas.create_line(12,12,70,70,fill="black",width=5)

    def tilstand2(self):
        canvas = tk.Canvas(self.window,bg="red",width=self.bredde*0.08,height=self.bredde*0.08)
        canvas.pack(side="left",expand=True)

        canvas.create_line(12,70,70,12,fill="white",width=5)

    def tilstand3(self):
        canvas = tk.Canvas(self.window,bg="#414141",width=self.bredde*0.08,height=self.bredde*0.08)
        canvas.pack(side="left",expand=True)

        canvas.create_oval(38,38,48,48,fill="black")

    def tilstand4(self):
        canvas = tk.Canvas(self.window,bg="black",width=self.bredde*0.08,height=self.bredde*0.08)
        canvas.pack(side="left",expand=True)

        canvas.create_oval(38,38,48,48,fill="white")

    def vis(self):
        self.window.mainloop()

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

def main():
    person1 = Person()

    print(person1)
    person1.smitte()
    for i in range(8):
        person1.oppdaterTilstand()
        print(f"dag {i+1}")
        print(person1)
    person1.vis()

if __name__ == "__main__":
    main()