import requests

url = "https://pokeapi.co/api/v2/evolution-chain/1/"
response = requests.get(url)

data = response.json()

print(data["chain"]["species"]["name"])
print(data["chain"]["evolves_to"][0]["species"]["name"])
print(data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"])

# Get additional details about the first Pokemon
pokemon_name = "charizard"#data["chain"]["species"]["name"]
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
pokemon_response = requests.get(pokemon_url)
pokemon_data = pokemon_response.json()

print(f"\nDetails about {pokemon_name.title()}:")
print(f"Height: {pokemon_data['height']/10} meters")
print(f"Weight: {pokemon_data['weight']/10} kg")
print("Types:", ", ".join([t['type']['name'] for t in pokemon_data['types']]))


