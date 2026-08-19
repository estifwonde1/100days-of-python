import string
letters = list(string.ascii_lowercase)

direction = input("welcome to the mysterious ceasercypher do u wanna encode or decode \n ").lower()
message = input("what is the word or message \n").lower()
shift = int(input("what is the shift number\n"))

def encode(message,shift):
    tar = list(message)
    m = shift
    for n in range(0,len(tar)-1):
        tar[n]=letters[m]
        m += shift
        print(tar)
encode(message,shift)






    
    
    


