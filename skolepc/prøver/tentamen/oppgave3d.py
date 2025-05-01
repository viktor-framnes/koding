import tkinter as tk
import random

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

class passord(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(300,300)
        self.tegn = False
        self.tall = False
        self.tekst = tk.Label(self,text="Passordgenerator",font=1).pack(pady=2)
        self.tekst2 = tk.Label(self,text="Passordlengde:").pack(pady=2)
        self.entry = tk.Entry(self)
        self.entry.pack(pady=2)
        tk.Button(self,text="Store Bokstaver",command=self.bokstavvalg).pack(pady=2)
        tk.Button(self,text="Tall",command=self.tallvalg).pack(pady=2)
        self.tekst3 = tk.Label(self,text="Valgt: ")
        self.tekst3.pack(pady=2)
        tk.Button(self,text="Generer passord",command= self.svar).pack(pady=2)
        self.tekst4 = tk.Label(self,text="Ditt passord:").pack(pady=2)
        self.svar = tk.Label(self,text="",highlightbackground="lightgrey",highlightthickness=1,width=20,anchor="w")
        self.svar.pack(pady=2)

    def bokstavvalg(self):
        if self.tegn == False:
            self.tegn = True
        else:
            self.tegn = False
        self.tekst3svar()
        
    def tallvalg(self):
        if self.tall == False:
            self.tall = True
        else:
            self.tall = False
        self.tekst3svar()


    def tekst3svar(self):
        if self.tegn == True and self.tall == True:
            self.tekst3.config(text="Valgt: tall, store bokstaver")
        elif self.tegn == True and self.tall == False:
            self.tekst3.config(text="Valgt: store bokstaver")
        elif self.tegn == False and self.tall == True:
            self.tekst3.config(text="Valgt: tall")
        else:
            self.tekst3.config(text="Valgt: ")



    def svar(self):
        try:
            x = self.entry.get()
            x = int(x)
            if x < 0:
                print("Skriv et positivt heltall")
                return None
            else:
                passord = ""
                if self.tegn == False and self.tall == False:
                    for i in range(x):
                        passord += alfabet[random.randint(26,len(alfabet)-11)]
                elif self.tegn == False and self.tall == True:
                    for i in range(x):
                        passord += alfabet[random.randint(26,len(alfabet)-1)]
                elif self.tegn == True and self.tall == False:
                    for i in range(x):
                        passord += alfabet[random.randint(0,len(alfabet)-11)]
                else:
                    for i in range(x):
                        passord += alfabet[random.randint(0,len(alfabet)-1)] 
                self.svar.config(text=passord)
            
        except ValueError:
            print("du må skrive et heltall")

_  = passord()
_.mainloop()