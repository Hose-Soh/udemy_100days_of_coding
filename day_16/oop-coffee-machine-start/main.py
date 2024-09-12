from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    user_select = input(f"What would you like? ({options}) ")
    if user_select=="off":
        break
    elif user_select=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_select)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)