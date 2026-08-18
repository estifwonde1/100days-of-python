import random
print("Hangman where ur mistake costs a little man's life")
word_list = [
    "apple", "banana", "cherry", "desktop", "elephant", 
    "forest", "guitar", "harbor", "island", "jacket", 
    "kitten", "lemon", "mountain", "needle", "ocean", 
    "python", "queen", "river", "shadow", "turtle"
]
victim = [
r'''
      _______
     |/      |
     |      
     |     
     |      
     |      
     |
    _|___
''',
r'''
      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___
''',
r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
''',
r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
''',
r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
''',
r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
''']
word = list(random.choice(word_list))
print(word)
splited = word.copy()
size = len(splited)
for i in range(0,size):
    splited[i] = "_"
print(splited)
print(word)
ha = list("hangman")
trial = 0
n = 0
while trial <= len(victim)-1:
    guess = input("guess a letter \n")
    if guess in word:
        for i in range(0,size):
            if word[i] == guess:
                splited[i] = guess
        print(splited)                          
    else:
        print(victim[n])
        n += 1
        trial +=1   
    if "_" not in splited:
        print ("u won")
        break
if trial == 6:
    print(" u hanged an innocent man")
   
            

                
