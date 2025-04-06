brett = []
m = 8
n = 8
for i in range(m):
    brett.append([])
    for j in range(n):
            if i % 2 == 0:
                if j % 2 == 0:
                    brett[i].append("◼️")
                else:
                    brett[i].append("◽️")
            else:
                if j % 2 == 0:
                    brett[i].append("◽️")
                else:
                    brett[i].append("◼️")
        


for rad in brett:
    print(rad)