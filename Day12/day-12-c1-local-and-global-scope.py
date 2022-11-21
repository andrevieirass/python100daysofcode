# Scope
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

print("\n##########\n")

# Local Scope
def drink_potion():
    potion_strength = 2  # Local scope
    print(potion_strength)

drink_potion()
# print(potion_strength)  # NameError: name 'potion_strength' is not defined

print("\n##########\n")

# Global Scope
player_health = 10  # Global scope

def drink_potion():
    potion_strength = 2  # Local scope
    print(player_health)

drink_potion()
print(player_health)
