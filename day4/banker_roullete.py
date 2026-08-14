import random
print("Welcome to the banker roullete")

names = []
name = input("enter the names \n").lower()
con = input("wanna add more . YES or NO").lower()
names.append(name)

while con == "yes":
    name = input("enter the names \n").lower()
    names.append(name)
    con = input("wanna add more . YES or NO").lower()
print(names)
payer = random.choice(name)
print (f" and thepayer is drum roll please{payer}")
