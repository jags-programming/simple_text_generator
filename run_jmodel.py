# file: run_jmodel.py
# Description: This script loads a Wikipedia text file, trains a Markov Chain model using the text, 
#              and generates new text based on a given prompt.

from JModel import SimpleTextGenerator  # Import the Markov Chain class
import os  # For file handling

def load_text_from_file(title, folder="data"):
    """
    Loads text from a saved Wikipedia file.

    Args:
        title (str): The Wikipedia page title (used for filename).
        folder (str): The directory where the text file is stored (default: "data").

    Returns:
        str or None: The content of the file as a string if found, otherwise None.
    """
    
    # Generate the filename based on the title (spaces replaced with underscores)
    filename = title.replace(" ", "_") + ".txt"
    filepath = os.path.join(folder, filename)

    # Check if the file exists before attempting to read
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found. Please fetch the Wikipedia text first.")
        return None

    # Read the file and return its contents
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

# Specify the Wikipedia page title to load text from
title = "A. P. J. Abdul Kalam"

# Load the previously saved Wikipedia text
text = load_text_from_file(title)

# Proceed only if text was successfully loaded
if text:
    # Initialize the Markov Chain model
    model = SimpleTextGenerator()

    # Train the model using the loaded text
    model.train(text)
    
    # Define a sample prompt to generate new text
    prompt = "Dr. A. P. J. Abdul Kalam"

    # Generate text using the trained model
    result = model.generate(prompt)
    
    # Print the generated text output
    print("Generated Text:", result)
