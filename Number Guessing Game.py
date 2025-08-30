
import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it in " + str(attempts) + " attempts.")
            break

number_guessing_game()
