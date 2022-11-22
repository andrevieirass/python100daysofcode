# Guessing the Number
import os

from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(random_number, guess, attempts):
    """
    Checks answer against guess.
    Returns the number of turns remaining.
    """
    if guess < 1 or guess > 100:
        print("Number out of range.")
        return attempts
    elif guess > random_number:
        print("Lower.")
        return attempts - 1
    elif guess < random_number:
        print("Higher.")
        return attempts - 1
    else:
        print(f"\nYou got it! The number is {random_number}!!!")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS

def play_guess_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = randint(1, 100)
    attempts = set_difficulty()
    guess = 0

    while guess != random_number:
        print(f"\nYou have {attempts} remaining to guess the number.")

        guess = int(input("Make a guess: "))
        attempts = check_answer(random_number, guess, attempts)

        if attempts == 0:
            print("\nYou've run out of guesses, you lose.")
            return
        elif guess != random_number:
            print("Guess again.")

while input("Do you want to play the Guessing the Number? Type 'y' or 'n': ") == "y":
  os.system("clear")
  play_guess_number()
