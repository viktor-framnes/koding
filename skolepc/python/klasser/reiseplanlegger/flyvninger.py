from flight import Flight
import datetime as dt

flyvninger = []

flyvning1 = Flight()
flyvning1.setFlynummer("1154")
flyvning1.setAvreise(2024,3,2,13,25)
flyvning1.setAnkomst(2024,3,2,19,30)
flyvning2 = Flight()
flyvning2.setFlynummer("1244")
flyvning2.setAvreise(2024,3,3,12,10)
flyvning2.setAnkomst(2024,3,3,14,40)
flyvning3 = Flight()
flyvning3.setFlynummer("1054")
flyvning3.setAvreise(2024,3,4,9,5)
flyvning3.setAnkomst(2024,3,4,10,0)

flyvninger.append(flyvning1)
flyvninger.append(flyvning2)
flyvninger.append(flyvning3)

for x in flyvninger:
    x.getFlynummer()
    x.getAvreise()
    x.getAnkomsttid()
    x.getFlightTime()
    print()

flyvninger[0].setFlynummer("0001")
flyvninger[1].setAvreise(2024,11,1,13,47)
flyvninger[2].setAnkomst(2024,3,4,11,0)

for x in flyvninger:
    x.getFlynummer()
    x.getAvreise()
    x.getAnkomsttid()
    x.getFlightTime()
    print()