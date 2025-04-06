import pandas as pd
import matplotlib.pyplot as plt

# oppgave 1
filnavn = "student_data.csv"
dt = pd.read_csv(filnavn,delimiter=",",na_values="-")

# oppgave 2
print(dt.head(5))

# oppgave 3
gjennomsnitt = dt["Alder"].mean()
print((gjennomsnitt))

# oppgave 4
x = list(dt["Karakter"])
print(x.count(6))

# oppgave 5
sortert = dt.sort_values(by="Oppmøte",ascending=False)
print(sortert)

# oppgave 6 
print(dt.iloc[[dt["Oppmøte"].idxmax()]])

# oppgave 7
dt["Bestått"] = True
for i in range(len(dt)):
    if dt["Oppmøte"][i] <= 85:
        dt["Bestått"][i] = False  
print(dt)

# oppgave 8
print(dt.groupby("Karakter")["Oppmøte"].mean())

# oppgave 9 
print(dt[dt["Alder"] >= 21]) # kan også f.eks. dt[(dt["Year"] >= 2000) & (df["Year"] <= 2010)] du kan ha flere betingelser, viser fra 2000 til 2010

# oppgave 10
x = list(set(dt["Karakter"]))
y = list(dt["Karakter"])
for i in range(len(x)):
    print(f"antall av karakter {i+1} er {y.count(x[i])}")

# oppgave 11
x = dt["StudentID"]
y = dt["Oppmøte"]
xlinje = list(x)

plt.bar(x,y,align="center",zorder=2)
plt.xticks(xlinje)
plt.ylim(70,101)
plt.grid(axis="y",zorder=0)
plt.show()

