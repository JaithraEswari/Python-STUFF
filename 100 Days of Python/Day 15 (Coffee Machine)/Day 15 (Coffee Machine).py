from menu_resources import *

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
quaters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
money = 0

espresso_water = menu["espresso"]["ingredients"]["water"]
espresso_coffee = menu["espresso"]["ingredients"]["coffee"]
espresso_cost = menu["espresso"]["cost"]

latte_water = menu["latte"]["ingredients"]["water"]
latte_milk = menu["latte"]["ingredients"]["milk"]
latte_coffee = menu["latte"]["ingredients"]["coffee"]
latte_cost = menu["latte"]["cost"]

cappuccino_water = menu["cappuccino"]["ingredients"]["water"]
cappuccino_milk = menu["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = menu["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = menu["cappuccino"]["cost"]


machine_off = False
while not machine_off:
    question = input('What would you like? (espresso/latte/cappucino): ')

    if question == 'espresso':
        if water < espresso_water:
            print('Sorry there is not enough water.')
        elif coffee < espresso_coffee:
            print('Sorry there is not enough coffee.')
        else:
            coin1 = float(input('Quaters: $'))
            coin2 = float(input('Dimes: $'))
            coin3 = float(input('Nickles: $'))
            coin4 = float(input('Pennies: $'))
            total_amount = quaters * coin1 + dimes * coin2 + nickles * coin3 + pennies * coin4 
            if total_amount == espresso_cost:
                water -= espresso_water
                coffee -= espresso_coffee
                money += espresso_cost
                print('Here is your espresso. Enjoy!')    
            elif total_amount > espresso_cost:
                water -= espresso_water
                coffee -= espresso_coffee
                change = total_amount - espresso_cost
                money += espresso_cost
                print(f'Here is ${change} in dollars in change.')
                print('Here is your espresso. Enjoy!')

            else:
                print('Sorry that is not enough money. Money refunded.')
            

    if question == 'latte':
        if water < latte_water:
            print('Sorry there is not enough water.')
        elif milk < latte_milk:
            print('Sorry there is not enough milk.')
        elif coffee < latte_coffee:
            print('Sorry there is not enough coffee.')
        else:
            coin1 = float(input('Quaters: $'))
            coin2 = float(input('Dimes: $'))
            coin3 = float(input('Nickles: $'))
            coin4 = float(input('Pennies: $'))
            total_amount = quaters * coin1 + dimes * coin2 + nickles * coin3 + pennies * coin4 
            if total_amount == latte_cost:
                water -= latte_water
                milk -= latte_milk
                coffee -= latte_coffee
                print('Here is your latte. Enjoy!')

            elif total_amount > latte_cost:
                water -= latte_water
                coffee -= latte_coffee
                change = total_amount - latte_cost
                money += latte_cost
                print(f'Here is ${change} in dollars in change.')
                print('Here is your latte. Enjoy!')
            else:
                print('Sorry that is not enough money. Money refunded.')


    if question == 'cappuccino':
        if water < cappuccino_water:
            print('Sorry there is not enough water.')
        elif milk < cappuccino_milk:
            print('Sorry there is not enough milk.')
        elif coffee < cappuccino_coffee:
            print('Sorry there is not enough coffee.')
        else:
            coin1 = float(input('Quaters: $'))
            coin2 = float(input('Dimes: $'))
            coin3 = float(input('Nickles: $'))
            coin4 = float(input('Pennies: $'))
            total_amount = quaters * coin1 + dimes * coin2 + nickles * coin3 + pennies * coin4 
            if total_amount == cappuccino_cost:
                water -= cappuccino_water
                milk -= cappuccino_milk
                coffee -= cappuccino_coffee
                print('Here is your cappuccino. Enjoy!')
            elif total_amount > cappuccino_cost:
                water -= cappuccino_water
                milk -= cappuccino_milk
                coffee -= cappuccino_coffee
                change = total_amount - cappuccino_cost
                money += cappuccino_cost
                print(f'Here is ${change} in dollars in change.')
                print('Here is your cappuccino. Enjoy!')
            else:
                print('Sorry that is not enough money. Money refunded.')

    if question == 'report':
        print(f'Water: {water}ml')
        print(f'Milk: {milk}ml')
        print(f'Coffee: {coffee}g')    
        print(f'Money: ${money}')

    if question == 'off':
        machine_off = True

