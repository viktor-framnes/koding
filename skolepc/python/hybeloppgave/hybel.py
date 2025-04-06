hus = [
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None]
]
kart = [
    ["Ledig","Ledig","Ledig","Ledig"],
    ["Ledig","Ledig","Ledig","Ledig"],
    ["Ledig","Ledig","Ledig","Ledig"]
]
regnskap = {}


def flytt_inn(i,j,navn,epost,mobil):
    hus[i][j] = {"navn":navn,"epost":epost,"mobil":mobil}
    kart[i][j] = "Opptatt"
    registrer_betaling(navn,7000)

def flytt_ut(i,j):
    hus[i][j] = None
    kart[i][j] = "Ledig"

def sjekk_ledig_hybel(i,j):
    if hus[i][j] != None:
        return "opptatt"
    else:
        return "ledig"

def flytt_mellom_hybler(i,j,k,l):
    if sjekk_ledig_hybel(l,k) == "ledig":
        hus[k][l] = hus[i][j]
        hus[i][j] = None
        kart[k][l] = kart[i][j]
        kart[i][j] = "Ledig"
    else:
        return "Det var opptatt der"
    
def vis_status():
    for x in kart:
        for i in range(0,len(x)-1):
            print(f"{x[i]:8}",end=" ")
        print(f"{x[-1]:8}")

def registrer_betaling(student_navn,beløp):
    regnskap[student_navn] = beløp

flytt_inn(1,1,"Viktor","epost@123","991")
vis_status()
flytt_mellom_hybler(1,1,2,2)
print()
vis_status()
print()
print(regnskap) 
