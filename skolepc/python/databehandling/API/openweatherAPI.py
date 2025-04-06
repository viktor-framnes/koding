import requests

apiNøkkel = '19ee405a7f88fee2cc25853cc3321c68' # Rate limit: Maks 60 ganger i minuttet
by = 'Stavanger'

respons = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={by}&appid={apiNøkkel}",verify=False)
data = respons.json()
print(data)


absNull = -273.15 # grader celcius

temp = data["main"]["temp"] + absNull
tempFeel = data["main"]["feels_like"] + absNull
print(temp)
