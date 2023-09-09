from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text,shift,direction):
  message = ''
  for c in range(len(text)):
    if text[c].isalpha():
      index = alphabet.index(text[c])
      if direction == 'encode':
        message+=alphabet[index+shift]
      else:
        message+=alphabet[index-shift]
    else:
      message+=text[c]
  print(f"The {direction}d text is {message}\n")

print(logo)
info = 'yes'
while info=='yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caeser(text,shift,direction)
  info = input("Type \'yes\' if you want to go again. Otherwise type \'no\'\n").lower()

print("Good Bye!!")