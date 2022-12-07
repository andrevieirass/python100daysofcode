from data import MENU, resources


def report():
    """
    Returns the current amount of resources and money in the machine.
    """
    global money

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {money}$")


def check_resources(order_ingredients):
    """
    Returns True when order can be made, or False if ingredients are
    insufficient.
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


def process_coins():
    """
    Returns the total calculated from coins inserted.
    """
    print("Please insert coins.")

    total = 0.25 * int(input("How many quarters?: "))
    total += 0.1 * int(input("How many dimes?: "))
    total += 0.05 * int(input("How many nickles?: "))
    total += 0.01 * int(input("How many pennies?: "))

    return total


def check_transaction(money_received, drink_cost):
    """
    Returns True when the payment is accepted, or False if money is
    insufficient.
    """
    if money_received >= drink_cost:
        global money
        change = round(money_received - drink_cost, 2)
        money += drink_cost

        print(f"Here is ${change} in change.")

        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients from the resources.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕️!")


machine_status = True
money = 0

while machine_status:
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if choice == "off":
        print("Turning off the coffee machine.")
        machine_status = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]

        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
