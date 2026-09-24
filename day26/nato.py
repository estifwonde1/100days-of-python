import pandas as pd

data=pd.read_csv("nato_phonetic_alphabet.csv")

new_dict ={row.Letter:row.Code for (index,row) in data.iterrows()}
print(new_dict)

word = input("enter a word: ").upper()
print(word)

coded = [new_dict[letter] for letter in word]

print(coded)
