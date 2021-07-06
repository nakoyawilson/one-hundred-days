from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

the_menu = Menu()
menu_items = the_menu.get_items()[:-1]

machine_on = True
while machine_on:
    user_selection = input(f"What would you like? ({menu_items}): ")
    if user_selection == "off":
        machine_on = False