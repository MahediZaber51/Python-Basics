import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    return displayed

if __name__ == "__main__":
    print("Hangman Game")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nWord:", display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            guessed_letters.append(guess)
            print("Incorrect guess.")
            attempts -= 1
        
        if "_" not in display_word(secret_word, guessed_letters):
            print(f"Congratulations! You guessed the word '{secret_word}'!")
            break
        
        if attempts == 0:
            print(f"Sorry, you're out of attempts. The word was '{secret_word}'.")
            break

    print("Game Over.")
