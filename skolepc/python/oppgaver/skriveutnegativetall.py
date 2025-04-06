tall = [1, 3, -2, 2, 5, -1, -7, 8, 5, 6, -4, 5]
negativetall = []
sum = 0

for i in range(len(tall)):
    if tall[i] < 0:
        sum = sum + 1
        negativetall.append(tall[i])

print(sum)
print(negativetall)