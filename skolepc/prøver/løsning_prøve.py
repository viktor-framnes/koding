import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importerer data fra fil
filename = "utslipp.csv"
df = pd.read_csv(filename, delimiter=";",header=1, encoding="latin1")

#Endrer kolonnenavn slik at de blir enklere å jobbe med
kolonnenavn = ["År", "Totalt utslipp", "Olje- og gassutvinning", "Veitrafikk", "Luftfart etc.", "Jordbruk" ]
df.columns = kolonnenavn

#Oppgave 1a
print("\nOppgave 1A:")
#Bruker kolonnenavnene til å hente ut maks utslipp fra hver kategori. Starter derfor fra og med indeks 2
for kategori in kolonnenavn[2:]:
    maks_utslipp = df[kategori].max()
    
    #Lager en df med raden(e) lik maks utslipp
    maks_utslipp_df = df[df[kategori] == maks_utslipp]
    #Henter ut året for maks utslipp
    maks_år = maks_utslipp_df["År"].values[0]
    
    print(f"Maks utslipp ({maks_utslipp}) for {kategori} var i år {maks_år}")

"""Alternativ løsning ved bruk av .idmax():
maks_index = df["Olje- og gassutvinning"].idxmax()
maks_verdi = df.loc[maks_index,"Olje- og gassutvinning"]
maks_år = df.loc[maks_index, "År"]
print(maks_verdi, maks_år)"""

#Henter laveste verdi i totalt utslipp
minst_utslipp = df["Totalt utslipp"].min()
#Henter ut raden(e) lik minst utslipp
minst_utslipp_df = df[df["Totalt utslipp"] == minst_utslipp]
#Henter ut året for minst utslipp
minst_år = minst_utslipp_df["År"].values[0]

print(f"\nDet minste totale utslippet ({minst_utslipp}) var i år {minst_år}")



#Oppgave 1b 
print("\nOppgave 1B:")

gjennomsnitt = df["Olje- og gassutvinning"].mean()
gjennomsnitt = gjennomsnitt.round()
print(f"Det gjennomsnittlige utslippet i Olje- og gassutvinning er {gjennomsnitt}")

#Oppgave 2a
print("\nOppgave 2A:")

df.plot(x = "År",kind="line")
plt.title("Oversikt over utslipp fordelt på ulike næringer")
plt.ylabel("CO$_2$-ekvivalenter [1000 Tonn]")
plt.savefig("linjediagram.png")

# plt.show()
plt.close() #Sletter figuren fra minnet

#Oppgave 2b
print("\nOppgave 2B:")

#Velger raden som inneholder år 2023
df_2023 = df[df["År"]==2023]

#Fjerner "År" og "Totalt utslipp" fra dfen
utslipps_kategorier = df_2023.drop(columns=["År", "Totalt utslipp"])
#Legger til en kolonne som er differansen mellom totalt utslipp og utslippskategoriene
utslipps_kategorier["Andre kilder"] = df_2023["Totalt utslipp"].values[0] - utslipps_kategorier.sum(axis=1)
#Finner prosentandelen av totalutslippet
prosentandeler = (utslipps_kategorier.iloc[0] / df_2023["Totalt utslipp"].values[0]) * 100

# Plot sektordiagram
prosentandeler.plot(kind="pie", autopct="%.1f%%", startangle=90, colormap="viridis")
plt.ylabel("") #Fjerner indeksnummeret fra plottet 
plt.title("Prosentvis fordeling av utslipp (2023)")
plt.savefig("sektordiagram.png")
# plt.show()


#Oppgave 3 
print("\nOppgave 3")
#Henter inn data om Norges befolkning
filnavn_befolkning = "befolkning.csv"
df_befolkning = pd.read_csv(filnavn_befolkning, sep=";",header=1,encoding="latin1")
df_befolkning.columns = ["År","Befolkning"] #Endrer kolonnenavnene



#Løkke som sørger for at input er gitt på riktig format
print("Velg mellom: \n1 Totalt utslipp \n2 Olje- og gassutvinning \n3 Veitrafikk \n4 Luftfart etc.\n5 Jordbruk")
while True:
    næring = input("Skriv inn ønsket næring(1-5):\n")
    år = input("Skriv inn ønsket år (1990-2023):\n")
    try:
        i = int(næring)
        næring = df.columns[i]
    except (ValueError,IndexError):
        print("Ugyldig næring valgt. Skriv et tall mellom 1 og 5. \nPrøv igjen:")
        continue
    try:
        år = int(år)
        if (år<1990) or (år>2023):
            raise ValueError
        else:
            break
    except ValueError:
        print("Ugyldig år valgt. Velg et år mellom 1990 og 2023. \nPrøv igjen:")
        
#Lager en ny kolonne med utslipp(gitt næring)/befolkningstall
df[f"Utslipp per innbygger({næring})"]=df[næring]/df_befolkning["Befolkning"]
#Henter ut kun fra det angitte året
filtrert_df_år = df[df["År"] == år]
#Henter ut verdien til "Utslipp per innbygger" for det gitte året
utslipp_per_pers = filtrert_df_år[f"Utslipp per innbygger({næring})"].values[0]
#Ganger med 1000 for å få benevningen tonn
utslipp_per_pers_tonn = utslipp_per_pers * 1000
#If-setning som sørger for riktig print
if næring == "Totalt utslipp":
    print(f"Det totale utslippet per person i {år} var {utslipp_per_pers_tonn:.2f} tonn CO2-ekvivalenter")
else:
    print(f"Utslippet per person i {år} fra {næring} var {utslipp_per_pers_tonn:.2f} tonn CO2-ekvivalenter")



