#from replit import clear
import os
from art import logo

def highest_bidder(auction_dict):
  highest = 0
  for key in auction_dict:
    if auction_dict[key] > highest:
      highest = auction_dict[key]
      winner = key
  print(f'The winner is {winner.capitalize()} with a bid of ${highest}')

print(logo)
print("Welcome to the secret auction program")
auction_dict = {}
info = 'yes'
while info == 'yes':
  name = input("What is your name?  ")
  bid = int(input("What's your bid? $"))
  auction_dict[name] = bid
  info = input("Type \'yes\' if there are other bidders, otherwise type \'no\'\n").lower()
  #clear()
  os.system('cls')

highest_bidder(auction_dict)


"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""