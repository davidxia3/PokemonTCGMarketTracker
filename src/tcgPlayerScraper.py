from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

options = Options()
options.headless = False


with open("data/processed/cards.json") as file:
    cards = json.load(file)

unfound = []

for i in range(20):
    card=cards[i]
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://shop.tcgplayer.com/pokemon")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))


        input_field = driver.find_element(By.ID, "ProductName")

        input_field.send_keys(card["name"])


        dropdown = Select(driver.find_element(By.ID, "SetName"))
        dropdown.select_by_visible_text(card["set"])

        search = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Search']")

        search.click()
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        search_results = driver.find_elements(By.XPATH, "//div[@class='search-result']")

        found = False
        link = ""
        for search_result in search_results:
            try:
                rarity = search_result.find_element(By.CLASS_NAME, "search-result__rarity").text
                rarity = int(rarity.split("#")[1].split("/")[0])
                if rarity == int(card["number"]):
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


        if found:
            driver.get(link)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "charts-item")))

            tcg_id = link.split("product/")[1].split("/")[0]

            time_buttons = driver.find_elements(By.CLASS_NAME, "charts-item")
            for button in time_buttons:
                if button.text == "1Y":
                    button.click()
                    break
            time.sleep(0.5)
            
            try:
                driver.find_element(By.CLASS_NAME, "error-data")
                unfound.append(i)
            except:
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
                dates = []
                for row in rows:
                    row_data = row.find_elements(By.TAG_NAME, "td")
                    dates.append(driver.execute_script("return arguments[0].textContent;", row_data[0]).lstrip("$"))
                    if data["base"][0] != -1:
                        (data["base"][1]).append(float(driver.execute_script("return arguments[0].textContent;", row_data[data["base"][0]]).lstrip("$")))
                    if data["holo"][0] != -1:
                        (data["holo"][1]).append(float(driver.execute_script("return arguments[0].textContent;", row_data[data["holo"][0]]).lstrip("$")))
                    if data["reverse"][0] != -1:
                        (data["reverse"][1]).append(float(driver.execute_script("return arguments[0].textContent;", row_data[data["reverse"][0]]).lstrip("$")))
        card["tcg"] = tcg_id
        card["dates"] = dates
        card["base"] = data["base"][1]
        card["holo"] = data["holo"][1]
        card["reverse"] = data["reverse"][1]
    except:
        break

print(unfound)

with open("data/processed/cardsWithPrices.json","w") as outfile:
    json.dump(cards, outfile, indent=4)


