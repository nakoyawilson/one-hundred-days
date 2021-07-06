from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
the_menu = Menu()
the_coffee_maker = CoffeeMaker()
the_money_machine = MoneyMachine()

menu_items = the_menu.get_items()[:-1]

machine_on = True
while machine_on:
    user_selection = input(f"What would you like? ({menu_items}): ")
    if user_selection == "off":
        machine_on = False
    elif user_selection == "report":
        print(the_coffee_maker.report())
        print(the_money_machine.report())
    else:
        item = the_menu.find_drink(user_selection)
        sufficient_resources = the_coffee_maker.is_resource_sufficient(item)
        if sufficient_resources:
            print(sufficient_resources)
        else:
            print("Sorry, there is not enough resources.")
