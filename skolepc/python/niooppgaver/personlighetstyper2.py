def min_departments(N, M, S, incompatibilities):
    # Bygg inkompatibilitetstabellen
    incompatible = {chr(c): set() for c in range(ord('A'), ord('Z') + 1)}
    for O, U in incompatibilities:
        incompatible[O].add(U)

    # Iterer gjennom strengen S for å dele opp i avdelinger
    departments = 0
    current_department = set()
    

    for i, char in enumerate(S):
        # Sjekk om char er inkompatibel med gjeldende avdeling
        if any(c in incompatible[char] for c in current_department):
            # Start en ny avdeling
            departments += 1
            current_department.clear()
        
        # Legg til denne typen i den nåværende avdelingen
        current_department.add(char)

    # Legg til siste avdeling om nødvendig
    if current_department:
        departments += 1

    print(current_department)
    print(incompatible)

    return departments

# Eksempel på input
N = 14
M = 3
S = "AABCABCCACACBB"
incompatibilities = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'A')
]



result = min_departments(N, M, S, incompatibilities)
print(f"Minimum number of departments: {result}")
