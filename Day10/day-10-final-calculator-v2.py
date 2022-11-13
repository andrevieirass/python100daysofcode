# Calculator
import os

from art import logo

# Calculation
def calculation(n1, n2, symbol):
    if symbol == "+":
        return n1 + n2
    elif symbol == "-":
        return n1 - n2
    elif symbol == "*":
        return n1 * n2
    elif symbol == "/":
        return n1 / n2
    else:
        print("You entered an invalid symbol")

operations = ["+", "-", "*", "/"]

def calculator():
    print(logo)

    num1 = float(input("\nWhat's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("\nPick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = calculation(num1, num2, operation_symbol)

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
