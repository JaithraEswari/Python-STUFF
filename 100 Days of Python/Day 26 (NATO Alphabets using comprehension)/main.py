import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for index,row in df.iterrows()}
# print(nato)

is_on = True
while is_on:
    word = input("Enter a word: ").upper() 
    try: 
        splitted = [nato[letter] for letter in word]
        print(splitted)
        is_on = False
    except KeyError:
        print("Please enter a valid word")







