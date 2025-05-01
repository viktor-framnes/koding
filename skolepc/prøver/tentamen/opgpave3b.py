import tkinter as tk

class passord(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(300,300)
        self.tekst = tk.Label(self,text="Passordgenerator",font=1).pack(pady=2)
        self.tekst2 = tk.Label(self,text="Passordlengde:").pack(pady=2)
        self.entry = tk.Entry(self)
        self.entry.pack(pady=2)
        self.b1 = tk.Button(self,text="Tall").pack(pady=2)
        self.b2 = tk.Button(self,text="Store Bokstaver").pack(pady=2)
        self.tekst3 = tk.Label(self,text="Valgt: Store bokstaver").pack(pady=2)
        self.b3 = tk.Button(self,text="Generer passord",command= self.svar).pack(pady=2)
        self.tekst4 = tk.Label(self,text="Ditt passord:").pack(pady=2)
        self.svar = tk.Label(self,text="",highlightbackground="lightgrey",highlightthickness=1,width=20,anchor="w")
        self.svar.pack(pady=2)

    def svar(self):
        try:
            x = self.entry.get()
            x = int(x)
            if x < 0:
                print("Skriv et positivt heltall")
                return None
            else:
                self.svar.config(text=x)
        except ValueError:
            print("du må skrive et heltall")

_  = passord()
_.mainloop()