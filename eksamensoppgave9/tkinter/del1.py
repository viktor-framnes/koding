import tkinter as tk


window = tk.Tk()
window.geometry("400x400")


boks = tk.Frame(window)
boks.configure(
)
boks.pack(expand=True)

canvas = tk.Canvas(boks,bg="red",width=300,height=300)
canvas.pack()

canvas.create_line(25,275,275,25,fill="white",width=10)

window.mainloop()

#-----------------------------------------------------------

window2 = tk.Tk()
window2.geometry("400x400")


boks2 = tk.Frame(window2)
boks2.configure(
)
boks2.pack(expand=True)

canvas2 = tk.Canvas(boks2,bg="#ff9696",width=300,height=300)
canvas2.pack()

canvas2.create_line(25,25,275,275,fill="black",width=10)

window2.mainloop()

#-----------------------------------------------------------

window3 = tk.Tk()
window3.geometry("400x400")


boks3 = tk.Frame(window3)
boks3.configure(
)
boks3.pack(expand=True)

canvas3 = tk.Canvas(boks3,bg="#414141",width=300,height=300)
canvas3.pack()

canvas3.create_oval(140,140,160,160,fill="black")

window3.mainloop()

#-----------------------------------------------------------

window4 = tk.Tk()
window4.geometry("400x400")


boks4 = tk.Frame(window4)
boks4.configure(
)
boks4.pack(expand=True)

canvas4 = tk.Canvas(boks4,bg="black",width=300,height=300)
canvas4.pack()

canvas4.create_oval(140,140,160,160,fill="white")

window4.mainloop()

#-----------------------------------------------------------

window5 = tk.Tk()
window5.geometry("400x400")


boks5 = tk.Frame(window5)
boks5.configure(
)
boks5.pack(expand=True)

canvas5 = tk.Canvas(boks5,bg="lightgrey",width=300,height=300)
canvas5.pack()

window5.mainloop()