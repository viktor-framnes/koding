import tkinter as tk

window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde) # Setter vinduets størrelse ved oppstart.

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
mid.pack(fill="both", expand=True)  # Fyller både horisontalt og vertikalt

# Legger et vindu inni et annet
innervindu = tk.Frame(mid)
innervindu.configure(
    background="MediumvioletRed",
    height=300,
    width=bredde * 0.8
)
innervindu.pack_propagate(False)  # Skrur av at children kan endre rammen
innervindu.pack(expand=True)  # Sørger for at innervinduet fyller tilgjengelig plass

footer = tk.Frame(window)
footer.configure(
    background="lightcoral",
    height=50,
    width=bredde
)
footer.pack()

# Legger til tekst med Label-klassen og midtstiller den i innervinduet
hohoho = tk.Label(innervindu) 
hohoho.configure(
    text="ho ho ho!",
    font=("Comic sans", 30),
    foreground="white",
    background="MediumvioletRed"
)
hohoho.pack(expand=True)  # Sørger for å midtstille vertikalt og horisontalt

# Legger til overskriften og midtstiller den i headeren
overskrift = tk.Label(header)
overskrift.configure(
    text="Velkommen til tkinter",
    font=("Comic sans", 30),
    foreground="white",
    background="palevioletred"
)
overskrift.pack(expand=True)  # Midtstiller i header
header.pack_propagate(False)

# Kjører GUI-tråden
window.mainloop()