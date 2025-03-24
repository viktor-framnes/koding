tall1 = int(input("Skriv inn det første tallet: "))
tall2 = int(input("Skriv inn det andre tallet: "))

if tall1 > tall2:
    print(f"Det største tallet er tall1 altså {tall1} og det minste er tall2 altså {tall2}")
elif tall1 == tall2:
    print(f"Tall1 {tall1} og tall2 {tall2} er like store")
else: 
    print(f"Det største tallet er tall2 altså {tall2} og det minste er tall1 altså {tall1}")