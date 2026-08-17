import random
import string
print ("welcome to the number generator")
letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list(string.punctuation)
print(special_characters)
password = []
lett = int(input("how many letters do u want to have \n"))
num = int(input("how many numbers do u want to have \n"))
spec_char=int(input("how many characters do u want it have\n"))
for n in range (0,lett):
    password.append(random.choice(letters))
for m in range (0,num):
    password.append(random.choice(numbers))
for o in range(0,spec_char):
    password.append(random.choice(special_characters))
random.shuffle(password)
finalpassword = "".join(password)
print(f"ur new secure and impossipble to crack password is gonna be '{finalpassword}'")