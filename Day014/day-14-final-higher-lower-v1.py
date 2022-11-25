import os

from art import logo, vs
from game_data import data
from random import randint

def random_selection():
    random_selection = randint(0,49)

    return data[random_selection]

def compare_selection(a_selection, b_selection):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == "A":
        user_selection = a_selection["follower_count"]
        other_selection = b_selection["follower_count"]
    elif user_choice == "B":
        user_selection = b_selection["follower_count"]
        other_selection = a_selection["follower_count"]
    
    if user_selection > other_selection:
        return True
    elif user_selection < other_selection:
        return False

should_continue = True
score = 0
a_selection = random_selection()

while should_continue == True:
    print(logo)
    
    b_selection = random_selection()

    while a_selection == b_selection:
        b_selection = random_selection()

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(f'Compare A: {a_selection["name"]}, a {a_selection["description"]}, from {a_selection["country"]}.')
    print(vs)
    print(f'Compare B: {b_selection["name"]}, a {b_selection["description"]}, from {b_selection["country"]}.')

    compare = compare_selection(a_selection, b_selection)

    if compare == True:
        score += 1
        os.system("clear")
        a_selection = b_selection
    elif compare == False:
        should_continue = False
        os.system("clear")
        print(f"Sorry, that's wrong. Final score: {score}")
