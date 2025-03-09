# file: JModel.py
# Description: This script contains a class that implements a Markov Chain text generator.

import random
import string
from collections import defaultdict
from typing import List, Dict


class SimpleTextGenerator :
    """
    A simple Markov Chain model for text generation.
    This model learns word sequences from input text and generates text 
    based on observed transitions.
    """

    def __init__(self) -> None:
        """
        Initializes the Markov Chain model.

        Attributes:
        - `self.graph` (Dict[str, List[str]]): A dictionary where keys are words and values 
          are lists of possible next words.
        """
        self.graph: Dict[str, List[str]] = defaultdict(list)

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenizes input text into a list of words.

        - Removes punctuation and numbers.
        - Splits the text into words based on spaces.
        - Filters out empty tokens.

        Args:
        - text (str): Input text to be tokenized.

        Returns:
        - List[str]: A list of words (tokens).
        """
        text = text.translate(str.maketrans("", "", string.punctuation + "1234567890"))
        tokens = text.replace("\n", " ").split()

        return [t for t in tokens if t]  # Remove empty strings

    def train(self, text: str) -> None:
        """
        Trains the Markov Chain model using input text.

        - Creates a transition graph where each word points to possible next words.

        Args:
        - text (str): Input text to train the model.
        """
        tokens = self.tokenize(text)

        # Build the transition graph
        for i in range(len(tokens) - 1):
            self.graph[tokens[i]].append(tokens[i + 1])

    def generate(self, prompt: str, length: int = 10) -> str:
        """
        Generates text starting from a given prompt.

        - Uses trained word transitions to produce new text.

        Args:
        - prompt (str): Starting text for generation.
        - length (int): Number of words to generate (default: 10).

        Returns:
        - str: Generated text.
        """
        tokens = self.tokenize(prompt)

        if not tokens:
            return "Invalid prompt."  # Handle case where prompt is empty after tokenization

        current_word = tokens[-1] if tokens[-1] in self.graph else random.choice(list(self.graph.keys()))
        output_words = [prompt]  # Initialize with the given prompt

        for _ in range(length):
            next_words = self.graph.get(current_word, [])
            if not next_words:
                break  # Stop if no transitions exist
            current_word = random.choice(next_words)
            output_words.append(current_word)

        return " ".join(output_words)  # Use join for efficiency
