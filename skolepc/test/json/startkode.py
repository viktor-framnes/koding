"""
Startkode for å lese inn fra filen personer.json.
data inneholder en liste med ordbøker som beskriver hver enkelt person
med formatet nedenfor:
[
    {
        "navn": "Kristine Wold",
        "alder": 97,
        "adresse": {
            "gateadresse": "Løkkegata 9",
            "postnummer": "1440",
            "by": "Narvik",
            "land": "Norge"
        },
        "interesser": [
            "Baking",
            "Maling",
            "Fiske"
        ],
        "gift": false
    },
...

]

"""

import json

filnavn = "personer.json"

# Åpner tekstfilen og gjør om fra json-format til en datastruktur
with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)

print(f"Datasettet er av typen {type(data)}")
# Går gjennom listen med ordbøker vi fikk fra tekstfilen...
