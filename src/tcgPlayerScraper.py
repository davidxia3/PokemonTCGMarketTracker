from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import random
import re

options = Options()
options.headless = False

def get_card_name(input_string):
    card_name = input_string

    if not str(card_name).isascii():
        pattern = r'[^\x00-\x7F]'
        card_name = card_name.replace("\u00e9", "e")
        card_name = re.sub(pattern, '', card_name)
        card_name = card_name.strip()

    return card_name

master = []

# with open("data/processed/cards.json") as file:
#     cards = json.load(file)

with open("data/processed/set_dictionary.json") as file:
    set_dictionary = json.load(file)

output_dictionary = {}
for set_short in set_dictionary.keys():
    output_dictionary[set_short] = []

temp_dict = {}
temp_dict["ex14"] = set_dictionary["ex14"]


for set_short in temp_dict.keys():
    with open("data/processed/cardsBySet/" + set_short+".json") as file:
        cards = json.load(file)
    
    set_data = []

    for i in range(len(cards)):
        card=cards[i]
        try:
            driver = webdriver.Chrome(options=options)
            driver.get("https://shop.tcgplayer.com/pokemon")
            
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

            delay =random.uniform(1,3)
            time.sleep(delay)

            input_field = driver.find_element(By.ID, "ProductName")
            card_name = get_card_name(card["name"])
            try:
                int(card["number"])
            except:
                card_name = card_name + " (" + card["number"] + ")"

            input_field.send_keys(card_name)


            
            delay =random.uniform(1,3)
            time.sleep(delay)


            dropdown = Select(driver.find_element(By.ID, "SetName"))
            dropdown.select_by_visible_text(card["set"])

            search = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Search']")

            delay =random.uniform(1,3)
            time.sleep(delay)

            search.click()
            WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

            search_results = driver.find_elements(By.XPATH, "//div[@class='search-result']")

            found = False
            link = ""
            for search_result in search_results:
                try:
                    rarity = search_result.find_element(By.CLASS_NAME, "search-result__rarity").text
                    rarity = rarity.split("#")[1].split("/")[0].lstrip("0")
                    if rarity == card["number"]:
                        found = True
                        link = search_result.find_element(By.CLASS_NAME, "search-result__content").find_element(By.TAG_NAME, "a").get_attribute("href")
                        break
                except:
                    pass

            tcg_id = -1

            data = {
                "base": [-1, []],
                "holo": [-1, []],
                "reverse": [-1,[]]}  
            
            delay =random.uniform(1,3)
            time.sleep(delay)


            if found:
                driver.get(link)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "charts-item")))

                tcg_id = link.split("product/")[1].split("/")[0]

                delay =random.uniform(1,3)
                time.sleep(delay)


                time_buttons = driver.find_elements(By.CLASS_NAME, "charts-item")
                for button in time_buttons:
                    if button.text == "1Y":
                        button.click()
                        break
                time.sleep(0.5)
                
            
                table = driver.find_element(By.XPATH, "//table[@role='region' and @aria-live='polite']")
                header = table.find_element(By.TAG_NAME, "thead")
                header_rows = header.find_elements(By.TAG_NAME, "th")
                for i in range(1, len(header_rows)):
                    label = driver.execute_script("return arguments[0].textContent;", header_rows[i])
                    if label == "Normal":
                        data["base"][0] = i
                    elif label == "Holofoil":
                        data["holo"][0] = i
                    elif label == "Reverse Holofoil":
                        data["reverse"][0] = i
                body = table.find_element(By.TAG_NAME, "tbody")
                rows = body.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    row_data = row.find_elements(By.TAG_NAME, "td")
                    if data["base"][0] != -1:
                        value = driver.execute_script("return arguments[0].textContent;", row_data[data["base"][0]]).lstrip("$").replace(",","")
                        if value == "NaN":
                            data["base"][1].append(0.00)
                        else:
                            data["base"][1].append(float(value))
                    if data["holo"][0] != -1:
                        value = driver.execute_script("return arguments[0].textContent;", row_data[data["holo"][0]]).lstrip("$").replace(",","")
                        if value == "NaN":
                            data["holo"][1].append(0.00)
                        else:
                            data["holo"][1].append(float(value))
                    if data["reverse"][0] != -1:
                        value = driver.execute_script("return arguments[0].textContent;", row_data[data["reverse"][0]]).lstrip("$").replace(",","")
                        if value == "NaN":
                            data["reverse"][1].append(0.00)
                        else:
                            data["reverse"][1].append(float(value))
            else:
                print("UNFOUND")
                print(card["id"])
                print("")
            
            
            card["tcg"] = tcg_id
            card["base"] = data["base"][1]
            card["holo"] = data["holo"][1]
            card["reverse"] = data["reverse"][1]

            delay =random.uniform(1,3)
            time.sleep(delay)
            
            set_data.append(card)
            master.append(card)

            with open("data/processed/cardsWithPricesBySet/" + set_short + ".json", "w") as outfile:
                json.dump(set_data, outfile, indent=4)

        except Exception as e:
            print("EXCEPT")
            print(card["id"])
            print(e)
            print("")
        
            break


with open("data/processed/cardsWithPrices.json","w") as outfile:
    json.dump(master, outfile, indent=4)