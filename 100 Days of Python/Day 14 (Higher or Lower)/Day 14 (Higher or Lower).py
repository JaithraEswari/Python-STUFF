import random
import os
from art import *
from game_data import *

random_index_1 = random.randint(0, len(data) - 1)

name1 = data[random_index_1]['name']
follower_count1 = data[random_index_1]['follower_count']
description1 = data[random_index_1]['description']
country1 = data[random_index_1]['country']

score = 0

game_over = False
while not game_over:

    random_index_2 = random.randint(0, len(data) - 1)

    name2 = data[random_index_2]['name']
    follower_count2 = data[random_index_2]['follower_count']
    description2 = data[random_index_2]['description']
    country2 = data[random_index_2]['country']

    print(logo)
    print(f"Compare A: {name1}, a {description1}, from {country1}")
    print(vs)
    print(f"Against B: {name2}, a {description2}, from {country2}")
    
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()


    if answer == "A" and follower_count1 > follower_count2:
        score += 1
        name2 = name1
        follower_count2 = follower_count1
        description2 = description1
        country2 = country1
        print(f"You are right! Current score: {score}")
    elif answer == "B" and follower_count1 < follower_count2:
        score += 1
        name1 = name2
        follower_count1 = follower_count2
        description1 = description2
        country1 = country2
        print(f"You are right! Current score: {score}")
    else:
        game_over = True
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
