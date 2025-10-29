tall = [3, 4, 1, 2, 5]


for i in range(len(tall)):
    for j in range(i,len(tall)):
        if tall[j] < tall[i]:
            tall[i], tall[j] = tall[j], tall[i]
print(tall)