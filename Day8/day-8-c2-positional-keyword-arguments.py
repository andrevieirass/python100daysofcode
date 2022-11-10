# Function with more than 1 input
# Positional Argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"You live in {location}")

greet_with("André", "Brazil")
greet_with("Brazil", "André")

print("\n##########\n")

# Keyword Argument
def greet_with(name="André", location="Brazil"):
    print(f"Hello {name}")
    print(f"You live in {location}")

greet_with()
greet_with("André", "Brazil")
greet_with(location="Brazil", name="André")
