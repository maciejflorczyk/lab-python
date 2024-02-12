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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


bank = {
    "quarters": 0,  # 0.25
    "dimes": 0,  # 0.10
    "nickles": 0,  # 0.05
    "pennies": 0,  # 0.01
}

coins_paid = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}

coins_value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

coffee_machine_on = True

sum_paid = 0.0
total_cash = 0.0
give_coffee = False

# print(resources["water"])
# print(resources["milk"])
# print(resources["coffee"])
#
# print(MENU["espresso"])
# print(MENU["espresso"]["ingredients"])
# print(MENU["espresso"]["ingredients"]["water"])
# print(MENU["espresso"]["ingredients"]["milk"])
# print(MENU["espresso"]["ingredients"]["coffee"])
# print(MENU["espresso"]["cost"])

# def are_there_enough_resources(choice_value):
#     if choice_value == "espresso":
#     if choice_value == "latte":
#     if choice_value == "cappuccino":
#     if choice_value == "report":

# print("What would you like? (espresso/latte/cappuccino or print 'report'): ")
# print("Please insert coins.")
# print("How many quarters?: ")
# print("How many dimes?: ")
# print("How many nickles?: ")
# print("How many pennies?: ")
#
# print("Here is $1.6 in change.")
# print("Here is your {coffee_type} {logo} . Enjoy!")
#
# print("What would you like? (espresso/latte/cappuccino): ")
# print("Sorry there is not enough water.")


## TODO: Function: what operation do you want to perform?

def operation():
    choice_value = input("What would you like? (espresso/latte/cappuccino): ")
    return choice_value


def do_we_have_resources(choice_made):
    enough_resources = False

    for ingredient in MENU[choice_made]["ingredients"]:
        if MENU[choice_made]["ingredients"][ingredient] > resources[ingredient]:
            enough_resources = False
            print(f"Sorry, there is not enough {ingredient}.")
            return enough_resources
        else:
            # resources[ingredient] = - MENU[choice_made]["ingredients"][ingredient]
            enough_resources = True
            return enough_resources
    return enough_resources

def reduce_resources(choice_made):
    for ingredient in MENU[choice_made]["ingredients"]:
         resources[ingredient] -= MENU[choice_made]["ingredients"][ingredient]

def insert_coins():
    global sum_paid
    for coin in coins_paid:
        coins_paid[coin] = int(input(f"How many {coin}: "))

    # print(f"Bank: {sum(bank.values())}")
    # print(f"{choice} cost: {MENU[choice]["cost"]}")
    for coin in coins_paid:
        # coins_paid[coin] = int(input(f"How many {coin}: "))
        sum_paid += round(float(coins_value[coin] * coins_paid[coin]),2)
        #print(f"Sum paid: {sum_paid}")
    change = round(sum_paid - MENU[choice]["cost"],2)
    if change >= 0:
        print(f"Sum paid: {sum_paid}")
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def hand_coffee():
    global give_coffee
    if give_coffee == True:
        print(f"Here is your {choice}. Enjoy!")
        reduce_resources(choice)


def coffee_machine_power():
    turn_off = input("Do you want to turn the coffee machine off? 'yes' or 'no': ")
    if turn_off == "yes":
        return False
    elif turn_off == "no":
        return True
    else:
        return False


def report():
    for value in resources:
        print(f"{value}: {resources[value]}")
    print(f"Sum paid: {total_cash}")

while coffee_machine_on:
    sum_paid = 0.0
    choice = operation()
    if choice == "report":
        report()
    elif choice == "turnoff":
        coffee_machine_on = False
    else:
        if do_we_have_resources(choice):
            give_coffee = insert_coins()
            hand_coffee()
    total_cash += sum_paid
## TODO: add cash balance to the report