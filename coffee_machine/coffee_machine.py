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

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

def check_resources(drink_name):
    global water, milk, coffee, money
    water_requirement, milk_requirement, coffee_requirement = 0, 0, 0
    drink = MENU[drink_name]
    ingredients = drink['ingredients']
    ingredient_items = ingredients.keys()

    if 'water' in ingredient_items:
        water_requirement = ingredients['water']

    if 'milk' in ingredient_items:
        milk_requirement = ingredients['milk']

    if 'coffee' in ingredient_items:
        coffee_requirement = ingredients['coffee']

    cost = drink['cost']
    if water >= water_requirement and milk >= milk_requirement and coffee >= coffee_requirement:
        quarters_request = float(input("Please insert coins.\nhow many quarters?: "))
        dimes_request = float(input("how many dimes?: "))
        nickles_request = float(input("how many nickles?: "))
        pennies_request = float(input("how many pennies?: "))
        total_inserted = quarters_request * QUARTER + dimes_request * DIME + nickles_request * NICKLE + pennies_request * PENNY
        if total_inserted >= cost:
            change = round(total_inserted - cost, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {drink_name}. Enjoy!")
            money += cost
            water -= water_requirement
            milk -= milk_requirement
            coffee -= coffee_requirement
        else:
            print("Sorry that's not enough money. Money refunded.")
    else: # not enough resources
        if water < water_requirement:
            print("  Sorry there is not enough water")
        elif milk < milk_requirement:
            print("  Sorry there is not enough milk")
        else:
            print(" Sorry there is not enough coffee")

money = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

while True:
    water_str = f"Water: {water}ml"
    milk_str = f"Milk: {milk}ml"
    coffee_str = f"Coffee: {coffee}g"
    money_str = f"Money: ${money}"

    user_input = input("  What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'report':
        print(water_str)
        print(milk_str)
        print(coffee_str)
        print(money_str)
        continue
    elif user_input == 'off':
        break
    else:
        if user_input not in MENU.keys():
            print("Oops, the coffee you've entered is not in our menu!")
            continue
        check_resources(user_input)



