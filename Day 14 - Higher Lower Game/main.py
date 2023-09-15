from Coffe_machine import logo, vs
from game_data import data
import random
import os

def game():
    flag = False
    score = 0
    b_data = random.choice(data)
    while not flag:
        os.system('cls')
        a_data = b_data
        b_data = random.choice(data)
        while a_data == b_data:
            b_data = random.choice(data)
        print(logo)
        if score >0:
            print(f"You're right. Current score: {score}.")
        print(f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}")
        print(vs)
        print(f"Against B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}")
        answer = input("Who has more followers? Type \'A\' or \'B\':  ").upper()
        check_answer, next_data = check(a_data, b_data)
        if answer != check_answer:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            flag = True
        else:
            score += 1
            #print(f"You're right. Current score: {score}.")
            a_data = b_data

def check(a_data,b_data):
    a_followers = a_data['follower_count']
    b_followers = b_data['follower_count']
    if a_followers > b_followers:
        return 'A' , a_data
    else:
        return 'B', b_data


game()



"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""