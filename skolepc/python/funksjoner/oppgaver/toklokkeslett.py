
klokk1 = input("Skriv det første klokkeslettet med : i midten: ")
klokk2 = input("Skriv det andre klokkeslettet med : i midten: ")

def klokkeslett():

    a = klokk1.split(":")
    b = klokk2.split(":")

    print(a)
    print(b)
    
    
    time = int(b[0]) - int(a[0])
    sekund = int(b[1]) - int(a[1])

    print(f"{time} time og {sekund} sekunder")

klokkeslett()
