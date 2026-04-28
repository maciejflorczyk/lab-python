from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

serve_coffee = True

while serve_coffee:

    option = menu.get_items()

    choice = input("What would you like? (espresso / latte / cappuccino): ").lower()

    if choice == "off":
        serve_coffee = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)


""" 
    if choice in option
        print(choice)
       
      if check_resources(choice):
            cashier(choice)
    elif choice == "off":
        print("Off")
        serve_coffee = False
    elif choice == "report":
        print("Report:")
        report()
    else:
        print("Wrong choice!")
"""
