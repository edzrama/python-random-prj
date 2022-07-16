from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = MoneyMachine()
maker = CoffeeMaker()
is_on = True
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == 'report':
        maker.report()
        machine.report()
    elif order == 'off':
        is_on = False
    else:
        menu_item = menu.find_drink(order)
        if menu_item is not None:
            if maker.is_resource_sufficient(menu_item):
                if machine.make_payment(menu_item.cost):
                    maker.make_coffee(menu_item)