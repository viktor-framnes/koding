# link til oppgavene: 
"""
Valg jeg har gjort med datasettet:
- endret ? til å i kolonnenavnene
- endret navn fra 'Levendefødte i alt' til 'Fødselstall' 
"""
# Eksmanesoppgaver våren 2025
# Oppgave 8
# a)
import pandas as pd
import matplotlib.pyplot as plt

filnavn = "Datasett_fodselstall.csv"
# kan bruke delimiter="" eller sep=""
df = pd.read_csv(filnavn, delimiter="\t", encoding="utf-8", na_values="..") # bruker na_values=".." for å kunne regne selv om det ikke var noen verdier i csv filen, trengs for oppgave b)

print(df.to_string()) # printer ut hele tabllen uten ... for å forkorte ved å bruke .to_string()

# b)

df["Netto Folkevekst"] = df["Fødselstall"] + df["Innflyttinger"] - df["Utflyttinger"]
print(df.to_string())

# c)

årStart, årSlutt = map(int,input("Skriv inn start- og sluttsår [1945 2024]: ").split())
årStart = årStart - df["År"][0]
årSlutt = årSlutt - df["År"][0] + 1
x = df["År"][årStart:årSlutt]
y = df["Netto Folkevekst"][årStart:årSlutt]

plt.plot(x,y)
plt.show()

# metode 2 på c)
# df_sample = df.loc[årStart:årSlutt]
# print(df_sample)
# plt.plot(df_sample.index,df_sample["Netto Folkevekst"])
# plt.show()

