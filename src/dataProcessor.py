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

output_dictionary = {}

for set_short in sets.keys():
    output_dictionary[set_short] = []


for card in combined_cards:
    card_id = card["id"]
    set = str(card_id).split("-")[0]
    card["set"] = sets[set]
    output_dictionary[set].append(card)


with open('data/processed/cards.json', 'w') as outfile:
    json.dump(combined_cards, outfile, indent=4)

for set_short, set_data in output_dictionary.items():
    with open("data/processed/cardsBySet/"+set_short+".json","w") as outfile:
        json.dump(set_data, outfile, indent = 4)