import random
print("Hangman where ur mistake costs a little man's life")
word_list = [
    "apple", "banana", "cherry", "desktop", "elephant", 
    "forest", "guitar", "harbor", "island", "jacket", 
    "kitten", "lemon", "mountain", "needle", "ocean", 
    "python", "queen", "river", "shadow", "turtle"
]
right = []
victim = r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
'''
word = list(random.choice(word_list))
print(word)
splited = word.copy()
size = len(splited)
for i in range(0,size):
    splited[i] = "_"
print(splited)
print(word)


ha = list("hangman")
so = len(ha)

guess = input("guess a letter \n")
n = 0
if guess in word:
    for i in range(0,size):
        if word[i] == guess:
            splited[i] = guess
else:
    right.append(ha[n])
    n += 1
    print(right)
        

                
            
    
      
print(splited)
