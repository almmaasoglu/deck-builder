# MTG Deck Builder Tool

## Overview
**Welcome to the MTG Deck Builder Tool** - a unique application for Magic: The Gathering enthusiasts! Leveraging the power of OpenAI's API, this tool is designed to suggest creative and niche decks based on player input. This Python-based application integrates with the `mtgsdk` library to fetch detailed card information, offering a comprehensive deck-building experience.

## Features
- **Custom Deck Recommendations**: Generate tailored deck recommendations based on user input.
- **Integration with OpenAI API**: Utilizes advanced AI algorithms for innovative and niche deck ideas.
- **Fetch Detailed Card Information**: Retrieves detailed information about each card in the suggested deck using `mtgsdk`.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3
- pip (Python package manager)

## Getting Started
To start using the MTG Deck Builder Tool, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/almmaasoglu/deck-builder.git

2. **Navigate to the Project Directory**:
   ```bash
   cd deck-builder

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Set Up OpenAI API Key**:
   Obtain an API key from OpenAI.
   Create a .env file in the project root.
   Add OPENAI_API_KEY=your_api_key_here to the .env file.

5. **Run the Application**:
   To run the application, execute the following command in the project directory:
   ```bash
   python deck_builder.py


## Usage
Describe your request for a Magic: The Gathering deck at the prompt. The application will generate a deck recommendation based on your input and fetch detailed information about each card.

## Contributing
Contributions to the MTG Deck Builder Tool are welcome! 

## License
This project is licensed under the MIT License - see the LICENSE file for details.
