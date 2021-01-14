from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
espresso = MenuItem("espresso", 50, 0, 18, 1.50)
latte = MenuItem("latte", 200, 24, 150, 2.50)
cappuccino = MenuItem("cappuccino", 250, 24, 100, 3.00)
menu = Menu()

def getInput():
    return input(f"What would you like? {menu.get_items()}:").strip()

run = True
while run:

    choice = getInput()
    if choice == "off":
        run = False
    elif choice == "report":
        maker.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if maker.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    maker.make_coffee(drink)