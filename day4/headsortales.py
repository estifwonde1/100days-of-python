import random

print(" welcome to heads or tales")

choices = ("heads","tales")
user =input("choose heads or tales and meer ur fate \n").lower()
comp = random.choice(choices)

if user == comp:
    print(comp)
    print("congrats u win")
else:
    print(comp)
    print("hahahahahahaha u lose sucka")