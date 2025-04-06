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

x = bredde/2 #250
y = hoyde/2 #250

sirkel = canvas.create_oval(x+50,y+50,x-50,y-50,fill="yellow",outline="white",tags="sirkel",width=5)

blad1 = canvas.create_oval(x+250,y+65,x+53,y-65,fill="white",outline="black")
blad2 = canvas.create_oval(x-250,y+65,x-53,y-65,fill="white",outline="black")

blad3 = canvas.create_oval(x-65,5,x+65,y-53,fill="white",outline="black")
blad4 = canvas.create_oval(x-65,y+53,x+65,y*2,fill="white",outline="black")
    
window.mainloop()