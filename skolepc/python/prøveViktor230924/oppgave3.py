
kjor = True

while kjor == True:
    print("Skriv 0 for addisjon")
    print("Skriv 1 for subtraksjon")
    print("Skriv 2 for multiplikasjon")
    print("Skriv 3 for divisjon")
    metode = input("Velg regneart...")
    tall1 = int(input("Skriv første tall: "))
    tall2 = int(input("Skriv andre tall: "))
    if int(metode) == 0:
        print(f"{tall1} pluss {tall2} er lik {tall1 + tall2}")
    elif int(metode) == 1:
        print(f"{tall1} minus {tall2} er lik {tall1 - tall2}")
    elif int(metode) == 2:
        print(f"{tall1} gange {tall2} er lik {tall1 * tall2}")
    elif int(metode) == 3:
        print(f"{tall1} delt på {tall2} er lik {tall1 / tall2}")
    else:
        print("Du må skrive en av tallene!")
    slutt = input("Er du ferdig skriv q, vil du forsette trykk enter...")
    if slutt.lower() == "q":
        kjor = False
        break
        

