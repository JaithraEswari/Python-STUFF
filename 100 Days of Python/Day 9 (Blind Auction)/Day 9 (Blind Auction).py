import os
bidders = {}
print("Welcome to the blind auction program.")

def highest_bidder_name(bidders):
    highest_bidder = 0
    winner = ""
    for bidder in bidders:
        bidding_amount = bidders[bidder]
        if bidding_amount > highest_bidder:
            highest_bidder = bidding_amount
            winner = bidder
    print(f'The winner is {winner} with an amount of ${highest_bidder}')



question = True
while question:
    name = input("Enter your name: ")
    price = int(input("Enter your bidding price: $"))
    bidders[name] = price
    question = input("Do you want to continue: ")
    if question == 'yes':
        os.system('cls')
    else:
        question = False
        highest_bidder_name(bidders)
        max_value = max(bidders.values())
        # print(f'Max value is {max_value}')


