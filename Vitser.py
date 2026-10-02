import json

with open("vitser.json", "r", encoding="utf-8") as fil:
    vitser = json.load(fil)

# Vis første vits
print("=== FØRSTE VITS ===")
print(vitser["1"])

# Vis alle vitser
print("\n=== ALLE VITSER ===")
for nummer in vitser:
    print(f"{nummer}: {vitser[nummer]}")
