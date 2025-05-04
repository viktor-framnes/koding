strs=["",""]

par = []
indeks = []
if len(strs) == 1:
    par.append(strs)
else:
    for i in range(len(strs)-1):
        if i == len(strs)-2 and strs[-1] not in par and len(strs) > 2:
            par.append([strs[-1]])

        if i in indeks:
            continue
        templist = []
        for j in range(i+1,len(strs)-len(par)):
            if j in indeks:
                continue
            if strs[i] not in templist:
                templist.append(strs[i])
            if sorted(strs[i]) == sorted(strs[j]):
                templist.append(strs[j])     
                indeks.append(i)
                indeks.append(j)

        if templist != []:
            par.append(templist) 
print(par)
