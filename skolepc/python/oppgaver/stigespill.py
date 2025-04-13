from random import randint

#spillvariabler
m = 10 
n = 10
brett = []
x = 105
y = 111
antallkast = 0

#spiller kordinasjon
spillerikon = "X" 
spiller = 0
buffer = 0

#stiger og slanger
stiger = [
    [1,4,9,21,28,36,51,71,80],
    [38,14,31,42,84,44,67,91,100]

]
slanger = [
    [16,48,49,56,62,64,87,93,95,98],
    [6,26,11,53,19,60,24,73,75,78]
]

#spillfunksjoner
def terning():
    return randint(1,6)

def flyttspiller():
    global spiller
    spiller += terningkast
    if spiller > 100:
        spiller -= terningkast

#legge inn verdier i brettet
for i  in range(m):
    brett.append([])
    x -= 5
    y -= 15
    for j in range(n):
        if i % 2 == 0:
            brett[i].append(x)
            x = x - 1
        else:
            brett[i].append(y)
            y = y + 1

#leter etter slanger og stiger
for i in range(m):
    for j in range(n):
        if brett[i][j] in stiger[0]:
            brett[i][j] = "   s"
        elif brett[i][j] in slanger[0]:
            brett[i][j] = "   o"


#spille spillet
spilligang = True

while spilligang == True:

    #skifterr tilbake fra x
    for i in range(m):
        for j in range(n):
            if brett[i][j] == "   X":
                brett[i][j] = buffer
    #plassere spiller 
    for i in range(m):
        for j in range(n):
            if brett[i][j] == spiller:
                buffer = brett[i][j]
                brett[i][j] = f"   {spillerikon}"

    #printer brettet
    for rad in brett:
        for i in range(0,len(rad)-1):
            print(f"{rad[i]:4}",end="")
        print(f"{rad[-1]:4}")

    print("\n")
    
    #sjekke om spillet er ferdig
    if spiller == 100:
        spilligang = False
        print("Du vant")
        print(f"Du brukte {antallkast} kast")
        break


    kast = input("Kast terningen...")

    antallkast += 1
        
    if kast.upper() == "Q":
        quit()
    else:
        terningkast = terning()
        flyttspiller()
        for i in range(len(stiger)):
            for j in range(len(stiger[1])):
                if spiller in stiger[0]:
                    print(f"Stige! Du går fra plass {spiller} til {stiger[1][stiger[0].index(spiller)]}")
                    spiller = stiger[1][stiger[0].index(spiller)]
        for i in range(len(slanger)):
            for j in range(len(slanger[1])):
                if spiller in slanger[0]:
                    print(f"Slange! Du går fra plass {spiller} til {slanger[1][slanger[0].index(spiller)]}")
                    spiller = slanger[1][slanger[0].index(spiller)]

    print(f"Du kastet {terningkast},spilleren din er nå på plass: {spiller}")