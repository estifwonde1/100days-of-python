import random
print("Hangman where ur mistake costs a little man's life")
word_list = [
    "apple", "banana", "cherry", "desktop", "elephant", 
    "forest", "guitar", "harbor", "island", "jacket", 
    "kitten", "lemon", "mountain", "needle", "ocean", 
    "python", "queen", "river", "shadow", "turtle"
]
right = []
vitim = r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
'''
word = "elephant"
splited = list(word)
print(splited)

guess = input("guess a letter \n")

for letter in splited:
    if guess == letter:
        right.append(guess)
        print(right)
