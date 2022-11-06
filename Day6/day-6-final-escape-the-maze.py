# reeborg.ca
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Escape the Maze
## First try
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_right_and_move():
    turn_right()
    move()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif not wall_on_right() and wall_in_front():
        turn_right_and_move()
    elif not wall_on_right() and front_is_clear():
        turn_right_and_move()
    elif wall_on_right() and wall_in_front():
        turn_left()

## Challenge resolution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()