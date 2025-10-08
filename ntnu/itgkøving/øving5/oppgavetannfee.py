teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114, 109, 11, 2, 21, 45, 2, 26, 81, 54, 14, 118, 108, 117, 27, 115, 43, 70, 58, 107]
x = [[] for i in range(len(teeth))]


for i, tenner in enumerate(teeth):
    tjuere = tenner//20
    x[i].append(tjuere)
    tenner = tenner-tjuere*20
    tiere = tenner//10
    x[i].append(tiere)
    tenner = tenner-tiere*10
    femere = tenner//5
    x[i].append(femere)
    tenner = tenner-femere*5
    enere = tenner//1
    x[i].append(enere)
    tenner = tenner-enere*1

for rad in x:
    print(f"20: {rad[0]} , 10: {rad[1]} , 5: {rad[2]} , 1: {rad[3]}")
