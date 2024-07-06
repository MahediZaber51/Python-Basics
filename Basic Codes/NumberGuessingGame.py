import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        user_guess = int(input("Take a guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low!")
        elif user_guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
