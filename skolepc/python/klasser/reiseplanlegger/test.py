from flight import Flight
from reiserute import Reiserute
import datetime as dt

flights = []

flights.append(Flight("US230",dt.datetime(2014, 4, 5, 5, 5, 0),dt.datetime(2014, 4, 5, 6, 15, 0)))

flights.append(Flight("US235",dt.datetime(2014, 4, 5, 6, 55, 0),dt.datetime(2014, 4, 5, 7, 45, 0)))

flights.append(Flight("US237",dt.datetime(2014, 4, 5, 9, 35, 0),dt.datetime(2014, 4, 5, 12, 55, 0)))

reiserute = Reiserute(flights)

print(reiserute.getTotalTravelTime())

print(reiserute.getTotalFlightTime())
