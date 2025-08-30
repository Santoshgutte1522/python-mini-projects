import random

def roll_dice():
    while True:
        print("You rolled:", random.randint(1, 6))
        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            break

roll_dice()
