N,Q = map(int,input().split())
S = input().upper()
S = S[:N]

def sjekkStilling():
    global stilling
    global sett
    if stilling[0] >= (stilling[1]+2):
        sett[0] += 1
        stilling = [0,0]
    if stilling[1] >= (stilling[0]+2):
        sett[1] += 1
        stilling = [0,0]

for i in range(Q):
    stilling = [0,0]
    sett = [0,0]
    teller = 0
    K,M = map(int,input().split())
    for j in range(len(S)):

        if S[j] == "A":
            stilling[0] += 1
        if S[j] == "B":
            stilling[1] += 1
        if stilling[0] >= K or stilling[1] >= K:
            sjekkStilling()

        teller += 1

        if M in sett:
            if sett[0] == M:
                print(f"A {teller}")
            else:
                print(f"B {teller}")
            break

        if teller >= N and M not in sett:
            print("X")
            break







