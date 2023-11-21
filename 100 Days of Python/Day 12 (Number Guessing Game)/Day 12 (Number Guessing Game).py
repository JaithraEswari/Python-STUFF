import random
from art import logo
print(logo)
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

random_number = random.randint(1,100)
print(random_number)

def hard():
    attempts = 5
    game_over = False
    while not game_over:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        if random_number == guess:
            print(f'You got it! The answer was {random_number}')
            game_over = True
        elif attempts == 1:
            print('You have run out of guesses. You lose.')
            game_over = True
        elif random_number > guess:
            print('Too low.')
            print('Guess again.')
        else:
            print('Too high.')
            print('Guess again.')
        attempts -= 1

def easy():
    attempts = 10
    game_over = False
    while not game_over:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        if random_number == guess:
            print(f'You got it! The answer was {random_number}')
            game_over = True
        elif attempts == 1:
            print('You have run out of guesses. You lose.')
            game_over = True
        elif random_number > guess:
            print('Too low.')
            print('Guess again.')
        else:
            print('Too high.')
            print('Guess again.')
        attempts -= 1

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'hard':
    hard()
else:
    easy()
        
        

