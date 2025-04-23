import pandas as pd
import json


filnavn = "oppskrifter.json"

# dt = pd.read_json(filnavn)

# print(dt.to_string())

with open(filnavn,encoding="utf-8") as fil:
    data = json.load(fil)

print(len(data["oppskrifter"]))

