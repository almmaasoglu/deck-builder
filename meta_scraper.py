from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_meta_decks():
    options = Options()
    options.headless = True  # Running in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://mtgarena.pro/meta/'
    driver.get(url)
    time.sleep(10)  # Adjust time as needed to ensure the page loads completely

    meta_decks = []
    # Note: Update the selectors below based on the actual structure of the webpage
    deck_containers = driver.find_elements(By.CLASS_NAME, 'sc-eYWfdp lmVEMn')  # Update the class name
    for deck_container in deck_containers[:5]:  # Limit to top 5 decks
        deck_name = deck_container.find_element(By.CLASS_NAME, 'sc-enTruF fvHdPl').text.strip()  # Update the class name

        cards = []
        card_elements = deck_container.find_elements(By.CLASS_NAME, 'sc-fbNZEX gzbppH')  # Update the class name
        for card_element in card_elements:
            card_name = card_element.text.strip()
            cards.append(card_name)

        deck_info = {
            'name': deck_name,
            'cards': cards
        }
        meta_decks.append(deck_info)

    driver.quit()

    # Write scraped data to a text file
    with open('scraped_meta_decks.txt', 'w') as file:
        for deck in meta_decks:
            file.write(f"Deck Name: {deck['name']}\n")
            file.write("Cards:\n")
            file.write('\n'.join(deck['cards']))
            file.write("\n\n")

    return meta_decks










