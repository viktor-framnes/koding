# før         menn       etter
# beate    <- arne   ->  ane
# dagmar   <- david  ->  beate
# caroline <- bjarne ->  dagmar
# ane      <- carl   ->  caroline

# før [beate,caroline,ane,dagmar]
# menn [arne,bjarne,carl,david]
# etter [ane,dagmar,caroline,beate]

# svar: arne, david, bjarne, carl

n = int(input())

før = [""]*n
menn = [""]*n
etter = [""]*n
for i in range(n):
    menn[i], før[i], etter[i] = input().split()

for i in range(n-1):
    indeks = etter.index(før[i])
    før[i+1], menn[i+1], etter[i+1], før[indeks], menn[indeks], etter[indeks] = før[indeks], menn[indeks], etter[indeks], før[i+1], menn[i+1], etter[i+1]

print(menn)