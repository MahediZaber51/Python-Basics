import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    print("Dice Rolling Game")
    input("Press Enter to roll the dice...")

    roll_result = roll_dice()
    print("You rolled:", roll_result)
