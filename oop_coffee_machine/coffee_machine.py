from replit import clear

def make_drink(order, resource, drink):
    """Deducts ingredients from resources to make the drink"""
    items = 'ingredients'
    for item in order[items]:
        if item in resource:
            resource[item] -= order[items][item] 
    print(f"Here is your {drink}. Enjoy!")

def resource_checker(resource_list, ingredients):
    """Returns False if not enough resources available, or True if resources are sufficient"""
    for item_x, value_x in ingredients.items():
        for item_y, value_y in resource_list.items():
            if item_x == item_y:
                if value_x > value_y:
                   print(f"Sorry there is not enough {item_y}.")
                   return False   
    return True
           

def money_checker(payment, price):
    """returns true if enough money has been received for payment, or false if not enough"""
    if payment == price or payment > price:
        return True
    else:
        return False

def cashier(payment, price):
    """Returns change left over"""
    print(f'Here is your ${payment - price} in change')

def get_report(resource_list):
    """Gathers and prints the inventory of resources dictionary"""
    global money
    for item in resource_list:
        if item == "coffee":
            print(f"{item.title()}: {resource_list[item]}g")
        else:
            print(f"{item.title()}: {resource_list[item]}ml")
    print((f"Money: ${money}")) 

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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffee_maker():           
    global money
    running = True
    while running:
        take_order = input('What would you like? (espresso/latte/cappuccino): ').lower()
      
        if take_order == 'report':
            get_report(resources)
        elif take_order == 'off':
            running = False
        else:
            order = MENU[take_order]
            if resource_checker(resources, order['ingredients']):
                quarters = (input("Please insert coins.\nHow many quarters?: "))
                if quarters == '': quarters = 0
                else: quarters = int(quarters)
                dimes = (input('How many dimes?: '))
                if dimes == '': dimes = 0
                else: dimes = int(dimes)
                nickels = (input('How many nickels?: '))
                if nickels == '': nickels = 0
                else: nickels = int(nickels)
                pennies = (input('How many pennies?: '))
                if pennies == '': pennies = 0
                else: pennies = int(pennies)

                total_change = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
                price = order['cost']

                if take_order == 'espresso':
                    if money_checker(total_change, price):
                        cashier(total_change, price)
                        make_drink(order, resources, take_order)
                        money += price
                    else: 
                        print("Sorry that is not enough money. Money refunded")
                elif take_order == 'latte':
                    if money_checker(total_change, price):
                        cashier(total_change, price)
                        make_drink(order, resources, take_order)
                        money += price
                    else: 
                        print("Sorry that is not enough money. Money refunded")
                elif take_order == 'cappuccino':
                    if money_checker(total_change, price):
                        cashier(total_change, price)
                        make_drink(order, resources, take_order)
                        money += price
                    else: 
                        print("Sorry that is not enough money. Money refunded")
            else:
                coffee_maker()
clear()            
coffee_maker()