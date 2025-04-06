tall1 = int(input("Skriv inn et tall: "))
tall2 = int(input("Skriv inn et tall: "))
tall3 = int(input("Skriv inn et tall: "))
tall4 = int(input("Skriv inn et tall: "))
tall5 = int(input("Skriv inn et tall: "))

storst = tall1

if tall2 > storst:
    storst = tall2

if tall3 > storst:
    storst = tall3
if tall4 > storst:
    storst = tall4
if tall5 > storst:
    storst = tall5

print("Det største tallet er ", storst)

if tall1 == tall2 and tall1 == tall3 and tall1 == tall4 and tall1 == tall5:
    print("Tallene er like")
else:
    print("Tallene er ikke like")

