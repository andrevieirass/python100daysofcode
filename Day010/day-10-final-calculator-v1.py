# Calculator
import os

from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("\nWhat's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("\nPick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calc = input(f"\nType 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' to end.: ").lower()

        if continue_calc == "y":
            num1 = answer
        elif continue_calc == "n":
            should_continue = False
            
            os.system("clear")
            calculator()
        elif continue_calc == 'e':
            should_continue = False

            print("Good bye!")
        else:
            print("Wrong option.")

calculator()
