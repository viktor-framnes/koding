N = int(input())
prices = []

for i in range(N):
    b,o = map(int,input().split())
    prices.append(list((b,o)))

for i in range(N):
    dp_k = [0] * N  # Maks fortjeneste når bilen er i Kristiansand
    dp_o = [float('-inf')] * N  # Maks fortjeneste når bilen er i Oslo
    dp_b = [float('-inf')] * N  # Maks fortjeneste når bilen er i Bergen

    # Kristiansand: Vente eller bli oppdatert av retur fra Oslo/Bergen
    if i > 0:
        dp_k[i] = max(dp_k[i], dp_k[i - 1])  # Vente
    if i >= 2:
        dp_k[i] = max(dp_k[i], dp_o[i - 2])  # Tilbake fra Oslo
    if i >= 3:
        dp_k[i] = max(dp_k[i], dp_b[i - 3])  # Tilbake fra Bergen

        # Reise til Oslo: Oppdater på dag i+2
    if i + 2 < N:
        dp_o[i + 2] = max(dp_o[i + 2], dp_k[i] + prices[i + 2][1])

        # Reise til Bergen: Oppdater på dag i+3
    if i + 3 < N:
        dp_b[i + 3] = max(dp_b[i + 3], dp_k[i] + prices[i + 3][0])

        # Oslo/Bergen: Vente
    if i > 0:
        dp_o[i] = max(dp_o[i], dp_o[i - 1])  # Vente i Oslo
        dp_b[i] = max(dp_b[i], dp_b[i - 1])  # Vente i Bergen

    # Maksimum profit finnes i en av de tre tilstandene på siste dag
resultat = max(dp_k[-1], dp_o[-1], dp_b[-1])

print(resultat)  # Forventet output: 130
