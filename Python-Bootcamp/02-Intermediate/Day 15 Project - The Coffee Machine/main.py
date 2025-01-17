
"""

# Mi programa

import menu


coffees = menu.MENU
resources = menu.resources

def ask_for_coffee():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    while order != "espresso" and order != "latte" and order != "cappuccino" and order != "report":
        order = input("Wrong order!!! Write it again. ")
    return order

def count_money(order):
    money = 0.0
    quarter = int(input("How many quarters?: "))
    money += quarter * 0.25
    dime = int(input("How many dimes?: "))
    money += dime * 0.10
    nickle = int(input("How many nickles?: "))
    money += nickle * 0.05
    pennie = int(input("How many pennies?: "))
    money += pennie * 0.01
    money -= coffees[order]["cost"]
    if money < 0:
        print("Sorry that's not enough money. Money refunded.")
    return round(money, 2)


def check_resources(order):
    for ele in resources:
        if resources[ele] < coffees[order]["ingredients"][ele]:
            print(f"Sorry, there is not enough {ele}")
            return False
    return True


def waste_resources(order):
    for ele in resources:
        resources[ele] = resources[ele] - coffees[order]["ingredients"][ele]
    return resources



def coffe_machine():

    order = ask_for_coffee()

    if order == "report":
        for ele in resources:
            print(ele + ": " + str(resources[ele]))
        order = ask_for_coffee()

    continue_process = check_resources(order)

    if continue_process:
        dineros = count_money(order)
        resoruces = waste_resources(order)
        print(dineros)
        print(resoruces)

    return continue_process


coffee_machine_work = True
while coffee_machine_work:
    coffee_machine_work = coffe_machine()
"""


#########################################
##############  PROPUESTA  ##############
#########################################
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])























