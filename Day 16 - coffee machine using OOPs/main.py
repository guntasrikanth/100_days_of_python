from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
#menuitem = MenuItem()
money = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have? {options}: ")
    #print(choice)
    if choice == 'off':
        print("Bye bye 👋. Turning off.")
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        #menuitem = MenuItem(drink.name, drink.ingredients["water"], drink.ingredients["milk"], drink.ingredients["coffee"], drink.cost)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)
