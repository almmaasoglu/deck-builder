import os

from dotenv import load_dotenv
from openai import OpenAI
from mtgsdk import Card
from meta_scraper import scrape_meta_decks

# Load environment variables from .env file
load_dotenv()

# Check if OPENAI_API_KEY is set
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

# Instantiate the OpenAI client with your API key
client = OpenAI(api_key=openai_api_key)

def get_deck_recommendation(description, meta_decks):
    try:
        # Constructing a string that includes both deck names and their card names
        deck_info_strings = []
        for deck in meta_decks:
            deck_info = f"{deck['name']} (Cards: {', '.join(deck['cards'])})"
            deck_info_strings.append(deck_info)

        meta_info = '; '.join(deck_info_strings)
        meta_prompt = f"Considering the current meta decks: {meta_info}, {description}"
        
        completion = client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an assistant knowledgeable about Magic: The Gathering. "
                            "Suggest unique and niche decks based on player's choice of format. "
                            "Make sure to be very thoughtful with card choices and additions. "
                            "Decks that should be rare so it's not often played. "
                            "Decreasing the counter potential of the cards. "
                            "Make sure to take the current meta into account. "
                        )
                    },
                    {"role": "user", "content": meta_prompt}
            ]
        )            
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_card_names(recommendation):
    # Placeholder function, needs to be adapted to the format of recommendations
    return [name.strip() for name in recommendation.split('-')[1:]]

def fetch_cards_from_mtg_api(card_names):
    detailed_cards = []
    for name in card_names:
        fetched_cards = Card.where(name=name).where(language='English').all()
        for card in fetched_cards:
            card_details = {
                'name': card.name,
                'mana_cost': card.mana_cost,
                'type': card.type,
                'rarity': card.rarity,
                'text': card.text,
            }
            detailed_cards.append(card_details)
    return detailed_cards

def main():
    meta_decks = scrape_meta_decks()
    user_input = input("Describe your request for a Magic: The Gathering deck: ")
    deck_recommendation = get_deck_recommendation(user_input, meta_decks)
    
    if deck_recommendation:
        print("\nDeck Recommendation:")
        print(deck_recommendation)

        card_names = extract_card_names(deck_recommendation)
        detailed_cards = fetch_cards_from_mtg_api(card_names)

        if detailed_cards:
            print("\nDetailed Card Information:")
            for card in detailed_cards:
                print(f"Name: {card['name']}, Mana Cost: {card['mana_cost']}, Type: {card['type']}, Rarity: {card['rarity']}, Text: {card['text']}")
        else:
            print("No detailed card information found.")
    else:
        print("Unable to generate deck recommendation.")

if __name__ == "__main__":
    main()
