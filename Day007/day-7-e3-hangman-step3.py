# Step 3
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f"The chosen word is: {chosen_word}")

display = []

# Create blanks
for letter in chosen_word:
# for letter in range(word_length):
    display.append("_")
    # display += "_"

# TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True

        print("You win!!!")
