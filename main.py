import re
from initial_data import MENU
from initial_data import resources
from initial_data import coins


balance = 0
recipes = list(MENU.keys())
products_titles = [product for product in resources]
initial_resources = []
for key, value in resources.items():
    initial_resources.append(value)
current_resources = initial_resources

# display list of recipes presented in the menu
def show_menu():
    menu_items = []
    for item, values in MENU.items():
        menu_items.append(f"{item} ${'%.2f' % values['cost']}")
    print(' | '.join(menu_items))

# get price for an item from the menu
def get_cost(receipt):
    return round(MENU[receipt]['cost'], 2)

# get amount of resources required for one ingredient in the recipe 
# and catch KeyError to return 0 for case when resource exists but not required for the receipt
def get_ingredient_amount(recipe, ingredient):
    try:
        return MENU[recipe]['ingredients'][ingredient]
    except KeyError:
        return 0

# check what resources and their amount are required for order and return them in a list
def required_ingredients(recipe):
    required_ingredients = []
    for product in products_titles:
        required_ingredients.append(get_ingredient_amount(recipe, product))
    return required_ingredients

# check if existing resources will be enough to make an order
def resources_sufficiency(existing_resources, required_resources):
    for i in range(len(existing_resources)):
        if existing_resources[i] >= required_resources[i] and existing_resources[i] > 0:
            print(type(existing_resources[i]))
            return True
        else:
            return False
        
# return status for amount of resources
def check_insufficiency_reason():
    if current_resources[0] == 0:
        return 'out of water'
    elif current_resources[1] == 0:
        return 'out of milk'
    elif current_resources[2] == 0:
        return 'out of coffee'
    else:
        return 'existing resources is not enough to make an order'


# substract resources required for order and return the remaining resources
def substract_resources(existing_resources, used_resources):
    for i in range(len(existing_resources)):
        if existing_resources[i] - used_resources[i] >= 0:
            existing_resources[i] -= used_resources[i]
    return existing_resources

# insert coins of different values in different amount 
# check if entered amount is valid (it should be int)
# and return the dict of them along with their name, value and amount
def insert_coins():
    inserted_coins_dict = {}
    for coin_name, coin_values in coins.items():
        coin_value = coin_values['value']
        inserted_coins = input(f'How many {coin_name}s ({coin_value}¢) 🪙 ? ')
        while not re.match('^\\d+$', inserted_coins):
            inserted_coins = input(f'Please enter correct amount of {coin_name}s ({coin_value}¢) 🪙 : ')
        # sum of coins inserted for one of the coins type (its amount multiplied by value)
        inserted_coins_amount = int(inserted_coins) * int(coin_value) / 100
        inserted_coins_dict[coin_name] = {
            'value': int(coin_value),
            'amount': int(inserted_coins)
        }
        print(f'{inserted_coins} {coin_name}s ({coin_value}¢) in total amount ${"%.2f" % inserted_coins_amount} inserted.')
    return inserted_coins_dict

# count a sum of all coins and return it in format round(sum, 2)
def count_sum_coins(some_coins):
    sum_coins = 0
    for name, values in some_coins.items():
        sum_coins += values['value'] * values['amount'] / 100
    return round(sum_coins, 2)

# add money from order to the balance
def upgrade_balance(deposit):
    global balance
    balance += deposit
    return balance

# print report with resources and coins balance
def print_report():
    print(f'Water {current_resources[0]} ml')
    print(f'Milk {current_resources[1]} ml')
    print(f'Coffee {current_resources[2]} g')
    print(f'Money ${"%.2f" % balance}')


##############################################################################

# add 'off' functionality to stop the execution of the coffee machine
is_on = True

while is_on:
    # print welcome message
    print('Welcome to the Coffee Machine!')

    # print menu
    print('Please let me know your choice.')
    show_menu()

    # ask what customer would like to order
    order = input('Type 1, 2 or 3: ')

    # add report and off functionality to the start menu
    if order.lower() == 'report':
        print_report()
    elif order.lower() == 'off':
        is_on = False
    elif int(order) in range(1, 4):
        recipe = recipes[int(order) - 1]
        print_report()
        ## check if resources sufficient
        if resources_sufficiency(current_resources, required_ingredients(recipe)):
            

            print(f'Your order is {recipe[5:].capitalize()}.')
            ## ask to insert coins
            print(f'Please insert the coins for total amount ${"%.2f" % get_cost(recipe)}.')
            inserted_coins = insert_coins()
            sum_inserted_coins = count_sum_coins(inserted_coins)
            required_coins = get_cost(recipe)

            ### check if inserted amount enough to pay for the order
            if sum_inserted_coins == required_coins:
                #add money to balance
                print('Amount is accepted. ')
                balance = upgrade_balance(required_coins)
                print('☕ ☕ ☕ ☕ ☕ Preparing order ☕ ☕ ☕ ☕ ☕')
                #substract the resources
                current_resources = substract_resources(current_resources, required_ingredients(recipe))
                #return the order 
                print(f'Your {recipe[5:].capitalize()} is ready.\nEnjoy your virtual coffee experience!')

            ### if money is not enough then make a refund
            elif sum_inserted_coins < required_coins:               
                print('Inserted coins is not enough for the order.')
                print(f'You have inserted ${sum_inserted_coins}, it is not enough for {recipe[5:].capitalize()} (${"%.2f" % required_coins}).')
                print(f'Inserted amount will be refunded in full, please take ${sum_inserted_coins} from the coin return.')

            ### if money is more than required then return charge and make the order
            elif sum_inserted_coins > required_coins:
                #count charge
                change = round(sum_inserted_coins - required_coins, 2)
                print(f'Inserted ${"%.2f" % sum_inserted_coins} in total which is more than required for {recipe[5:].capitalize()} (${"%.2f" % required_coins}).')
                #uprgade balance
                balance = upgrade_balance(required_coins)
                print(f'Please take you change in amount ${("%.2f" % change)}.')
                print('☕ ☕ ☕ ☕ ☕ Preparing order ☕ ☕ ☕ ☕ ☕')
                #substract the resources used
                current_resources = substract_resources(current_resources, required_ingredients(recipe))
                #return the order 
                print(f'Your order {recipe[5:].capitalize()} is ready.\nEnjoy your virtual coffee experience!')

        ## if resources insufficient then notify order cannot be done
        else:
            reason = check_insufficiency_reason()
            print(f'Insufficient resources: {reason}.')
            print('Please try to make another order or return later.')
            
    print_report()
    # separate the coffee sessions
    print('\n')
    print('##############################################################################')
    print('\n')
