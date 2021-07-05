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
        return

machine_on = True
while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        machine_on = False
    elif selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $")
    elif selection == "espresso":
        resources_sufficient =check_resources(selection, resources)
    elif selection == "latte":
        resources_sufficient =check_resources(selection, resources)
    elif selection == "cappuccino":
        resources_sufficient =check_resources(selection, resources)