import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filnavn = 'house-price.csv'
df = pd.read_csv(filnavn,header=0,delimiter=",")

gjennomsnittspris = df["price"].mean()
print(f"{gjennomsnittspris:.0f}kr er gjennomsnittprisen på hus")
makspris = df["price"].max()
print(f"{makspris}kr er det dyreste huset")
minpris = df["price"].min()
print(f"{minpris}kr er det billigste huset")

# Plotte pris på hus sammen med hvor mange soverom det er
df.plot(kind='scatter',x='bedrooms',y='price')
plt.ylabel("Pris [kr]")
plt.xlabel("Antall soveroom")
plt.title("Sammenheng mellom pris og antall soverom")

# Plotte pris på hus sammen med hvor mange etasjer det er
df.plot(kind="scatter",x="stories",y="price")
plt.ylabel("Pris [kr]")
plt.xlabel("Antall etasjer")
plt.title("Sammenheng mellom pris og antall etasjer")
plt.xlim(0, 5)

# Plotte sektor diagram av antall soverom
plt.figure("sektor diagram soverom")
x = set(df["bedrooms"])
soverom = list(x)

y = list(df["bedrooms"])
z = []
for i in range(len(soverom)):
    z.append(y.count(soverom[i]))

plt.pie(z,labels=soverom)
plt.title("Sektor diagram som viser foredling på hvor mange soverom det er")

# Plotte sektor diagram av antall bad
plt.figure("sektor diagram bad")
x = set(df["bathrooms"])
bad = list(x)

y = list(df["bathrooms"])
z = []
for i in range(len(bad)):
    z.append(y.count(bad[i]))

plt.pie(z,labels=bad)
plt.legend()
plt.title("Sektor diagram som viser foredling på hvor mange bad det er")
plt.show()
    