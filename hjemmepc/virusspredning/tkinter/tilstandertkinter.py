import tkinter as tk

window = tk.Tk()
window.geometry("1800x400")


tilstand1 = tk.Frame(window)
tilstand1.configure(
)
tilstand1.pack(expand=True,side="left")

canvas5 = tk.Canvas(tilstand1,bg="lightgrey",width=300,height=300)
canvas5.pack()



tilstand2 = tk.Frame(window)
tilstand2.configure(
)
tilstand2.pack(expand=True,side="left")

canvas2 = tk.Canvas(tilstand2,bg="#ff9696",width=300,height=300)
canvas2.pack()

canvas2.create_line(25,25,275,275,fill="black",width=10)



tilstand3 = tk.Frame(window)
tilstand3.configure(
)
tilstand3.pack(expand=True, side="left")

canvas = tk.Canvas(tilstand3,bg="red",width=300,height=300)
canvas.pack()

canvas.create_line(25,275,275,25,fill="white",width=10)



tilstand4 = tk.Frame(window)
tilstand4.configure(
)
tilstand4.pack(expand=True,side="left")

canvas3 = tk.Canvas(tilstand4,bg="#414141",width=300,height=300)
canvas3.pack()

canvas3.create_oval(140,140,160,160,fill="black")


tilstand5 = tk.Frame(window)
tilstand5.configure(
)
tilstand5.pack(expand=True,side="left")

canvas4 = tk.Canvas(tilstand5,bg="black",width=300,height=300)
canvas4.pack()

canvas4.create_oval(140,140,160,160,fill="white")



window.mainloop()
