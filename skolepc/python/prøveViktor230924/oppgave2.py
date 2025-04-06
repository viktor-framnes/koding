alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-","1","2","3","4","5","6","7","8","9","0"]

tekst = input("Skriv inn din tekst: ")

print(f"Det er {len(tekst)} tegn i teksten")

ord = 1
if tekst[0] == " ":
    ord -= 1

for i in range(len(tekst)):
    if tekst[i] == " ":
        try:
            if tekst[i+1].lower() in alf:
                ord += 1
        except IndexError:
            break
if ord >= 10:
    print("Beklager, dette var en for lang tekst")
else:
    print(f"Det er {ord} ord i teksten")
