import os

from art import logo, vs
from game_data import data
from random import choice

def get_random_account():
    """
    Get a random account from data.
    """
    return choice(data)

def format_data(account):
    """
    Format account into printable format:
        name
        description
        country
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    count = account["follower_count"]

    # return f"{name}, a {description}, from {country}"
    return f"{name}, a {description}, from {country} - {count}"

def check_answer(guess, a_followers, b_followers):
    """
    Checks followers against user's guess and returns True if they got 
    it right. Or False if they got it wrong.
    """
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

def game_higher_lower():
    print(logo)
    
    score = 0
    should_continue = True
    account_b = get_random_account()

    while should_continue:        
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        account_a_follower_count = account_a["follower_count"]
        account_b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, account_a_follower_count, account_b_follower_count)

        os.system("clear")
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

while input("Do you want to play the Higher or Lower game? Type 'Y' or 'N': ").upper() == "Y":
    os.system("clear")
    game_higher_lower()
print("Godd Bye!")