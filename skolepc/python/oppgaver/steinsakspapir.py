import random

spillerValg = input("Stein, Saks eller Papir? ").upper()

valg = ["STEIN", "SAKS", "PAPIR"]
datamaskinValg = valg[random.randint(0,2)]

if spillerValg == "STEIN":  
    if datamaskinValg == "STEIN":
        print("Uavgjort")
    elif datamaskinValg == "SAKS":
        print("Du vant")
    elif datamaskinValg == "PAPIR":
        print("Du tapte")
    
elif spillerValg == "SAKS":
    if datamaskinValg == "STEIN":
        print("Du tapte")
    elif datamaskinValg == "SAKS":
        print("Uavgjort")
    elif datamaskinValg == "PAPIR":
        print("Du vant")
 
elif spillerValg == "PAPIR":
    if datamaskinValg == "STEIN":
        print("Du vant")
    elif datamaskinValg == "SAKS":
        print("Du tapte")
    elif datamaskinValg == "PAPIR":
        print("Uavgjort")

else:
    print("Du må skrive: stein, saks eller papir")
    quit()

print(f"Du valgte {spillerValg}, mens datamaskinen valgte {datamaskinValg}")