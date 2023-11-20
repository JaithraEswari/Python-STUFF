print("Welcome to Treasure Island.Your mission is to find the treasure.")
direction = input('left or right?\n')
if(direction == 'left'):
    travel_method = input('You have come across a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if(travel_method == 'wait'):
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
        if(door == 'yellow'):
            print('You Win!')
        else:
            print('Game Over')
    else:
        print('Game Over')
else:
    print('Game Over')
