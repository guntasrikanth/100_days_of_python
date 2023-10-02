with open("Input/Names/invited_names.txt", mode='r') as file:
    name_list = file.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

for i in range(len(name_list)):
    name = name_list[i].strip()
    new = content.replace('[name]', name)
    #print(new)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w') as new_letter:
        new_letter.write(new)
