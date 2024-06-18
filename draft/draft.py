
def get_word() -> str:
   
    return input("Chooser, please enter your word: ").strip().lower()

def get_lives() -> int:
   
    while True:
        try:
            lives = int(input("Chooser, please enter the number of lives: "))
            return lives
        except ValueError:
            print("Please enter a valid number.")

def get_guess(suggested_letters: list) -> str:
    
    while True:
        guess = input("Guesser, please enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in suggested_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def assess_guess(secret_word: str, guessed_letter: str, lives_left: int) -> int:
  
    if guessed_letter in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        lives_left -= 1
    return lives_left

def display_word(secret_word: str, suggested_letters: list) -> bool:
   
    displayed_word = ''.join([letter if letter in suggested_letters else '_' for letter in secret_word])
    print("Current word: ", ' '.join(displayed_word))
    return '_' not in displayed_word

def main():
    secret_word = get_word()
    lives = get_lives()
    suggested_letters = []
    while lives > 0:
        guess = get_guess(suggested_letters)
        suggested_letters.append(guess)
        lives = assess_guess(secret_word, guess, lives)
        if display_word(secret_word, suggested_letters):
            print("Congratulations! You've guessed the word!")
            break
    else:
        print("Game over! The word was:", secret_word)

if __name__ == "__main__":
    main()