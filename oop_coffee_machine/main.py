from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker as CM
from money_machine import MoneyMachine as MM
from replit import clear

coffee_maker = CM()
cashier = MM()
menu = Menu()

def coffee_machine():
    running = True
    while running:
        order = input(f"What would you like? ({menu.get_items()}): ").lower()
        if order == 'off':
            running = False
            clear()
        elif order == "report":
            coffee_maker.report()
            cashier.report()
        elif menu.find_drink(order):
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink):
                if cashier.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
    
coffee_machine()