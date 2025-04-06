import tkinter as tk

window = tk.Tk()
window.geometry("1200x600")
canvasHoyde = 500
canvasBredde = 1200

canvas = tk.Canvas(window,bg="lightblue",height=canvasHoyde,width=canvasBredde)
canvas.pack()
canvas.create_rectangle(30,canvasHoyde-100,130,canvasHoyde,fill="yellow")

bakke = tk.Frame(window)
bakke.configure(
    bg="lightgreen",
    height=100,
    width=1200
)
bakke.pack()

window.mainloop()