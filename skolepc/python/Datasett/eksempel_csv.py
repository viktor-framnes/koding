import matplotlib.pyplot as plt
import pandas as pd

# Opprett en variabel med navn på filen du skal bruke
filnavn = "befolkning.csv"

df = pd.read_csv(filnavn,header=1,delimiter=";")
# usecols=["Personer"] , for å bare vise en kolonne

# For å hente ut informasjon fra en kolonne: df["Navn_på_kolonne"]
plt.plot(df["År"],df["Personer"])
plt.xlabel("År")
plt.ylabel("Antall Personer")
plt.grid()
plt.show()

print(df)