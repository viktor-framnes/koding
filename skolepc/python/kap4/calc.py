"""
Grafikk med tkinter.
calc
"""
import tkinter as tk
window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)    # Setter vinduets størrelse ved oppstart.
window.configure()

l1 = tk.Label(text="BASIC Kalkulator",)
l1.pack()

e1 = tk.Entry()
e1.pack()
e2 = tk.Entry()
e2.pack()


b1 = tk.Button(text="+")
b2 = tk.Button(text="-")
b3 = tk.Button(text="*")
b4 = tk.Button(text="/")
b5 = tk.Button(text="Avslutt")

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()

l2 = tk.Label(text="Svar")
l2.pack()

valg = ""

def pluss(e):
    tall1 = int(e1.get())
    tall2 = int(e2.get())
    l2["text"] = tall1 + tall2
def minus(e):
    tall1 = int(e1.get())
    tall2 = int(e2.get())
    l2["text"] = tall1 - tall2
def gange(e):
    tall1 = int(e1.get())
    tall2 = int(e2.get())
    l2["text"] = tall1 * tall2
def dele(e):
    tall1 = int(e1.get())
    tall2 = int(e2.get())
    l2["text"] = tall1 / tall2
def avslutt(e):
    window.destroy()


b1.bind("<Button-1>",pluss)
b2.bind("<Button-1>",minus)
b3.bind("<Button-1>",gange)
b4.bind("<Button-1>",dele)
b5.bind("<Button-1>",avslutt)


# Kjører GUI-tråden

window.mainloop()


