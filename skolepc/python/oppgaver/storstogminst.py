liste = [1,4,5,1,2,4,5,10]

minst = liste[0]
storst = liste[0]

for i in range(len(liste)):
    if liste[i] > storst:
        storst = liste[i]
    elif liste[i] < minst:
        minst = liste[i]

print(f"Det største tallet er {storst} og det minste er {minst}")