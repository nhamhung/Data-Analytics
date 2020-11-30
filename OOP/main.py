from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
items = menu.get_items()
machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    user_input = input(f"  What would you like? ({items}): ")
    if user_input == 'off':
        break
    elif user_input == 'report':
        coffee_maker.report()
        machine.report()
    else:
        drink = menu.find_drink(user_input) # return a MenuItem
        if drink is None:
            continue
        if coffee_maker.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

