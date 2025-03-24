tabell = [
    ["A", "B", "C"], 
    ["D", "E", "F"], 
    ["G", "H", "I"]
    ]

for i in range(len(tabell)):
    for j in range(len(tabell[i])):
        if tabell[i][j] == "E":
            print(f"Bokstaven E har indeks {tabell[i].index('E')}")

for i in range(len(tabell)):
    for j in range(len(tabell[i])):
        tabell[i][j] = tabell[1][2]
print(tabell)