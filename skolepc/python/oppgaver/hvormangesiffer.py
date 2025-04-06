tall = input("Skriv inn et tall ")
tall = int(tall)

if tall > 9999:
    print("Tallet har mer enn fire siffer")
elif tall > 999:
    print("Tallet har mer enn tre siffer")
elif tall > 99:
    print("Tallet har mer enn to siffer")
elif tall > 9:
    print("Tallet har mer enn et siffer")
elif tall > 0:
    print("Tallet har bare ett siffer")
else:
    print("Tallet er negativt eller ugyldig")