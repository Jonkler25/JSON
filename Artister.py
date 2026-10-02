import json

with open("Artister.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

print("=== EN ARTIST ===")
artist = data["Artister"][0]
print(f"Navn: {artist['navn']}")
print(f"Sjanger: {artist['sjanger']}")
print(f"Album: {artist['Album'][0]}")
print(f"Debut: {artist['Debut']}")

print("\n=== ALLE ARTISTER ===")
for artist in data["Artister"]:
    print(f"- {artist['navn']}")

print("\n=== OPPLYSNING ===")
print(f"{data['Artister'][0]['navn']} debuterte i {data['Artister'][0]['Debut']}")
