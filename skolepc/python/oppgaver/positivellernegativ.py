tall = input("skriv inn et tall ")
tall = int(tall)

if tall > 0:
    if tall > 100:
        print("Tallet er større enn hundre")
    else:
        print("Tallet er hundre eller mindre, men positivt")
elif tall < 0:
    if tall < -100:
        print("Tallet er mindre enn minus hundre")
    else:
        print("Tallet er minus hundre eller større, men negativt")
elif tall == 0:
    print("Tallet er null")