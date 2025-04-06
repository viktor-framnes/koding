import datetime as dt

class Reiserute:
    def __init__(self, trips = []) -> None:
        self.trips = trips
        self.sortering()
        
    def sortering(self):
        for i in range(len(self.trips)):
            for j in range(i,len(self.trips)):
                if self.trips[i].avreisetid > self.trips[j].avreisetid:
                    self.trips[i], self.trips[j] = self.trips[j], self.trips[i]
        
    def getTotalFlightTime(self):
        totTid = 0
        for x in self.flights:
            tid = x.ankomsttid - x.avreisetid
            totTid += tid.seconds / 60
        return f"Det totale fly tiden er {totTid:.0f} min"

    def getTotalTravelTime(self):
        tid = self.trips[-1].ankomsttid - self.trips[0].avreisetid
        return f"Den totale reisetiden er {(tid.seconds / 60):.0f} min"

def main():
    from flight import Flight
    flights = []    
    flights.append(Flight("US230",dt.datetime(2014,4,5,5,5),dt.datetime(2014,4,5,6,15)))
    flights.append(Flight("US235",dt.datetime(2014,4,5,6,55),dt.datetime(2014,4,5,7,45)))
    flights.append(Flight("US240",dt.datetime(2014,4,5,2,55),dt.datetime(2014,4,5,4,45)))
    

    reiserute = Reiserute(flights,["boat","tog","buss"])

    print(reiserute.getTotalFlightTime())
    print(reiserute.getTotalTravelTime())

if __name__ == "__main__":
    main()