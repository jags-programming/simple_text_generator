Simple Text Generator

This repository contains a simple text generator based on a Markov Chain model. The model learns word sequences from input text and generates new text based on observed transitions.

Features

Tokenizes input text and removes punctuation.

Builds a transition graph for word sequences.

Generates text using a trained Markov Chain model.

Files

JModel.py - Contains the SimpleTextGenerator class for training and generating text.

run_jmodel.py - Loads text from a file, trains the model, and generates text.

wiki_getbio.py - (Optional) Fetches Wikipedia text for training.

Setup

Prerequisites

Python 3.7+

git installed and configured

Installation

Clone the repository:

git clone https://github.com/jags-programming/simple_text_generator.git

Navigate to the project directory:

cd simple_text_generator

(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies (if any are required in the future):

pip install -r requirements.txt

Usage

Train the model with text:

python run_jmodel.py

Modify prompt in run_jmodel.py to experiment with different starting words.

Contributing

Feel free to fork the repository and submit pull requests!

License

MIT License. See LICENSE for details.

