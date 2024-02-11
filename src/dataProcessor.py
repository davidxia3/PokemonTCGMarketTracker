import json
import os

directory = "data/raw/cards"

combined_cards = []

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(os.path.join(directory, filename), 'r') as file:
            data = json.load(file)
            combined_cards.extend(data)


with open('data/processed/combined_cards.json', 'w') as outfile:
    json.dump(combined_cards, outfile, indent=4)

