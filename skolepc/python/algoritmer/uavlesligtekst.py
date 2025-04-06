from random import randint

tekst = "Det spiller ingen rolle i hvilke rekkefølge bokstavene står. Det eneste som telle r er at første og siste bokstav står på riktig sted. Du vil fortsatt kunne lese teksten uten problemer. Dette skyldes at menneskehjernen er kreativ."

x = tekst.split()
y = ""

for ord in x:
    if len(ord) > 3:
        a = ord[0]
        b = ord[-1]
        midten = list(ord[1:-1])

        for i in range(len(midten)):
            j = randint(0, len(midten) - 1)
            midten[i], midten[j] = midten[j], midten[i]

        resultat = ""
        for bokstav in midten:
            resultat += bokstav
        stokket_ord = a + resultat + b
    else:
        stokket_ord = ord

    y += stokket_ord + " "

print(y)

