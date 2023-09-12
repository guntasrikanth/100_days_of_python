############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    computer = []
    user = []
    info = input("Do you want to play Blackjack game? Type \'y\' or \'n': ").lower()
    if info == 'y':
        computer = []
        user = []
        os.system('cls')
        print(logo)
        for i in range(2):
            user.append(random.choice(cards))
            computer.append(random.choice(cards))
        user_sum = sum(user)
        computer_sum = sum(computer)
        print("Welcome to Blackjack game")
        print(f"Your cards: {user}, current score: {user_sum}")
        print(f"computer's first card: {computer[0]}")
        can_continue = True
        while can_continue:
            play = input(f"Type \'y\' to get another card, type \'n\' to pass: ")
            if play == 'y':
                user.append(random.choice(cards))
                user_sum = sum(user)
                print(f"Your cards: {user}, current score: {user_sum}")
                print(f"computer's first card: {computer[0]}")
                if user_sum >21:
                    print(f"Your final hand: {user}, final score: {user_sum}")
                    print(f"computer's final hand: {computer}, final score: {computer_sum}")
                    print("You went over. You lose")
                    blackjack()
            else:
                can_continue = False
                print(f"Your final hand: {user}, final score: {user_sum}")
                print(f"computer's final hand: {computer}, final score: {computer_sum}")
                if user_sum > computer_sum and user_sum < 22:
                    print("You won.")
                else:
                    print("You lose.")
        blackjack()
    else:
        print("Thanks for playing Blackjack game")

blackjack()


"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""