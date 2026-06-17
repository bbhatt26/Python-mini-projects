MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 125,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200, 
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250, 
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def print_report():
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ₹{money}\n")

def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_payment(drink_cost):
    print(f"Drink price: ₹{drink_cost}")
    try:
        payment = float(input("Insert money ₹: "))
    except ValueError:
        print("Invalid input! Try again")
        return 0

    payment = round(payment, 2)
    return payment

def check_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ₹{change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")

# Main loop
is_on = True
while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
        print("Coffee machine shutting down... Goodbye!")

    elif choice == "report":
        print_report()

    elif choice in MENU:
        drink = MENU[choice]

        if check_resources(drink["ingredients"]):
            payment = process_payment(drink["cost"])

            if payment > 0 and check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

    else:
        print("Invalid choice! espresso/latte/cappuccino ?")