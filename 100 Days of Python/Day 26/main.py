import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for index,row in df.iterrows()}
print(nato)

input = input("Enter a word: ").upper()

splitted = [nato[letter] for letter in input]

print(splitted)

