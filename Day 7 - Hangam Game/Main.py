import random 
import words, hangman
lives = 6
end =True
word_list = words.word_list
choose_word = random.choice(word_list)

length = len(choose_word)
word = []
for _ in range(length):
  word.append('_')

print(f"Welcome to {hangman.logo}\n\nPredict the word by guessing all the correct letters\n")
print(f"{' '.join(word)}\n")
while end:
    letter = input("Guess a letter: ").lower()
    for i in range(length):
      if letter == choose_word[i]:
        word[i] = letter
    if '_' not in word:
      end = False
      print('you won')
    if letter not in choose_word:
      lives-=1
      print(f"\nOpps!!!, You guessed the wrong letter. You have {lives} lives remaining.")
      
      if lives == 0:
        end = False
        print("You lose")
        print("The word is: ",choose_word)
    else:
      print("\nGreat, You guessed the correct letter. Keep going.")
    print(f"{' '.join(word)}\n")
    
    print(hangman.stages[lives])

"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""
