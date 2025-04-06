import tkinter as tk

window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
window.title("Canvas-tegning")
window.configure(background="black")

# 1) Legger canvas direkte i vinduet
canvas = tk.Canvas()
canvas.configure(
        background="#235E6F",
        width=bredde,
        height=hoyde,
)
canvas.pack(expand=True)
sirkel = canvas.create_oval(50,100,100,150,fill="white",outline="black",tags="sirkel",width=5)

rektBredde = 100
rektHoyde = 50
x = 200
y = 200

rektangel = canvas.create_rectangle(
    x-rektBredde/2,y-rektHoyde/2,
    x+rektBredde/2,y+rektHoyde/2,
    fill="black",
    outline="white",
    width=5,
    tags="rektangel"
    )

window.mainloop()