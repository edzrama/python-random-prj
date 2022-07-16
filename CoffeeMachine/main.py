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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def report(val):
    for resource in resources:
        print(f"{resource} : {resources[resource]}")
    print(f"money : {money}")


def off(val):
    global repeat
    repeat = False
    print("Machine Shutting down")


def espresso(item):
    make_a_coffee(item)


def latte(item):
    make_a_coffee(item)


def cappuccino(item):
    make_a_coffee(item)


def make_a_coffee(val):
    ingredients = MENU[val]['ingredients']
    sufficient = True
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            sufficient = False
    if sufficient:
        calc_coin(val)


def calc_coin(item):
    print("Please insert coins.")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.10
    nickles = float(input("How many nickels? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    total_payment = quarters + dimes + nickles + pennies
    cost = MENU[item]['cost']
    if total_payment >= cost:
        calc_change(item, total_payment, cost)
    else:
        print("Sorry, that's not enough money. Money refunded.")


def calc_change(item, total_payment, cost):
    deduct_ingredients(item)
    total_change = round((total_payment - cost), 2)
    global money
    money += cost
    if total_change != 0:
        print(f"Here is ${total_change} in change.")
    else:
        print("Thank you for paying the exact amount.")
    print(f"Here is your {item} ☕ Enjoy!")


def deduct_ingredients(val):
    ingredients = MENU[val]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


commands = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
    "report": report,
    "off": off
}

repeat = True
while repeat:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command in commands:
        check_command = commands[command]
        check_command(command)
    else:
        print("Invalid command")
