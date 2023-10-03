import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

name = input("Enter any word: ")

letter_list = [letter.upper() for letter in name]
nato_list = [nato_dict.get(char) for char in letter_list if char in nato_dict.keys()]
print(nato_list)
