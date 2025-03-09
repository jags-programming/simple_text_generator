# Simple Text Generator

This repository contains a simple text generator based on a Markov Chain model. The model learns word sequences from input text and generates new text based on observed transitions.

## Features
- Tokenizes input text and removes punctuation.
- Builds a transition graph for word sequences.
- Generates text using a trained Markov Chain model.

## Files
- `JModel.py` - Contains the `SimpleTextGenerator` class for training and generating text.
- `run_jmodel.py` - Loads text from a file, trains the model, and generates text.
- `wiki_getbio.py` - (Optional) Fetches Wikipedia text for training.

## Setup
### Prerequisites
- Python 3.7+
- `git` installed and configured

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/jags-programming/simple_text_generator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd simple_text_generator
   ```
3. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies (if any are required in the future):
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Train the model with text:
   ```sh
   python run_jmodel.py
   ```
2. Modify `prompt` in `run_jmodel.py` to experiment with different starting words.

## Contributing
Feel free to fork the repository and submit pull requests!

## License
MIT License. See `LICENSE` for details.

