import json

filnavn = "ordbok.json"
#filnavn = "liste.json"

# Åpner tekstfilen og gjør om fra json-format til en ordbok
with open(filnavn, encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
# Skriver ut ordboken vi fikk fra tekstfilen.
for key, value in data.items():
    print(key,value)