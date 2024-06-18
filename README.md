### Hangman Game

** Project Overview**

Welcome to the Hangman game! This Python implementation allows you to play the classic word-guessing game. You can choose a word, set the number of lives, and guess letters until you either guess the word correctly or run out of lives.

**Features**

- **Choose a secret word.
- **Set the number of lives.
- **Guess letters to reveal the word.
- **Track the number of incorrect guesses and turns.

**File Structure**

- main.py: Main script to execute the game.
- utils/game.py: Contains the Hangman class, which encapsulates the main game logic.
- utils/input_utils.py: Defines functions to handle user input, such as getting the secret word, lives, and guesses from the players.

This Hangman game implementation allows for an interactive word-guessing experience, enhancing user engagement through a well-structured and modular codebase.

## How to Run

1. Clone the Repository:

    ```bash
    git clone https://github.com/RachaelShenRq/hangman-game.git
    cd hangman-game
    ```

2.  Install Dependencies:

   Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

3. Run the Game:

   Execute the game by running the following command:

   ```bash
   python main.py
   ```

4. Game Flow:

    The Chooser enters a word and the number of lives.
    The Guesser starts guessing letters.
    The game continues until the word is guessed correctly or lives run out.

License
    @Shen Rongqing   