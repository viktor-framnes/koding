m = 10 
n = 10
brett = []
y = 111



for i  in range(m):
    brett.append([])
    y -= 15
    for j in range(n):
        if i % 2 != 0:
            brett[i].append(y)
            y = y + 1
           
     

for rad in brett:
    print(rad)