# import json
# indeks = 0

# with open('dataJSON.json',encoding="utf-8") as fil:
#     data = json.load(fil)

# #oppgave 1 fra onenote
# print(data["butikker"][0]["produkter"][1]["antall_solgt"][1])

# #oppgave 2 fra onenote
# print(data["butikker"][1]["vær"]["temperatur"][1])

# # oppgave 3 fra onenote
# y = data["butikker"][0]["produkter"][0]["antall_solgt"]
# indeks = y.index(max(y))
# print(indeks)

# #oppgave 4 fra onenote
# y = data["butikker"][2]["vær"]["nedbør"]
# indeks = y.index(max(y))
# print(indeks)
# print()

# #oppgave 5 fra onenote
# y = data["butikker"][2]["vær"]["temperatur"]
# for i in range(len(y)):
#     if y[i] < -5:
#         print(y.index(y[i]), "indeks")

# #oppgave 6 fra onenote
# x = []
# y = data["butikker"][1]["produkter"][1]["antall_solgt"]
# for i in range(len(y)):
#     if 15 < y[i]:
#         x.append(y.index(y[i]))
# print(x)

# ---------------------------------------------------

# Oppgave 13 fra aunivers

import json
import matplotlib.pyplot as plt
import numpy as np

filnavn = "lonnstabell.json"
with open(filnavn, 'r', encoding='utf-8') as fil:
    data = json.load(fil)

# Lage lister med årstall, lønn for kvinner og lønn for menn
aarstall = data["dataset"]["dimension"]["Tid"]["category"]["index"]
alle_aarstall = list(aarstall.keys()) # Henter ut verdiene fra ordboken

lonn_kvinner = data["dataset"]["value"][6:]
lonn_menn = data["dataset"]["value"][:6]

# Plotting av gjennomsnittslønn for kvinner og menn
plt.figure('Linjegraf')
plt.plot(alle_aarstall, lonn_kvinner, label = "Kvinner")
plt.plot(alle_aarstall, lonn_menn, label = "Menn")

plt.legend()
plt.xlabel("Årstall")
plt.ylabel("Gjennomsnittslønn [kr]")
plt.title("Utvikling av gjennomsnittslønn")
plt.grid(axis="y")

# Plotting av gruppert stolpediagram
bar_width = 0.35
indeks = np.arange(len(alle_aarstall))

plt.figure("Stolediagram")
plt.bar(indeks - bar_width/2, lonn_kvinner, bar_width, label = "Kvinner")
plt.bar(indeks + bar_width/2, lonn_menn, bar_width, label = "Menn")
plt.xticks(indeks,alle_aarstall)

plt.legend()
plt.xlabel("Årstall")
plt.ylabel("Gjennomsnittslønn [kr]")
plt.title("Utvikling av gjennomsnittslønn")
plt.grid(axis="y")

plt.show()
