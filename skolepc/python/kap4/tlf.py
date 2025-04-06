import tkinter as tk
import datetime as dt


window = tk.Tk()

window.minsize(250,200)

l1 = tk.Label(window,text="Telefonkatalog")
l2 = tk.Label(window,text="Navn")
l3 = tk.Label(window,text="Telefonnummer")
l4 = tk.Label(window)
e1 = tk.Entry(window)
e2 = tk.Entry(window)
b1 = tk.Button(window,text="Legg til")
b2 = tk.Button(window,text="Skriv ut")

l1.pack()
l2.pack()
e1.pack()
l3.pack()
e2.pack()
b1.pack()
b2.pack()
l4.pack()

x = ""
def leggtil(e):
    global x
    x += e1.get() + " " + e2.get() + "\n"

def skrivut(e):
    l4["text"] = x


b1.bind("<Button-1>", leggtil)
b2.bind("<Button-1>", skrivut)

window.mainloop()