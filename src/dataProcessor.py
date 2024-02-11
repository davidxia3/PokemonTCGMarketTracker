import json
import os

directory = "data/raw/cards"

combined_cards = []

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(os.path.join(directory, filename), 'r') as file:
            data = json.load(file)
            combined_cards.extend(data)

with open("data/processed/set_dictionary.json", "r") as file:
    sets = json.load(file)

for card in combined_cards:
    card_id = card["id"]
    set = str(card_id).split("-")[0]
    card["set"] = sets[set]


with open('data/processed/cards.json', 'w') as outfile:
    json.dump(combined_cards, outfile, indent=4)

