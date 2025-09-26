def weekday_newyear(year:int):
    ukedager = ["man","tir","ons","tor","fre","lor","son"]
    x = year - 1900

    antall_skudd = (x-1) // 4
    
    dag = x-(antall_skudd*7) + antall_skudd
    if year == 1900:
        return f"{year} {ukedager[0]}"
    return f"{year} {ukedager[dag]}"

def is_workday(dag):
    arbeidsdager = [0,1,2,3,4]
    if dag in arbeidsdager:
        return True
    else:
        return False
    
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def workdays_in_year(year):
    dag = weekday_newyear(year).split()
    godedager = ["man","tir","ons","tor","fre"]

    if dag[1] in godedager:
        if is_leap_year(year) and dag[1] not in ["fre","lor"]:
            return 5*52+2
        else:
            return 5*52+1
    else:
        return 5*52
    
    
for i in range(20):
    tall = 1900 + i
    print(f"{tall} {workdays_in_year(tall)}")
