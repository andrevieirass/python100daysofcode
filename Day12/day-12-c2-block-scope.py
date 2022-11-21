# Block Scope
# It doesn't exist in Python
game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]  # Global scope

print(new_enemy)

print("\n##########\n")

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    
    if game_level < 5:
        new_enemy = enemies[0]  # Local scope

    print(new_enemy)

create_enemy()
