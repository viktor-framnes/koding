import tkinter as tk


class Populasjontkinter():
    def __init__(self):    
        self.window = tk.Tk()
        self.window.geometry("1010x1000")
        self.bredde = 1000
        self.hoyde = 1000

        self.frame = tk.Frame(self.window)
        self.frame.configure(
            background="blue",
            height= self.hoyde,
            width= self.bredde
        )
        self.frame.pack(expand=True)

        for i in range(11):
            for j in range(11):
                self.lagblokk(i,j)

        #start posisjon
        #midten
        self.sykBlokk()
        self.blokk.grid(row=5,column=5)
        #N
        self.smittetBlokk()
        self.blokk.grid(row=4,column=5)
        #S
        self.smittetBlokk()
        self.blokk.grid(row=6,column=5)
        #V
        self.smittetBlokk()
        self.blokk.grid(row=5,column=4)
        #Ø
        self.smittetBlokk()
        self.blokk.grid(row=5,column=6)
        

    def lagblokk(self,i,j):
        self.blokk = tk.Canvas(self.frame,bg="grey",width=self.bredde*0.08,height=self.hoyde*0.08)
        self.blokk.grid(row=i,column=j)

    def oppdaterblokk(self,i,j):
        self.blokk.grid(row=i,column=j)

    #forskjellige typer tilstander
    def smittetBlokk(self):
        self.blokk = tk.Canvas(self.frame,bg="#ff9696",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_line(12,12,70,70,fill="black",width=5)

    def sykBlokk(self):
        self.blokk = tk.Canvas(self.frame,bg="red",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_line(12,70,70,12,fill="white",width=5)

    def friskMedInumitetBlokk(self):
        self.blokk = tk.Canvas(self.frame,bg="#414141",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_oval(38,38,48,48,fill="black")

    def dodBlokk(self):
        self.blokk = tk.Canvas(self.frame,bg="black",width=self.bredde*0.08,height=self.bredde*0.08)
        self.blokk.create_oval(38,38,48,48,fill="white")

    #viser brettet
    def vis(self):
        self.window.mainloop()



def main():
    popt1 = Populasjontkinter()
    popt1.vis()


if __name__ == "__main__":
    main()

