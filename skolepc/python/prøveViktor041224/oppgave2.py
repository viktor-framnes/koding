import tkinter as tk
window = tk.Tk()
window.minsize(250,200)
byttfargeKnapp = tk.Button(window, text="Bytt farge",command=lambda: farge())
byttfargeKnapp.pack(side="bottom",pady=5)
farger = ["#779645","#B4403B","#EDB361","#FFE9D9"]
x = 0
def farge():
    global x
    if x == len(farger):
        x = 0
    window.configure(background=farger[x])
    x += 1
window.mainloop()