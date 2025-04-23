import tkinter as tk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(200,200)
        self.tekst = tk.Label(self,text="Kodelås",font=100).pack()
        self.frame1 = tk.Frame(self)
        self.frame1.pack(pady=10)
        tk.Button(self.frame1, text="*", command=self.stjerne).grid(row=1, column=1,padx=2)
        tk.Button(self.frame1, text="1", command=lambda: self.trykk("1")).grid(row=1, column=2,padx=2)
        tk.Button(self.frame1, text="2", command=lambda: self.trykk("2")).grid(row=1, column=3,padx=2)
        tk.Button(self.frame1, text="3", command=lambda: self.trykk("3")).grid(row=1, column=4,padx=2)
        tk.Button(self.frame1, text="4", command=lambda: self.trykk("4")).grid(row=1, column=5,padx=2)
        tk.Button(self.frame1, text="5", command=lambda: self.trykk("5")).grid(row=1, column=6,padx=2)
        self.tekst = tk.Label(self)
        self.tekst.pack()
        self.avslutt = tk.Button(self, text="Avslutt", command=lambda: self.destroy()).pack(side="bottom",pady=20)
        self.kjor = False
        self.kode = ["1","2","3","4"]
        self.forsok = []

    def trykk(self,a):
        if self.kjor:
            if len(self.forsok) < 4:
                self.forsok.append(a)
                print(self.forsok)

    def stjerne(self):
        if self.kjor == True:
            if self.kode == self.forsok:
                self.tekst.config(text="Åpnet")
                print(self.forsok)
            elif len(self.forsok) == 4:
                self.tekst.config(text="Feil")
                self.kjor = False
                print(self.forsok)
        else:
            self.kjor = True
            self.forsok = []
            self.tekst.config(text="")

_  = Gui()
_.mainloop()