tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]

sum = 0

for i in range(len(tall)):
    sum += i

print(f"summen av tallene er {sum} og gjennomsnittet er {sum/len(tall)}")