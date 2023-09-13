import random
from art import logo
import os

def intro():
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 to 100.")
    computer_guessed_number = random.randint(1,100)
    #print(computer_guessed_number)
    difficulty_level(computer_guessed_number)
    play_game = input('Want to play the game again? Type \'y\' or \'n\'?  ')
    if play_game == 'y':
        intro()
    else:
        print("Thanks for playing the game. Have a great day.")
    
def difficulty_level(computer_guessed_number):
    level = input("Choose a difficulty. Type \'easy\' or \'hard\':  ").lower()
    if level != 'easy' and level != 'hard':
        print("Enter correct difficulty level.")
        difficulty_level(computer_guessed_number)
    elif level == 'easy':
        attempts = 10
        guess(attempts,computer_guessed_number)
    else:
        attempts = 5
        guess(attempts,computer_guessed_number)

def guess(attempts,computer_guessed_number):
    is_game_over = False
    while not is_game_over and attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guessed_number = int(input("Make a guess: "))
        if user_guessed_number == computer_guessed_number:
            print("Wooh!!! You guessed it correct.")
            print(f"Computer guessed: {computer_guessed_number}")
            is_game_over =True
        elif user_guessed_number + 5 == computer_guessed_number or user_guessed_number - 5 == computer_guessed_number:
            print("Very close in guessing the number.")
            attempts -= 1
        elif user_guessed_number > computer_guessed_number:
            print("Too high.")
            attempts -= 1
        else:
            print("Too low.")
            attempts -= 1
        if attempts != 0 and is_game_over == False:
            print("Guess again.")
    if attempts == 0 :
        print("You ran out of guesses, you lose.")
        print(f"Computer guessed: {computer_guessed_number}")
    
intro()
    

"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""
    