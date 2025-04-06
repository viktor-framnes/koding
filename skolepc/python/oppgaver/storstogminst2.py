liste = ["a","aa","aaa","bec","aaaaaaa"]

minst = liste[0]
storst = liste[0]

for i in range(len(liste)):
    if len(liste[i]) > len(storst):
        storst = liste[i]
    elif len(liste[i]) < len(minst):
        minst = liste[i]

print(f"Det lengste ordet er {storst} og det minste er {minst}")