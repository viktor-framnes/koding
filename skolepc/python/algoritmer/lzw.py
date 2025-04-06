t = "abcabc"
t = "Problemet er at du ikke vet om toget kommer, eller er i rute. Det er for uforutsigbart for hundretusenvis av folk."

lzw = {}
kode = 0
sekvens = ""

# Går gjennom teksten
for c in t:
    # print(f"ascii-kode {ord(c)}")
    if len(sekvens) >= 8:
        sekvens = ""
    else:
        sekvens += c
    if c not in lzw:
        lzw[c] = kode
        kode += 1
    if sekvens not in lzw:
        lzw[sekvens] = kode
        kode += 1

# for key,val in lzw.items():
    # print(key,val)

print()

ut = ""
sekvens_gammel = ""
for c in t:
    if len(sekvens) >= 8:
        sekvens = ""
    else: 
        sekvens += c
    if sekvens in lzw:
        sekvens_gammel = sekvens
        ut += str(bin(lzw[sekvens]))
    
print(ut)
lengde_tekst = len(t) * 8
forhold = len(ut) / lengde_tekst
print(f"Forholdet [tekst]:[ut_tekst] = {100*forhold:.1f}%")
print()
print(lzw)