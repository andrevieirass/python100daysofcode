print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

# Nested if and elif
if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))

    if age < 5:
        print("Please pay $3")
    elif age >= 5 and age <= 12:
        print("Please pay $5.")
    elif age >= 12 and age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")

else:
    print("Sorry, you have to grow taller before you can ride.")
