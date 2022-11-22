# Dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary)

print("\n##########\n")

# Retrieving items from a dictionary
print(programming_dictionary["Bug"])
# print(programming_dictionary["Bugs"])  # KeyError: 'Bugs'

print("\n##########\n")

# Add an item to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

print("\n##########\n")

# Create an empty dictionary
empty_dictionary = {}

print(empty_dictionary)

print("\n##########\n")

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "New value for the Bug key."

print(programming_dictionary)

print("\n##########\n")

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
