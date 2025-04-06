tall = input("Skriv inn et tall ")
tall = int(tall)

if tall < 100:
    if tall > 50:
        print("Tallet er mellom 100 og 50")
    else:
        print("Tallet er mindre enn 50")
else:
    print("Tallet er større enn 100")
