import string
letters = list(string.ascii_lowercase)


print (letters)
# word = list(input("enter the word u want to be cyphered by the magician \n").lower())

shift = int(input("by how much \n"))
n = 0


cyphered = []
def encode(shift):
    for m in range (0,len(letters),shift):
          print(letters[m])
        
        
    # print (word)
    

encode(shift)


    
    
    


