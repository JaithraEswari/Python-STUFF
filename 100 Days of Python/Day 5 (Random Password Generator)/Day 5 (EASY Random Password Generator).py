import random

print('Welcome to the PyPassword Generator!')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input('How many letters would you like in your password?\n'))
num_numbers = int(input('How many symbols would you like?\n'))
num_symbols = int(input('How many numbers would you like?\n'))

password = ''

for letter in range(1, num_letters + 1):
    rnd_letter = random.choice(letters)
    password += rnd_letter

for number in range(1, num_numbers + 1):
    rnd_number = random.choice(numbers)
    password += rnd_number

for symbol in range(1, num_symbols + 1):
    rnd_symbol = random.choice(symbols)
    password += rnd_symbol

print(f'Here is your password: {password}')