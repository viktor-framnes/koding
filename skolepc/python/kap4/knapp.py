import tkinter as tk
import datetime as dt


window = tk.Tk()

window.minsize(250,200)

okKnapp = tk.Button(window,text="OK")
okKnapp.pack(expand=True)

y = ""
x = 0
def trykket(e):
    global x
    global y
    if y == "y":
        z = dt.datetime.now()
        v = z-x
        if v < dt.timedelta(seconds=0.5):
            window.quit()
    else:
        x = dt.datetime.now()
        okKnapp["text"] = "trykket"
        window.configure(background="#abcdef")
        y = "y"




okKnapp.bind("<Button-1>",trykket)

window.mainloop()