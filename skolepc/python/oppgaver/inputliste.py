liste = []
kjor = False

while kjor == False:
    tall = input("Skriv inn tallet: ")
    if tall == "x":
        kjor = True
        break
    liste.append(tall)

print(liste)