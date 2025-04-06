N = int(input())
h = [0] * N # lager en liste fylt med 0 av lengde N
b = [0] * N
hoyde = 0

for i in range(N):
    h[i], b[i] = map(int, input().split())

for i in range(len(b)):
    for j in range(i,len(b)):
        if b[j] < b[i]: 
            b[i], b[j] = b[j], b[i]
            h[i], h[j] = h[j], h[i]

    try:
        if b[i] != b[i+1]:
            hoyde += h[i]    
        else:
            pass # her må du lage en måte å finne den høyeste høyden av de like verdiene i b listen.
    except IndexError:
        hoyde += h[i]

print(hoyde)

# [1,2,2,4,5,6,1] #hoyde
# [6,3,1,2,3,4,2] #bredde

# må plusse sammen høyden til alle de høydene med forskjellige bredder.
# så må man plusse på den høyeste høyden til de like breddene.

# sortere listen, men passe på at høyde og bredde verdiene fortsatt ligger sammen
# så gå gjennom listen med bredder, så lenge den neste ikke er lik 

# jeg to lister der det er like verdier i den ene skal jeg finne like verdier på den andre listen ved samme plass.