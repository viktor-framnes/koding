import tkinter as tk

window = tk.Tk()
window.title("Button med lambda")
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)

knapp = tk.Button(window, text="OK", command= lambda: handleKnapp(5))
knapp.pack(expand=True)

def handleKnapp(tall):
    print(tall) # informasjon kan sendes fra lambda-uttrykket til funksjonen
    knapp["text"] = "Trykket"

window.mainloop()