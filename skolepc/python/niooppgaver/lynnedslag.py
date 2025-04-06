N, K = map(int, input().split())
allehus = [i for i in range(N)]
teller = 0

for i in range(K):
    a, b = map(int, input().split())
    paavirkethus = [i for i in range(a,b + 1)]
    
    if teller > 0:
        paavirkethus = [i for i in range(a,b+1)]
        for x in paavirkethus:
            if x in allehus:
                allehus.remove(x)
                paavirkethus.remove(x)
        for x in paavirkethus:
            if x not in allehus:
                allehus.append(x)
    else:
        for x in paavirkethus:
            if x in allehus:
                allehus.remove(x)
        paavirkethus = []

    teller += 1

print(len(allehus))
