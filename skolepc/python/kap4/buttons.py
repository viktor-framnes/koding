"""
Grafikk med tkinter.
knapper er i fokus
"""
import tkinter as tk
window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)    # Setter vinduets størrelse ved oppstart.
window.configure(background="#00873E")

# 1) Lager første vindu en "Frame"
header = tk.Frame(window)
header.configure(
    background="#00873E",
    height=100,
    width=bredde,
)
header.pack()

hovedvindu = tk.Frame(window)
hovedvindu.configure(
    background="#00873E",
    height=350,
    width=bredde,
)
hovedvindu.pack()

# Legger et vindu inni et annet
innervindu = tk.Frame(hovedvindu)
innervindu.configure(
    background="red",
    height=100,
    width=bredde*0.8,
    highlightbackground="white",
    highlightthickness=5, # border-width
)
hovedvindu.pack_propagate(False) # Skrur av at children kan endre rammen.


innervindu.pack_propagate(False)
innervindu.pack()

# Lager en usynlig boks som presser teksten lenger ned
usynlig_boks = tk.Frame(innervindu)
usynlig_boks.configure(
    height=10,
    background="red"
)
usynlig_boks.pack()

# Legger til litt tekst med Label-klassen.
hohoho = tk.Label(innervindu)
hohoho.configure(
    text="ho ho ho!",
    font = ("Comic sans", 50),
    foreground="white",
    background="red"
)

hohoho.pack()

footer = tk.Frame(window)
footer.configure(
    background="white",
    height=50,
    width=bredde,
)
footer.pack_propagate(False)
footer.pack()

#---------------- Slutt på GUI definisjonene ----------------------
# A) Lager knapper

avsluttKnapp = tk.Button(footer, text="avslutt")
avsluttKnapp.pack(expand=True)

knappOK = tk.Button(hovedvindu, text="OK")
knappOK.pack(expand=True)

# B) Lager funksjonene til knappene

def avslutt(e):
    """ Avslutter vinduet og programmet. """
    window.destroy()

teller = 0
def handle_knappOK(e):
    """ Bytter tekst på OK-knappen til tellende tall."""
    global teller
    teller += 1
    # knappOK.configure(text=teller)
    knappOK["text"] = f"{teller}"
# C) Binder knapper til funksjoner

avsluttKnapp.bind("<Button-1>",avslutt)
knappOK.bind("<Button-1>",handle_knappOK)

# Kjører GUI-tråden

window.mainloop()


