import json

filnavn = "transport.json"
with open(filnavn,encoding="utf-8") as fil:
    data = json.load(fil)

# oppgave a)
print(f"Det er {len(data["byer"])} byer i datasettet")

# oppgave b)
for by in data["byer"]:
    for i in range(len(by["stasjoner"])):
        if by["stasjoner"][i]["navn"] == "Chesham Broadway":
            print(f"stasjonen Chesham Broadway ligger i byen {by["navn"]}")

# oppgave c)
teller = 0
for by in data["byer"]:
    for i in range(len(by["stasjoner"])):
        kiosker = by["stasjoner"][i]["kiosker"]
        if "7-Eleven" in kiosker:
            teller += 1
print(f"{teller} 7-Eleven kiosker finnes")

# oppgave d)
teller = 0
for by in data["byer"]:
    for i in range(len(by["stasjoner"])):
        for j in range(len(by["stasjoner"][i]["ruter"])):
            destinasjoner = by["stasjoner"][i]["ruter"][j]["destinasjon"]
            if "Chesham Broadway" in destinasjoner:
                teller += 1
print(f"Det er {teller} stasjoner som har destinasjon Chesham Broadway")

# oppgave e)
tid = 0
antall = 0
for by in data["byer"]:
    for i in range(len(by["stasjoner"])):
        for j in range(len(by["stasjoner"][i]["ruter"])):
            if by["stasjoner"][i]["ruter"][j]["destinasjon"] == "Chesham Broadway":  
                x = by["stasjoner"][i]["ruter"][j]["tid"]
                y = int(x[0])
                tid += y
                antall += 1
gjennomsnitt = tid / antall
print(f"Den gjennomsnittlige tiden til Chesham Broadway er {gjennomsnitt:.1f} timer")