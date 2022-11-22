# Module
import random
import modules.pi as pi  # ../modules/pi.py

# Print random integer numbers
random_integer = random.randint(1, 10)

print(random_integer)

# Print random float numbers, default (0, 1)
random_float = random.random()

print(random_float)

# Print random float numbers, default (0, 1)
random_float = random.random() * 5

print(random_float)

# Different way
random_float = random.uniform(1, 5)

print(random_float)

print("\n##########\n")

# Using the created module pi
print(pi.pi)
