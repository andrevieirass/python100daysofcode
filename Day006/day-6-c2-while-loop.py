# While Loops
# while something_is_true:
#   Do something
x = 1
y = 7

while x <= 10:
    print(f"{x} * {y} = {x * y}")

    x += 1

print("\n##########\n")

word = "Hello World!"
word_len = len(word)
char = 0

while char < word_len:
    print(word[char])

    char += 1

# Reeborg
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

num_of_hurdles = 6

while num_of_hurdles > 0:
    jump_hurdle()
    
    num_of_hurdles -=1
    
    print(num_of_hurdles)
"""
