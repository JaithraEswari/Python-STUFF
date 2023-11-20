import random
from hangman_art import *
from hangman_words import *

chosen_word = random.choice(word_list)

print(logo)
print(f'the solution is {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6

end_of_game = False
while not end_of_game:

    guess = input('Guess the letter: ').lower()
    if guess in display:
        print(f'You have already guessed this letter, The letter {guess}.')
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess in letter:
            display[position] = letter

    print(display)
    print(stages[lives])

    if guess not in chosen_word:
        print(f'The letter you have guessed is wrong, The letter {guess} does not exist in the word.')
        lives -= 1
    if lives == 0:
        end_of_game = True
        print('You Lose!')

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('You Win!')

    
