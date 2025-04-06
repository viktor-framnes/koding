import json

filnavn = "personer.json"
#filnavn = "liste.json"

# Åpner tekstfilen og gjør om fra json-format til en ordbok
with open(filnavn, encoding="utf-8") as f:
    data = json.load(f)

b = []
c = 0
for person in data:
    a = person["alder"]
    if a == 60:
        b += person["interesser"]
    
for x in b:
    if x == "Musikk":
        c = c + 1 

print(c)

    


