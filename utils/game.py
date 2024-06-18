from typing import List

class Hangman:
    def __init__(self):
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: List[str] = list(self._choose_word())
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ['_' for _ in self.word_to_find]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def _choose_word(self) -> str:
        from random import choice
        return choice(self.possible_words)

    def play(self):
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            return
        if guess in self.correctly_guessed_letters or guess in self.wrongly_guessed_letters:
            print("You already guessed that letter.")
            return

        self.turn_count += 1
        if guess in self.word_to_find:
            for idx, letter in enumerate(self.word_to_find):
                if letter == guess:
                    self.correctly_guessed_letters[idx] = guess
            print("Good guess!")
        else:
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
            self.error_count += 1
            print("Wrong guess!")

    def start_game(self):
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            print("Word:", ' '.join(self.correctly_guessed_letters))
            print("Wrong guesses:", ', '.join(self.wrongly_guessed_letters))
            print(f"Lives: {self.lives}, Errors: {self.error_count}, Turns: {self.turn_count}")
            self.play()

        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

    def game_over(self):
        print("Game over...")

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
