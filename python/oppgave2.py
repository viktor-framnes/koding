tekst = "aaaassddaassffadaa"
sum = 0

for i in range(len(tekst)):
    if tekst[i] == "s":
        sum += 1

print(f"Det er {sum} forekomster av bokstaven s")