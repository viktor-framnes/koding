import requests
from pprint import pprint

places = {
    "Trondheim": {"lat": 63.43, "lon": 10.39},
    "Oslo": {"lat": 59.91, "lon": 10.75},
    "Bergen": {"lat": 60.39, "lon": 5.32},
    "Avaldsnes": {"lat": 59.35, "lon": 5.27},
    "Tromsø": {"lat": 69.64, "lon": 18.95},
}

def get_air_temp(lat,lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    response = requests.get(url)
    response2 = response.json()
    print(response2["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])

def get_air_temp2(place):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={places[place]["lat"]}&lon={places[place]["lon"]}"
    response = requests.get(url)
    response2 = response.json()
    print(response2["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])
    

get_air_temp(input(),input())
# get_air_temp2(str(input()))