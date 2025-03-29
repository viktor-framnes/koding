

brett = []
for i in range(11):
    brett.append([{0:0}]*11)

for rad in brett:
    print(rad)

print()
brett[5][5][0] = 1

for rad in brett:
    print(rad)