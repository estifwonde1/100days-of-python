import random
print ("Welcome to The Number guessing game")
print("I am thinking of a number between 1 and 100")
tar = random.randint(1,100)
def guess_engine(n):
    while n > 0:
        print(f"you have {n} attempts guess the right number")
        guess = int(input("Make a guess: "))
        if guess < tar:
            print("too low")
        elif guess > tar:
            print("too high")
        else:
            print("congrats u win")
            break
        n -= 1
    if n == 0:
        print("womp womp u lost")

play = True
 
while play:
    level = input("Choose the level difficulty : easy or hard \n").lower()
    if level == "easy":
        guess_engine(10)
    elif level == "hard":
        guess_engine(5)
    else:
        print("yo dumb dumb choose either easy or hard ")
    prove = input("wann still play: yes or no\n")
    if prove != "yes":
        play = False




    
