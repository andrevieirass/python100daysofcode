"""
# INSTRUCTIONS #

You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 23 splits the string names_string into individual names and puts them inside a List called names.
For this to work, you must enter all the names as names followed by comma then space.

e.g. name, name, name

Example Input
Angela, Ben, Jenny, Michael, Chloe

Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
"""
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# Way to understand list and random modules
num_items = len(names)
random_position = random.randint(0, num_items - 1)
random_name = names[random_position]

# Easier way
# random_name = random.choice(names)

print(f"{random_name} is going to buy the meal today!")
