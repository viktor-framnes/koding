import random

# Input: N = antall hus, K = antall lynnedslag
N, K = map(int, input().split())

# Bruker en liste for å holde styr på tilstanden til hvert hus
# 0 = internett av, 1 = internett på
hus_tilstand = [1] * N

for _ in range(K):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        # Bytt tilstand: 1 -> 0 eller 0 -> 1
        hus_tilstand[i] ^= 1

# Tell antall hus med internett på (verdi 1)
antall_med_internett = sum(hus_tilstand)
print(antall_med_internett)

# Test-generator
# Definer funksjon som genererer tester automatisk
def generate_test(N, K, max_range=100000):
    print(N, K)
    for _ in range(K):
        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        a, b = min(a, b), max(a, b)  # Sikrer at a <= b
        print(a, b)

# Eksempel på bruk av test-generator
if __name__ == "__main__":
    N_test, K_test = 10, 5
    generate_test(N_test, K_test)
