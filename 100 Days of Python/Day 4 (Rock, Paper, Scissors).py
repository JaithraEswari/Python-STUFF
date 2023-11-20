import random
player_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
random_integer = random.randint(0, 2)
options = ['Rock', 'Paper', 'Scissors']

if(player_input >= 3):
    print('Nuh uh! You lose.')
else:
    print(f'Player chooses:{options[player_input]}')
    print(f'Computer chooses:{options[random_integer]}')

    if(options[player_input] == options[random_integer]):
        print('Draw')
    elif(options[player_input] == 'Scissors' and options[random_integer] == 'Paper'):
        print("You win!")
    elif(options[player_input] == 'Paper' and options[random_integer] == 'Rock'):
        print("You win!")
    elif(options[player_input] == 'Rock' and options[random_integer] == 'Scissors'):
        print("You win!")
    else:
        print('You lose')   




