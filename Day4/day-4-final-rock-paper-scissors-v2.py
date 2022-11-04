"""
# INSTRUCTIONS #

Build a Rock, Paper, Scissors game to play against the machine.
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
machine_choice = random.randint(0, 2)

if player_choice < 0 or player_choice > 2:
    print("Sorry, invalid option!\nTry again.")
else:
    print(game_images[player_choice])
    print(f"Machine chose:\n{game_images[machine_choice]}")

choices = [
    ["It's a draw", "You lose", "You win"],
    ["You win", "It's a draw", "You lose"],
    ["You lose", "You win", "It's a draw"]
]

print(choices[player_choice][machine_choice])
