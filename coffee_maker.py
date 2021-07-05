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

def check_resources(drink_selection, machine_resources):
    water_needed = MENU.get(drink_selection, {}).get("ingredients", {}).get("water", 0)
    milk_needed = MENU.get(drink_selection, {}).get("ingredients", {}).get("milk", 0)
    coffee_needed = MENU.get(drink_selection, {}).get("ingredients", {}).get("coffee", 0)
    machine_water = machine_resources.get("water", 0)
    machine_milk = machine_resources.get("milk", 0)
    machine_coffee = machine_resources.get("coffee", 0)
    if machine_water < water_needed:
        return "Sorry, there is not enough water."
    elif machine_milk < milk_needed:
        if drink_selection == "espresso":
            pass
        else:
            return "Sorry, there is not enough milk."
    elif machine_coffee < coffee_needed:
        return "Sorry, there is not enough coffee."
    else:
        return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_coins = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total_coins

def sufficient_funds(payment, cost):
    if payment >= cost:
        return True
    else:
        return False

def make_coffee(drink_selection, machine_resources):
    water_needed = MENU.get(drink_selection, {}).get("ingredients", {}).get("water", 0)
    milk_needed = MENU.get(drink_selection, {}).get("ingredients", {}).get("milk", 0)
    coffee_needed = MENU.get(drink_selection, {}).get("ingredients", {}).get("coffee", 0)
    machine_water = machine_resources.get("water", 0)
    machine_milk = machine_resources.get("milk", 0)
    machine_coffee = machine_resources.get("coffee", 0)
    water_remaining = machine_water - water_needed
    milk_remaining = machine_milk - milk_needed
    coffee_remaining = machine_coffee - coffee_needed
    return water_remaining, milk_remaining, coffee_remaining

machine_on = True
profit = 0
while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        machine_on = False
    elif selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        resources_sufficient = check_resources(selection, resources)
        if resources_sufficient:
            user_payment = process_coins()
            drink_cost = MENU.get(selection, {}).get("cost", 0)
            sufficient_coins = sufficient_funds(user_payment, drink_cost)
            if sufficient_coins:
                if user_payment == drink_cost:
                    profit += user_payment
                else:
                    profit += drink_cost
                    user_change = user_payment - drink_cost
                    print(f"Here is ${user_change:.2f} dollars in change.")
                    new_water, new_milk, new_coffee = make_coffee(selection, resources)
                    resources["water"] = new_water
                    resources["milk"] = new_milk
                    resources["coffee"] = new_coffee
                    print(f"Here is your {selection}. Enjoy!")
            else:
                print(f"Sorry, that's not enough money. Money refunded")