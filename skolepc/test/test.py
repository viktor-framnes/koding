def finn_medianen(liste):
    sortert = sorted(liste)
    lengde = len(sortert)

    if lengde % 2 == 0:
        m1 = lengde //2
        m2 = lengde //2+1
        median = (sortert[m1] + sortert[m2]) /2
    else:
        midt = lengde //2
        median = sortert[midt]

    return median

a = [1,2,3,4,9,10,9,1]
print(finn_medianen(a)) 