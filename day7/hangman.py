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
guess = input("guess a letter \n")
trial = 0
n = 0
while trial <= 6:
    guess = input("guess a letter \n")
    if guess in word:
        for i in range(0,size):
            if word[i] == guess:
                splited[i] = guess
                print(splited)                          
    else:
        right.append(ha[n])
        n += 1
        trial +=1
        print(right)
   
    if "_" not in splited:
        print ("u won")
        break
    if trial == 7:
        print(" u hanged an innocent man")
        print(victim)
            

                
