import requests as req

name = input().lower()
name2 = input().lower()

respons = req.get(f'https://pokeapi.co/api/v2/pokemon/{name}/', verify=False)
data = respons.json()
repons2 = req.get(f'https://pokeapi.co/api/v2/pokemon/{name2}/', verify=False)
data2 = repons2.json()

navn = data["forms"][0]["name"]
høyde = data["height"]
vekt = data["weight"]
moves = []
for i in range(len(data["moves"])):
    moves.append(data["moves"][i]["move"]["name"])
movesSet = set(moves) 

navn2 = data2["forms"][0]["name"]
høyde2 = data2["height"]
vekt2 = data2["weight"]
moves2 = []
for i in range(len(data2["moves"])):
    moves2.append(data2["moves"][i]["move"]["name"])
movesSet2 = set(moves2) 
fellesMoves = set(movesSet) & set(movesSet2)
fellesMoves = list(fellesMoves)

høyest = ""
if høyde > høyde2:
    høyest = navn
else:
    høyest = navn2
tyngst = ""
if vekt > vekt2:
    tyngst = navn
else:
    tyngst = navn2
if len(moves) > len(moves2):
    flestmoves = navn
else:
    flestmoves = navn2
print(f"Pokemon {navn} og {navn2}:\nDen høyeste er {høyest} og den tyngste er {tyngst}.\nDen med flest moves er {flestmoves}\n De har disse moves til felles {fellesMoves}")

print(f"{navn}, {vekt} vekt, {høyde} høyde")
print(f"{navn2}, {vekt2} vekt, {høyde2} høyde")
# tekst = "Typer:"
# utskrift = ""
# x = []
# for i in range(len(data["types"])):
#     utskrift += str(data["types"][i]["type"]["name"])
#     x.append(utskrift)
# print(tekst,x)

