import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('konsumprisindeks.csv',delimiter=";",decimal=",")

måneder = ["Jan","Feb","Mar","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Des"]
v = []
w = []

v2 = []
w2 = []

#1a
for i in måneder:
    a = df[i].min()
    v.append(a)
    b = list(df[i])
    w.append(df["År"][b.index(a)])

for i in måneder:
    a = df[i].max()
    v2.append(a)
    b = list(df[i])
    w2.append(df["År"][b.index(a)])

minsteVerdi = min(v)
indeks = v.index(minsteVerdi)
if v.count(minsteVerdi) > 1:
    print("Det var flere år som hadde den minste verdien")
    for i in range(v.count(minsteVerdi)):
        if v[i] == minsteVerdi:
            print(f"Minste verdi var {minsteVerdi} og det var i år {w[i]} og i måned {måneder[i]}")
else:
    print(f"Minste verdi var {minsteVerdi} og det var i år {w[indeks]} og i måned {måneder[indeks]}")

maxVerdi = max(v2)
indeks2 = v2.index(maxVerdi)
if v2.count(maxVerdi) > 1:
    print("Det var flere år som hadde den største verdien")
    for i in range(v2.count(maxVerdi)):
        if v2[i] == maxVerdi:
            print(f"Maks verdi var {maxVerdi} og det var i år {w2[i]} og i måned {måneder[i]}")
else:
    print(f"Maks verdi var {maxVerdi} og det var i år {w2[indeks2]} og i måned {måneder[indeks2]}")

#1b
differanse = 0
for i, year in enumerate(df["År"][1:],start=1):
    if df["Des"][i]-df["Jan"][i]>differanse:
        differanse = df["Des"][i]-df["Jan"][i]
        verdi_jan = df["Jan"][i]
        verdi_des = df["Des"][i]
        år = year

print(f"\nOppgave 1b\nDen største differansen mellom Januar og Desember skjedde i {år}\nhvor differansen var {differanse:.1f} (Januar:{verdi_jan}, Desember:{verdi_des})\n")

# Oppgave 2a
x_verdier = list(df["År"])
y_verdier = list(df["Årsgj.snitt2"])

plt.figure("Oppgave 2a")
plt.plot(x_verdier,y_verdier)
plt.grid(axis="y")
plt.xlabel("år")
plt.ylabel("gjennomsnitt")
plt.show()

#Oppgave 2b
x_verdier = []
y_verdier = []

for i,z in enumerate(måneder,start=1):
    if df[z][0] > 0:
        y_verdier.append(df[z][0])
        x_verdier = måneder[:i]
print(x_verdier)
print(y_verdier)

plt.figure("Oppgave 2b")
plt.bar(x_verdier,y_verdier)
plt.grid(axis="y")
plt.xlabel("måneder")
plt.ylabel("konsumprisindeks")
plt.show()

#oppgave 3

def kalkis(beløp,fra_år,til_år):
    v = list(df["År"])
    w = list(df["Årsgj.snitt2"])
    x = w[v.index(fra_år)]
    y = w[v.index(til_år)]

    return f"Varen kostet {(y*beløp)/x:.1f} kroner"


print(kalkis(45,2000,2010))


# kolonne_navn = ["År","Årsgj.snitt2","Jan","Feb","Mar","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Des"]
# df["Årsgj.snitt2"] = pd.to_numeric(df["Årsgj.snitt2"])
# max_verdi = 0
# min_verdi = 100
# for navn in kolonne_navn[2:]:
#     df[navn] = pd.to_numeric(df[navn])
#     for i,element in enumerate(df[navn]):
#         if element>max_verdi:
#             max_verdi = element
#             max_måned = navn
#             max_år = df["År"][i]
#         if element<min_verdi:
#             min_verdi = element
#             min_måned = navn
#             min_år = df["År"][i]

# print(f"Konsumprisindeksen var størst i {max_måned} {max_år} og var på {max_verdi}")
# print(f"Konsumprisindeksen var minst i {min_måned} {min_år} og var på {min_verdi}")