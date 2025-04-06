from random import randint
n = 6
tall = []
for i in range(1000000):
    tall.append(randint(1,n))

#lager statistikk
statistikk = {}
for verdi in tall:
    if verdi in statistikk:
        statistikk[verdi] += 1
    else:
        statistikk[verdi] = 1

print(statistikk)
vanligste = max(statistikk.values())
for key,val in statistikk.items():
    if val == vanligste:
        print(f"Vanligste tall: {key} med {val} forekomster")

gjennomsnitt = 0
sum = 0
for val in statistikk.values():
    sum += val
    gjennomsnitt = sum/n
print(f"Gjennomsnittet er {gjennomsnitt}")