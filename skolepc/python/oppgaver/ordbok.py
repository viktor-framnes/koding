"""
Ordbok med python
"""

noedetater = {
    "113": "Ambulanse",
    "112": "Politi",
    "110": "Brann"
}

#Loope med nøkkel
for nøkkel in noedetater:
    print(nøkkel)

#Loope med verider
for verdi in noedetater.values():
    print(verdi)

#Loope med keys
for nøkkel in noedetater.keys():
    print(nøkkel, noedetater[nøkkel]) #Henter ut verdi ved hjelp av nøkkel

#Loope med både nøkkel og verdi
for key, val in noedetater.items():
    print(key,val)

print(f"110 hører til {noedetater['110']}") #Må bruke to ulike anførselstegn.