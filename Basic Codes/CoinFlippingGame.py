import random

def flip_coin():
    return random.choice(["heads", "tails"])

if __name__ == "__main__":
    print("Coin Flipping Game")
    player_choice = input("Heads or Tails? ").lower()

    if player_choice not in ["heads", "tails"]:
        print("Invalid choice. Please choose heads or tails.")
    else:
        coin_result = flip_coin()
        print("Coin flipped:", coin_result)

        if player_choice == coin_result:
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, you guessed wrong.")
