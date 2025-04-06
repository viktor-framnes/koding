import requests

print("Oppgave 1")
def get_pokemon_info():
    """Funksjon som henter navn på en pokemon fra bruker 
        og viser informasjon om det"""
    
    # Få Pokemon-navn fra bruker
    pokemon_navn = input("Skriv inn navnet på en Pokemon: ").lower() #bruker lower for å sikre at input er små bokstaver
    
    # Lag URL og send forespørsel
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_navn}"
    response = requests.get(url)
    
    if response.status_code == 200: #Sjekker om forespørselen var vellykket
        data = response.json() #Konverterer responsen til JSON
        
        # Hent ut informasjon
        navn = data['name'].title() # .title() sørger for at første bokstav i navnet er stor
        hoyde = data['height'] / 10  # Height er gitt i desimeter og derfor konverterer vi til meter
        vekt = data['weight'] / 10  # Weight er gitt i 100 gram og derfor konverterer vi til kg
        
        if len(data['types']) > 1: #Sjekker om pokemonen har flere typer
            typer = [data['types'][0]['type']['name'], data['types'][1]['type']['name']]
        else:
            typer = [data['types'][0]['type']['name']]
        
        # Printer informasjonen
        print(f"\nInformasjon om {navn}:\n\
        Høyde: {hoyde} m\n\
        Vekt: {vekt} kg\n\
        Type(r): {', '.join(typer)}") #.join() brukes for å ta ut hvert element i listen og sette komma mellom dem
    else:
        print(f"Feil: Kunne ikke finne Pokemon. Er du sikker på at {pokemon_navn} er et gyldig Pokemon navn?")

# Kjør programmet
get_pokemon_info()

print("\nOppgave 2")
def sammenlign_pokemon():
    """Funksjon som sammenligner to Pokemon og viser informasjon om dem"""
    
    # Hent navn på to Pokemon
    pokemon1_name = input("Skriv navn på første Pokemon: ").lower()
    pokemon2_name = input("Skriv navn på andre Pokemon: ").lower()
    
    # Hent data for begge Pokemon
    pokemon1_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon1_name}").json()
    pokemon2_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon2_name}").json()
    
    # Hent ut moves for hver Pokemon
    pokemon1_moves = []
    pokemon2_moves = []
    for move in pokemon1_data['moves']:
        pokemon1_moves.append(move['move']['name'])
    for move in pokemon2_data['moves']:
        pokemon2_moves.append(move['move']['name'])
    
    # Finn felles moves
    felles_moves = list(set(pokemon1_moves) & set(pokemon2_moves)) # Konverterer listene til mengder (set) og finner felles elementer ved hjelp av &
    
    # Lager en liste med hver rad som en liste med informasjon
    sammenlign_data = [
        ["Navn", pokemon1_data['name'].title(), pokemon2_data['name'].title()],
        ["Høyde", f"{pokemon1_data['height']/10}m", f"{pokemon2_data['height']/10}m"],
        ["Vekt", f"{pokemon1_data['weight']/10}kg", f"{pokemon2_data['weight']/10}kg"],
        ["Antall moves", len(pokemon1_moves), len(pokemon2_moves)]
    ]
    
    # Vis resultat
    print("\nSammenligning:")
    headers=["Egenskap", "Pokemon 1", "Pokemon 2"]
    print(f"{headers[0]:<15} {headers[1]:<15} {headers[2]:<15}") # <15 sørger for at alle kolonnene er 15 tegn brede
    for row in sammenlign_data:
        print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15}")
    
    print(f"\nFelles moves ({len(felles_moves)}):")
    for move in felles_moves[:5]:  # Viser bare de 5 første
        print(f"- {move}")
    if len(felles_moves) > 5:
        print("... og flere!")

# Kjør programmet
sammenlign_pokemon()

print("\nOppgave 3")
def get_pokemon_by_type():
    """Funksjon som viser alle tilgjengelige Pokemon-typer og lar brukeren velge en type"""
    
    # 1. Hent alle typer
    types_url = "https://pokeapi.co/api/v2/type"
    response = requests.get(types_url)
    
    if response.status_code == 200:
        types_data = response.json()
        
        # Vis alle tilgjengelige typer
        print("\nTilgjengelige Pokemon-typer:")
        for i, type_info in enumerate(types_data['results'], 1): # Bruker enumerate fordi vi vil nummerere typene
            print(f"{i}. {type_info['name']}")
        
        # 2. La brukeren velge type
        valgt_type = input("\nVelg en type (skriv navnet): ").lower()
        
        # 3. Hent Pokemon av valgt type
        type_url = f"https://pokeapi.co/api/v2/type/{valgt_type}"
        type_response = requests.get(type_url)
        
        if type_response.status_code == 200:
            type_data = type_response.json()
            print(f"\nPokemon av typen {valgt_type}:")
            print(f"Det er {len(type_data['pokemon'])} Pokemon av typen {valgt_type}\n\
                  De første 10 er:")
            for pokemon in type_data['pokemon'][:10]:  # Viser bare de 10 første
                print(f"- {pokemon['pokemon']['name'].title()}") # .title() sørger for at første bokstav i navnet er stor
            print("... og flere!")
        else:
            print("Feil: Kunne ikke finne den typen")
    else:
        print("Feil: Kunne ikke hente typer")

# Kjør programmet
get_pokemon_by_type()