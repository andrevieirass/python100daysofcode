"""
# INSTRUCTIONS #
Make your own "Choose Your Own Adventure" game.
Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

To write your code according to my story, you can use this flow chart from draw.io to help you.

However, I think the fun part is writing your own story.
"""
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input("You're at a crossroad. Where do you want to go? Type 'right' or 'left'\n ").lower()
if choice1 == "right":
    choice2 = input("You see a lake with an island on it, you can get there swimming or use something as a boat. How do you want to go? Type 'swim' or 'boat'\n ").lower()
    if choice2 == "boat":
        print("""
            __________   __________   __________
           |   BLUE   | |    RED   | |  YELLOW  |
           |  __  __  | |  __  __  | |  __  __  |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |__||__| | | |__||__| | | |__||__| |
           |  __  __()| |  __  __()| |  __  __()|
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |__||__| | | |__||__| | | |__||__| |
           |__________| |__________| |__________|
        """)

        choice3 = input("You get on the island and find a house with three doors, blue, red and yellow. Which one do you choose?\n ").lower()
        if choice3 == "blue":
            print("The room is empty.\nGAME OVER")
            print("""
                0================================================0
                |'.                                            .'|
                |  '.                                        .'  |
                |    '.                                    .'    |
                |      '. ______________________________ .'      |
                |        :                              :     .. |
                |        :                              :   .'|| |
                |        :                              :  |  || |
                |        :                              :  I  || |
                |        :           GAME OVER          :  |  || |
                |        :                              :  |  || |
                |        :                              :  |  || |
                |        :                              :  | 0+| |
                |        :                              :  |  || |
                |        :______________________________:  I  || |
                |      .'                                '.|  || |
                |    .'                                    '. || |
                |  .'                                        '|| |
                |.'                                            '.|
                0================================================0
            """)
        elif choice3 == "red":
            print("The room is on fire.\nGAME OVER")
            print("""
                            (  .      )
                        )           (              )
                              .  '   .   '  .  '  .
                     (    , )       (.   )  (   ',    )
                    .' ) ( . )   GAME OVER ,  . )   ( .
                   ). , ( .   (  ) ( , ')  .' (  ,    )
                  (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            """)
        elif choice3 == "yellow":
            choice4 = input("You find a golden chest. Do you to open it? Type 'yes' or 'no'\n ").lower()
            if choice4 == "yes":
                print("You are too curious. If you open the chest inside the room, it takes you to another dimension.\nGAME OVER")
            else:
                print("WINNER!!!\nYou can take the chest home.")
                print('''
                    *******************************************************************************
                              |                   |                  |                     |
                     _________|________________.=""_;=.______________|_____________________|_______
                    |                   |  ,-"_,=""     `"=.|                  |
                    |___________________|__"=._o`"-._        `"=.______________|___________________
                              |                `"=._o`"=._      _`"=._                     |
                     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                    /______/______/______/______/______/______/______/______/______/______/_____ /
                    *******************************************************************************
                ''')
        else:
            print("You didn't choose one of three doors.\nGAME OVER")
    else:
        print("You're attacked by an crocodile.\nGAME OVER")
        print("""
                           _.---._     .---.
                  __...---' .---. `---'-.   `.
              .-''__.--' _.'( | )`.  `.  `._ :
            .'__-'_ .--'' ._`---'_.-.  `.   `-`.
                   ~ -._ -._``---. -.    `-._   `.
                        ~ -.._ _ _ _ ..-_ `.  `-._``--.._
                                     -~ -._  `-.  -. `-._``--.._.--''.
                                          ~ ~-.__     -._  `-.__   `. `.
                                      GAME OVER ~~ ~---...__ _    ._ .` `.
                                                            ~  ~--.....--~`
        """)
else:
    print("You get lost on the woods.\nGAME OVER")
    print("""
        ^  ^  ^   ^  ^  ^   ^  ^  ^   ^  ^
       /|\/|\/|\ /|\/|\/|\ /|\/|\/|\ /|\/|\\
       /|\/|\/|\ /|\/|\GAME OVER\/|\ /|\/|\\
       /|\/|\/|\ /|\/|\/|\ /|\/|\/|\ /|\/|\\
       /|\/|\/|\ /|\/|\/|\ /|\/|\/|\ /|\/|\\
    ------------------------------------------
    """)
