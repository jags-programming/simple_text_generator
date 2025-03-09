# file: wiki_getbio.py
# Description: This script fetches the text of a Wikipedia page and saves it to a text file.

import wikipediaapi  # Wikipedia API for fetching page content
import os  # For file handling

def get_wikipedia_text(title, lang="en"):
    """
    Fetches the text content of a Wikipedia page.
    
    Args:
        title (str): The title of the Wikipedia page to fetch.
        lang (str): The language of the Wikipedia page (default is English: "en").
    
    Returns:
        str or None: The cleaned text content of the page if it exists, otherwise None.
    """
    
    # Define user-agent to comply with Wikipedia API policies (update contact info)
    user_agent = "MyWikiFetcherBot/1.0 (contact: myemail@mydomain.com)"  # ✅ Update this

    # Initialize Wikipedia API with the specified language and user-agent
    wiki = wikipediaapi.Wikipedia(
        language=lang, 
        user_agent=user_agent
    )

    # Fetch the page based on the provided title
    page = wiki.page(title)

    # Check if the page exists
    if not page.exists():
        print(f"Error: The Wikipedia page '{title}' does not exist.")
        return None

    # Extract the text content of the page
    raw_text = page.text

    # Clean up text by removing extra spaces and newlines
    cleaned_text = " ".join(raw_text.split())

    return cleaned_text

def save_text_to_file(title, text, folder="data"):
    """
    Saves the fetched Wikipedia text to a file.

    Args:
        title (str): The title of the Wikipedia page (used for filename).
        text (str): The cleaned Wikipedia page content.
        folder (str): The directory where the file will be saved (default: "data").
    """
    
    # Ensure the folder exists; create it if it doesn’t
    os.makedirs(folder, exist_ok=True)

    # Generate a valid filename from the page title
    filename = title.replace(" ", "_") + ".txt"
    filepath = os.path.join(folder, filename)

    # Write the text content to the file with UTF-8 encoding
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"✅ Wikipedia text saved to {filepath}")

# Example Usage:
if __name__ == "__main__":
    title = "A. P. J. Abdul Kalam"  # Specify the Wikipedia page title
    biography_text = get_wikipedia_text(title)

    # Save text if the page exists
    if biography_text:
        save_text_to_file(title, biography_text)
