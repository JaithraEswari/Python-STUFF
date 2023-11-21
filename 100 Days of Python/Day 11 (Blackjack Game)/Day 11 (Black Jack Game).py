import random
import os
from art import logo

start_game = True
while start_game:
    game_start = input(
        "Do you want to play a game of black jack? Type 'y' or 'n': ")
    if game_start == 'y':
        print(logo)

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        def deal_card():
            random_card = random.choice(cards)
            return random_card

        def calculate_score(sum_cards):
            calculated_score = sum(sum_cards)
            if calculated_score == 21 and len(sum_cards) == 2:
                return 0
            elif 11 in sum_cards and calculated_score > 21:
                sum_cards.remove(11)
                sum_cards.append(1)
            return calculated_score

        def compare(user_score, computer_score):
            if user_score == computer_score:
                return "Draw"
            elif computer_score == 0:
                return "The user has lost"
            elif user_score == 0:
                return "The user has won"
            elif user_score > 21:
                return "The user has lost"
            elif computer_score > 21:
                return "The computer has lost"
            elif user_score > computer_score:
                return "The user has won"
            else:
                return "The computer has won"

        user_cards = []
        computer_cards = []
        game_not_over = True

        for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while game_not_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current_score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                game_not_over = False
            else:
                next_round = input("Do you want to draw another card? Type 'y' or 'n': ")

                if next_round == 'y':
                    user_cards.append(deal_card())
                elif computer_score < 17:
                    computer_cards.append(deal_card())
                else:
                    game_not_over = False

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final_score: {computer_score}")
        print(compare(user_score, computer_score))
        new_game = input("Do you want to restart the game? Type 'y' or'n': ")
        if new_game == 'n':
            start_game = False
        else:
            os.system('cls')
    else:
        start_game = False