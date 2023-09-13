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

'''def blackjack():
    computer = []
    user = []
    is_game_over = input("Do you want to play Blackjack game? Type \'y\' or \'n': ").lower()
    if is_game_over == 'y':
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
                    print(f"\nYour final hand: {user}, final score: {user_sum}")
                    print(f"computer's final hand: {computer}, final score: {computer_sum}")
                    print("You busted. You lose")
                    blackjack()
            else:
                can_continue = False
                print(f"\nYour final hand: {user}, final score: {user_sum}")
                print(f"computer's final hand: {computer}, final score: {computer_sum}")
                if user_sum == computer_sum:
                    print("Draw")
                elif user_sum > computer_sum and user_sum < 22:
                    print("Hurray!!!, You won.")
                else:
                    print("You lose.")
        blackjack()
    else:
        print("Thanks for playing Blackjack game") 
blackjack() '''

def calculate(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        print("Both Busted, you lose")
    elif user_score == computer_score:
        print("Draw")
    elif computer_score ==0:
        print("You lose, opponent has Blackjack.")
    elif user_score == 0:
        print("You Won with a Blackjack")
    elif user_score > 21:
        print("You Busted, you lose")
    elif computer_score > 21:
        print("Computer Busted, you won")
    elif user_score > computer_score:
        print("You win")
    else:
        print("You lose")

def blackjack():
    computer = []
    user = []
    print(logo)
    is_game_over =False
    for i in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
        
    while not is_game_over:
        user_score = calculate(user)
        computer_score = calculate(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"computer's first card: {computer[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            play = input(f"Type \'y\' to get another card, type \'n\' to pass: ")
            if play =='y':
                user.append(random.choice(cards))
            else:
                is_game_over = True
    
    while computer_score!=0 or computer_score<17:
        computer.append(random.choice(cards))
        computer_score = calculate(computer)  
        
    print(f"\nYour final hand: {user}, final score: {user_score}")
    print(f"computer's final hand: {computer}, final score: {computer_score}")
    compare(user_score, computer_score)
    
play_again = 'y'
while play_again == 'y':
    os.system('cls')
    blackjack()
    play_again = input("Do you want to Blackjack game? Type \'y\' or \'n\'?  ")
    

"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""