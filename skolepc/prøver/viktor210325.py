import pandas as pd
import matplotlib.pyplot as plt
"""Forkortet navnene i utslipp.csv filen og byttet fra ? til å"""
"""Byttet fra ? til Å i befolkning.csv filen"""
filnavn = "utslipp.csv"
filnavn2 = "befolkning.csv"
dt = pd.read_csv(filnavn, sep=";", header=1, encoding="utf-8")
df = pd.read_csv(filnavn2, sep=";", header=1, encoding="utf-8")

# print(dt.to_string())

# oppgave 1 a)
# print(f"{dt["År"][dt["Olje- og gass"].idxmax()]} var året mest høyest olje og gass utslipp")
# print(f"{dt["År"][dt["Veitrafikk"].idxmax()]} var året mest høyest veitrafikk utslipp")
# print(f"{dt["År"][dt["Luftfart etc."].idxmax()]} var året mest høyest luftfart etc. utslipp")
# print(f"{dt["År"][dt["Jordbruk"].idxmax()]} var året mest høyest jordbruk utslipp")
# print(f"{dt["År"][dt["Alle kilder"].idxmin()]} var året mest minst utslipp totalt")

# oppgave 1 b)
# gjennomsnitt = dt["Olje- og gass"].mean()
# print(f"{gjennomsnitt:.2f}* 1000 tonn ekvivalenter er det årlige gjennomsnittet av utslipp fra 'Olje og gassutvinning'")

# # oppgave 2 a)
# x = dt["År"]
# y1 = dt["Olje- og gass"]
# y2 = dt["Veitrafikk"]
# y3 = dt["Luftfart etc."]
# y4 = dt["Jordbruk"]
# plt.plot(x,y1,zorder=2,label="Olje- og gass")
# plt.plot(x,y2,zorder=3,label="Veitrafikk")
# plt.plot(x,y3,zorder=4,label="Luftfart etc.")
# plt.plot(x,y4,zorder=5,label="Jordbruk")
# plt.legend()
# plt.grid(zorder=0)
# plt.xlabel("År")
# plt.ylabel("Utslipp målt i 1000 tonn C02 ekvivalenter")
# plt.show()

# oppgave 2 b)
dt["Andre kilder"] = dt["Alle kilder"] - dt["Olje- og gass"] - dt["Veitrafikk"] - dt["Jordbruk"] - dt["Luftfart etc."] 
y = []  
titler = ["Olje- og gass","Veitrafikk","Luftfart etc.","Jordbruk","Andre kilder"]  
verdier = []
for i in range(2,7):
    y.append(dt.iat[-1,i]/dt.iat[-1,1]*100)
for i in range(len(titler)):
    verdier.append(f"{titler[i]} - {y[i]:.1f}%")
plt.pie(y,labels=verdier)
plt.title(label="Prosentvis fordeling av utslipp (2023)")
plt.show()


# oppgave 3
# try:
#     try:
#         print("Næringene er: Olje- og gass, Veitrafikk, Luftfart etc., Jordbruk, Andre kilder, Alle kilder")
#         aar = input("Hvilke år...")
#         nering = input("Hvilke næring...")
#         aar = int(aar)
#         x = list(dt["År"])
#         y = x.index(aar)
#         a = dt[nering][y]

#         x2 = list(df["År"])
#         y2 = x2.index(aar)
#         b = df["Personer"][y2]
#         z = (a*1000)/b

#         print(f"utslipp fra {nering} i {aar} var {a} * 1000 tonn C02 ekvivalenter og det var {b} innbyggere derfor blir det ca. {z:.1f} tonn C02-ekvivalenter per innbygger")
#     except KeyError:
#         print("Du må skrive en næring helt likt som vist over")
#         quit()
# except ValueError:
#     print("Du må skrive et år mellom 1990 og 2023 uten noe mellomrom")
#     quit()