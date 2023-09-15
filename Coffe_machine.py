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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True
    

def check_money(cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global profit
    print("Please insert coins.")
    quaters = int(input("how many quaters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    penny = int(input("how many pennies?: "))
    money = round((0.25 * quaters + 0.1 * dimes + 0.05 * nickles + 0.01 * penny), 2)
    if money >= cost:
        change = round((money - cost),2)
        print(f"Here is your change ${change}")
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffe(choice, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕. Enjoy!")
    
    
def coffee():
    still_on = True
    while still_on:
        choice = input("What would you like to have? (espresso/latte/cappuccino):  ").lower()
        if choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            drink = MENU[choice]
            if check_resources(drink['ingredients']):
                if check_money(drink['cost']):
                    make_coffe(choice, drink["ingredients"])
        elif choice == 'off':
            print("Bye bye 👋. Turning off.")
            still_on = False
        else:
            print("Enter valid option")
       
print("Hi, Hope you're having a great day") 
coffee()

    


"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""