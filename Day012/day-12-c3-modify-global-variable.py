# Modifying Global Scope
enemies = 1

def increase_enemies():
    global enemies

    enemies += 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

print("\n##########\n")

enemies = 1

def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 2  # It doesn't modify the global scope

enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")
