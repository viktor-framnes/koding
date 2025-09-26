def weekday_newyear(year:int):
    ukedager = ["man","tir","ons","tor","fre","lor","son"]
    x = year - 1900
    dag = 0

    antall_skudd = (x-1) // 4
   

    dag = x-(antall_skudd*7) + antall_skudd
    if year == 1900:
        return year, ukedager[0]    
    return year, ukedager[dag]


for i in range(19):
    tall = 1900 + i
    print(weekday_newyear(tall))


