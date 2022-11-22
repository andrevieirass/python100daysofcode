# reboorg.ca
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def walk():
    while wall_on_right() and not wall_in_front():
  # while wall_on_right() and front_is_clear():
        move()

def jump_hurdle():
    turn_left()
    walk()
    turn_right()
    move()
    turn_right()
    move()
    walk()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_hurdle()

# OR #

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    turn_left()
    
    while wall_on_right():
        move()
    
    turn_right()
    move()
    turn_right()
    
    while not wall_in_front():
        move()
    
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_hurdle()