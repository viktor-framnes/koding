N, K = map(int, input().split())

hus_tilstand = [1] * N

for _ in range(K):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if hus_tilstand[i] == 1:
            hus_tilstand[i] = 0
        else:
            hus_tilstand[i] = 1

antall_med_internett = sum(hus_tilstand)
print(antall_med_internett)