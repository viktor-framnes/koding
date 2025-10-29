def visbrett():
    for i in range(len(synligbrett)):
        for j in range(len(synligbrett[0])):
            print(f"{synligbrett[i][j]}", end=" ")
        print("",end="\n")

def sjekkvunnet():
    for i in range(len(vinnermuligheter)):
        [a,b,c] = vinnermuligheter[i]
        if spillbrett[a] and spillbrett[a] == spillbrett[b] and spillbrett[a] == spillbrett[c]:
            return True 

def navn(a,b):
    spillere = {0:a, 1:b}
    return spillere

def sjekkgyldig(x,y):
    x = int(x)
    y = int(y)
    if x < 4 and y < 4 and synligbrett[y-1][x-1] == "_":
        synligbrett[y-1][x-1] = symbol[karakter]
        spillbrett[(y-1)*3+(x-1)] = symbol[karakter]
        return True
    else:
        print("Det var en brikke der eller så skrev du forbi koordinatsystemet")

        
spillbrett = ["","","","","","","","",""]
symbol = {0:"O",1:"X"}
vinnermuligheter = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
synligbrett = [["_" for i in range(3)] for j in range(3)]
karakter = 0
spillere = navn(input("Spiller1 skriv ditt navn:"), input("Spiller2 skriv ditt navn:"))
kjor = True 

while kjor:
    karakter ^= 1
    print()
    visbrett()
    print()
    if sjekkvunnet():
        print(f"Gratulerer spiller {spillere[karakter]} vant!")
        kjor = False
    elif "" not in spillbrett:
        print("Det ble uavgjort") 
        kjor = False
    else: 
        if sjekkgyldig(input("1-3, x: "),input("1-3, y: ")):
            pass
        else:
            karakter ^= 1
    

