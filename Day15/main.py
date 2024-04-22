# coin operated coffee machine project

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50, 
            "coffee": 18},
        "price": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200, 
            "coffee": 24, 
            "milk": 150},
        "price": 2.50
        },
    "cappuccino": {
        "ingredients":{
            "water": 250, 
            "coffee": 24, 
            "milk": 100}, 
        "price": 3.00}
}
coffee_machine = {'water': 300, "milk": 200, "coffee": 100}


def report():
    #print report 
    print(f"Water: {coffee_machine['water']}ml")
    print(f"Milk: {coffee_machine['milk']}ml")
    print(f"Coffee: {coffee_machine['coffee']}g")
    print(f"Money: ${coffee_machine['cash']}")

coins = {"penny": .01, "nickel": .05, "dime": .10, "quarter": .25}
on = True
while on:
    choice = input('What would you like? (espresso/latte/cappuccino)')
    if choice == 'off':
        on = False
    if choice in ['espresso', 'cappuccino', 'latte']:
        #check sufficient resources to make drink 
        for ingredient in MENU[choice]["ingredients"]:
            if MENU[choice]["ingredients"][ingredient] < coffee_machine[ingredient]:
                sufficient_resource = True
            else: 
                suffient_resource = False
                print(f"Sorry there is not enough {ingredient}")
                
        #if enough resources check sufficient funds 
        if sufficient_resource==True: 
            quarters    = input('How many quarters? ')
            dimes = input('How many dimes? ')
            nickels = input("How many nickels? ")
            pennies = input("How many pennies? ")
            total = float(quarters)*.25+float(dimes)*.1+float(nickels)*.05+float(pennies)*.01
            if total >= MENU[choice]["price"]:
                #remove resources from report
                # change = round(total - MENU[choice]["price"], 2)
                # coffee_machine['cash'] = coffee_machine['cash'] + total - change
                # if change != 0:
                #     print(f"Here is ${change} in change.")
                for key in coffee_machine: 
                    coffee_machine[key] = coffee_machine[key]-MENU[choice]["ingredients"][key]
            else: 
                print('Sorry that is not enough money. Money Refunded.')
    if choice == 'report':
        report()
            


