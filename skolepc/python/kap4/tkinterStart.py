"""
Grafikk med tkinter
Frames er i fokus
"""
import tkinter as tk

window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde) # Setter vinduets størrelse ved oppstart.
window.configure(background="lightpink")

# 1) Lager første vindu en "Frame"
header = tk.Frame(window)
header.configure(
    background="palevioletred",
    height=100,
    width=bredde
)
header.pack()

mid = tk.Frame(window)
mid.configure(
    background="lightpink",
    height=350,
    width=bredde
)
mid.pack()

footer = tk.Frame(window)
footer.configure(
    background="lightcoral",
    height=50,
    width=bredde
)
footer.pack()

# Kjører GUI-tråden
window.mainloop()
