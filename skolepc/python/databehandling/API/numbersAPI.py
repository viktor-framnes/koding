import requests as req

tall = input()
url = f"http://numbersapi.com/{tall}" #kan også ha ?json på slutten av url'en

resultat = req.get(url)
teksten = resultat.text
# data = resultat.json()

# print(f"Statuskode: {resultat.status_code}")
print(teksten)