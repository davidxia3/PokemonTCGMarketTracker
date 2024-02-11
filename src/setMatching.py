import json

with open ("data/processed/combined_cards.json", "r") as file:
    data = json.load(file)

sets=[]
for card in data:
    set = str(card["id"]).split("-")[0]
    if set not in sets:
        sets.append(set)

set_matching = {}



set_matching["mcd11"] = "McDonald's Promos 2011"
set_matching["mcd12"] = "McDonald's Promos 2012"
set_matching["mcd14"] = "McDonald's Promos 2014"
set_matching["mcd15"] = "McDonald's Promos 2015"
set_matching["mcd16"] = "McDonald's Promos 2016"
set_matching["mcd17"] = "McDonald's Promos 2017"
set_matching["mcd18"] = "McDonald's Promos 2018"
set_matching["mcd19"] = "McDonald's Promos 2019"
set_matching["mcd21"] = "McDonald's 25th Anniversary Promos"
set_matching["mcd22"] = "McDonald's Promos 2022"

set_matching["ex1"] = "Ruby and Sapphire"
set_matching["ex2"] = "Sandstorm"
set_matching["ex3"] = "Dragon"
set_matching["ex4"] = "Team Magma vs Team Aqua"
set_matching["ex5"] = "Hidden Legends"
set_matching["ex6"] = "FireRed & LeafGreen"
set_matching["ex7"] = "Team Rocket Returns"
set_matching["ex8"] = "Deoxys"
set_matching["ex9"] = "Emerald"
set_matching["ex10"] = "Unseen Forces"
set_matching["ex11"] = "Delta Species"
set_matching["ex12"] = "Legend Maker"
set_matching["ex13"] = "Holon Phantoms"
set_matching["ex14"] = "Crystal Guardians"
set_matching["ex15"] = "Dragon Frontiers"
set_matching["ex16"] = "Power Keepers"

set_matching["pop1"] = "POP Series 1"
set_matching["pop2"] = "POP Series 2"
set_matching["pop3"] = "POP Series 3"
set_matching["pop4"] = "POP Series 4"
set_matching["pop5"] = "POP Series 5"
set_matching["pop6"] = "POP Series 6"
set_matching["pop7"] = "POP Series 7"
set_matching["pop8"] = "POP Series 8"
set_matching["pop9"] = "POP Series 9"

set_matching["neo1"] = "Neo Genesis"
set_matching["neo2"] = "Neo Discovery"
set_matching["neo3"] = "Neo Revelation"
set_matching["neo4"] = "Neo Destiny"

set_matching["tk1a"] = "EX Trainer Kit 1: Latias & Latios"
set_matching["tk2a"] = "EX Trainer Kit 1: Latias & Latios"
set_matching["tk1b"] = "EX Trainer Kit 2: Plusle & Minun"
set_matching["tk2b"] = "EX Trainer Kit 2: Plusle & Minun"

set_matching["ecard1"] = "Expedition"
set_matching["ecard2"] = "Aquapolis"
set_matching["ecard3"] = "Skyridge"

set_matching["col1"] = "Call of Legends"

set_matching["bp"] = "Best of Promos"

set_matching["hsp"] = "HGSS Promos"

set_matching["det1"] = "Detective Pikachu"

set_matching["si1"] = "Southern Islands"

set_matching["np"] = "Nintendo Promos"

set_matching["dc1"] = "Double Crisis"

set_matching["cel25"] = "Celebrations"

set_matching["cel25c"] = "Celebrations: Classic Collection"
set_matching["ru1"] = "Rumble"

set_matching["dv1"] = "Dragon Vault"

set_matching["fut20"] = "Miscellaneous Cards & Products"

set_matching["pgo"] = "Pokemon GO"

set_matching["g1"] = "Generations"

set_matching["sve"] = "SV01: Scarlet & Violet Base Set"
set_matching["svp"] = "SV: Scarlet & Violet Promo Cards"
set_matching["sv1"] = "SV01: Scarlet & Violet Base Set"
set_matching["sv2"] = "SV02: Paldea Evolved"
set_matching["sv3"] = "SV03: Obsidian Flames"
set_matching["sv3pt5"] = "SV: Scarlet & Violet 151"
set_matching["sv4"] = "SV04: Paradox Rift"
set_matching["sv4pt5"] = "SV: Paldean Fates"

