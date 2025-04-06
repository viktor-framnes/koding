import random
N, M = map(int,input().split())
S = input().upper()
sta = []
ledere = []
par = []
daleder = ""

#legger alle personligheter i lister fordelt på de sta og lederne.
for _ in range(M):
    O, U = input().upper().split()
    sta += O
    ledere += U

#hvis det er en åpenbar leder ingen har et problem med.
for x in S:
    if x not in ledere:
        daleder = x

for i in range(len(S)):
    if S[i+1] != S[i]:
        pass


print(sta)
print(ledere)
print(daleder)
