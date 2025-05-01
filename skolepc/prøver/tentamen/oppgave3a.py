import tkinter as tk

class passord(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(300,300)
        self.title("tk")
        self.tekst = tk.Label(self,text="Passordgenerator",font=1).pack(pady=3)
        self.tekst2 = tk.Label(self,text="Passordlengde:").pack(pady=3)
        self.entry = tk.Entry(self).pack(pady=3)
        self.b1 = tk.Button(self,text="Tall").pack(pady=3)
        self.b2 = tk.Button(self,text="Store Bokstaver").pack(pady=3)
        self.tekst3 = tk.Label(self,text="Valgt: Store bokstaver").pack(pady=3)
        self.b3 = tk.Button(self,text="Generer passord").pack(pady=3)
        self.tekst4 = tk.Label(self,text="Ditt passord:").pack(pady=3)
        self.svar = tk.Label(self,text="IJuegVSk", highlightbackground="lightgrey",highlightthickness=1,width=20,anchor="w").pack(pady=2)
_  = passord()
_.mainloop()