set_matching["swshp"] = "SWSH: Sword & Shield Promo Cards"
set_matching["swsh1"] = "SWSH01: Sword & Shield Base Set"
set_matching["swsh2"] = "SWSH02: Rebel Clash"
set_matching["swsh3"] = "SWSH03: Darkness Ablaze"
set_matching["swsh4"] = "SWSH04: Vivid Voltage"
set_matching["swsh5"] = "SWSH05: Battle Styles"
set_matching["swsh6"] = "SWSH06: Chiilling Reign"
set_matching["swsh7"] = "SWSH07: Evolving Skies"
set_matching["swsh8"] = "SWSH08: Fusinon Strike"
set_matching["swsh9"] = "SWSH09: Brilliant Stars"
set_matching["swsh9tg"] = "SWSH09: Brilliant Stars Trainer Gallery"
set_matching["swsh10"] = "SWSH10: Astral Radiance"
set_matching["swsh10tg"] = "SWSH10: Astral Radiance Trainer Gallery"
set_matching["swsh11"] = "SWSH11: Lost Origin"
set_matching["swsh11tg"] = "SWSH11: Lost Origin Trainer Gallery"
set_matching["swsh12"] = "Silver Tempest"
set_matching["swsh12tg"] = "Silver Tempest Trainer Gallery"
set_matching["swsh12pt5"] = "Crown Zenith"
set_matching["swsh12pt5gg"] = "Crown Zenith: Galarian Gallery"
set_matching["swsh35"] = "Champion's Path"
set_matching["swsh45"] = "Shining Fates"
set_matching["swsh45sv"] = "Shining Fates: Shiny Vault"


set_matching["smp"] = "SM Promos"
set_matching["sm1"] = "SM Base Set"
set_matching["sm2"] = "SM - Guardians Rising"
set_matching["sm3"] = "SM - Burning Shadows"
set_matching["sm4"] = "SM - Crimson Invasion"
set_matching["sm5"] = "SM - Ultra Prism"
set_matching["sm6"] = "SM - Forbidden Light"
set_matching["sm7"] = "SM - Celestial Storm"
set_matching["sm8"] = "SM - Lost Thunder"
set_matching["sm9"] = "SM - Team Up"
set_matching["sm10"] = "SM - Unbroken Bonds"
set_matching["sm11"] = "SM - Unified Minds"
set_matching["sm12"] = "SM - Cosmic Eclipse"
set_matching["sm35"] = "Shining Legends"
set_matching["sm75"] = "Dragon Majesty"
set_matching["sm115"] = "Hidden Fates"
set_matching["sma"] = "Hidden Fates: Shiny Vault"

set_matching["xyp"] = "XY Promos"
set_matching["xy0"] = "Kalos Starter Set"
set_matching["xy1"] = "XY Base Set"
set_matching["xy2"] = "XY - Flashfire"
set_matching["xy3"] = "XY - Furious Fists"
set_matching["xy4"] = "XY - Phantom Forces"
set_matching["xy5"] = "XY - Primal Clash"
set_matching["xy6"] = "XY - Roaring Skies"
set_matching["xy7"] = "XY - Ancient Origins"
set_matching["xy8"] = "XY - BREAKthrough"
set_matching["xy9"] = "XY - BREAKpoint"
set_matching["xy10"] = "XY - Fates Collide"
set_matching["xy11"] = "XY - Steam Siege"
set_matching["xy12"] = "XY - Evolutions"

set_matching["bwp"] = "Black and White Promos"
set_matching["bw1"] = "Black and White"
set_matching["bw2"] = "Emerging Powers"
set_matching["bw3"] = "Noble Victories"
set_matching["bw4"] = "Next Destinies"
set_matching["bw5"] = "Dark Explorers"
set_matching["bw6"] = "Dragons Exalted"
set_matching["bw7"] = "Boundaries Crossed"
set_matching["bw8"] = "Plasma Storm"
set_matching["bw9"] = "Plasma Freeze"
set_matching["bw10"] = "Plasma Blast"
set_matching["bw11"] = "Legendary Treasures"

set_matching["dpp"] = "Diamond and Pearl Promos"
set_matching["dp1"] = "Diamond and Pearl"
set_matching["dp2"] = "Mysterious Treasures"
set_matching["dp3"] = "Secret Wonders"
set_matching["dp4"] = "Great Encounters"
set_matching["dp5"] = "Majestic Dawn"
set_matching["dp6"] = "Legends Awakened"
set_matching["dp7"] = "Stormfront"

set_matching["pl1"] = "Platinum"
set_matching["pl2"] = "Rising Rivals"
set_matching["pl3"] = "Supreme Victors"
set_matching["pl4"] = "Arceus"

set_matching["hgss1"] = "HeartGold SoulSilver"
set_matching["hgss2"] = "Unleashed"
set_matching["hgss3"] = "Undaunted"
set_matching["hgss4"] = "Triumphant"

set_matching["gym1"] = "Gym Heroes"
set_matching["gym2"] = "Gym Challenge"

set_matching["basep"] = "WoTC Promo"
set_matching["base1"] = "Base Set (Shadowless)"
set_matching["base2"] = "Jungle"
set_matching["base3"] = "Fossil"
set_matching["base4"] = "Base Set 2"
set_matching["base5"] = "Team Rocket"
set_matching["base6"] = "Legendary Collection"

with open("data/processed/set_dictionary.json","w") as outfile:
    json.dump(set_matching,outfile, indent=4)