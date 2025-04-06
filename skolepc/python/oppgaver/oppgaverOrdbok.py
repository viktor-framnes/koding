#oppgave 1
person = {
    "fornavn": "Viktor",
    "etternavn": "Framnes",
    "foedselsaar": "2006"
}

print(f"Mitt navn er {person['fornavn']} {person['etternavn']} og jeg er født i {person['foedselsaar']}")

#Oppgave 2
mandag = {
    
}

mandag["dato"] = "16.09.2024"
mandag["maksimumstemperatur"] = 16
mandag["minimumstemperatur"] = 13
mandag["nedbørsmengde"] = 3.4
mandag["vindstyrke"] = 2

print(f"Datoen i dag er {mandag['dato']}, dagens maksimumstemperatur er {mandag['maksimumstemperatur']} grader og minimumstemperaturen er {mandag['minimumstemperatur']} grader. Det er meldt {mandag['nedbørsmengde']} mm regn og en vindstyrke på {mandag['vindstyrke']} m/s")

#Oppgave 3
ordbok = {
    "variabel": "noe som lagrer en verdi",
    "datatype": "forklarer hva en verdi er",
    "operator": "det du bruker for å regne",
    "loekke": "noe som går gjennom flere ganger"
}

#Oppgave 4
krypter = {}
alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b"]

for i in range(len(alfabet) - 2):
    krypter[alfabet[i]] = alfabet[i+2]

print(krypter)