import json

filnavn = "oppskrifter.json"
with open(filnavn,encoding="utf-8") as fil:
    data = json.load(fil)

# oppgave 1
print(len(data["oppskrifter"])) # skriver ut antall oppskrifter

# oppgave 2
teller = 0
for oppskrift in data["oppskrifter"]:
    ingredienser = [ingrediens["ingrediens"] for ingrediens in oppskrift["ingredienser"]]
    if "Tomat" in ingredienser:
        teller += 1
print(teller) # skriver ut antall oppskrifter som inneholder Tomat

# oppgave 3
teller = 0
for oppskrift in data["oppskrifter"]:
    ingredienser = [ingrediens["ingrediens"] for ingrediens in oppskrift["ingredienser"]]
    if all(ingrediens in ingredienser for ingrediens in ["Egg", "Melk", "Hvetemel"]):
        teller += 1
print(teller) # skriver ut antall oppskrifter som inneholder egg, melk og hvetemel

# oppgave 4
rating = []
for oppskrift in data["oppskrifter"]:
    if oppskrift["rating"] == "NaN":
        continue
    else:
        rating.append(float(oppskrift["rating"]))
gjennomsnitt = sum(rating)/len(rating)
print(f"{gjennomsnitt:.3f}")

# oppgave 5
storst = 0
navn = ""
for oppskrift in data["oppskrifter"]:
    if len(oppskrift["ingredienser"]) > storst:
        navn = oppskrift["navn"]
        storst = len(oppskrift["ingredienser"])

print(navn)