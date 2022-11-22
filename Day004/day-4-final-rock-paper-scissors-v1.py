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

if player_choice == 0 and machine_choice == 2:
    print("You win")
elif player_choice == 1 and machine_choice == 0:
    print("You win")
elif player_choice == 2 and machine_choice == 1:
    print("You win")
elif player_choice == machine_choice:
    print("It's a draw")
else:
    print("You lose")

