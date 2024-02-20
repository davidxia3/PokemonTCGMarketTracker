import json
import re
from unicodedata import normalize

def remove_unicode(input_string):
    # Match any character that is not in the ASCII range
    pattern = r'[^\x00-\x7F]'
    return re.sub(pattern, '', input_string)


with open("data/processed/cards.json", "r") as file:
    cards = json.load(file)

for card in cards:
    
    if not card["name"].isascii():
        print(card["name"])
        card_name = card["name"]
        card_name = card_name.replace("\u00e9", "e")

        card_name = remove_unicode(card_name)

        card_name = card_name.strip()
        print(card_name)

test = "Rayquaza \u2605"

print(test.isascii())