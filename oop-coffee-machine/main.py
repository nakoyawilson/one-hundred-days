from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

the_menu = Menu()
menu_items = the_menu.get_items()[:-1]

user_selection = input(f"What would you like? ({menu_items}): ")