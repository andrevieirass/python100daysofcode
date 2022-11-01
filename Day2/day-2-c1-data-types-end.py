## Type Error
num_char = len(input("What is your name? "))

# print("Your name has " + num_char + " characters.") # ERROR

## Type Checking

# print(type(num_char))

new_num_char = str((num_char))

print("Your name has " + new_num_char + " characters.")
print(type(new_num_char))

print("\n##########\n")

## Type Conversion
a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

print(70 + float("100.5"))
