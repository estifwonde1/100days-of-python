import string
print(r'''
 ______  ______  ______  ______  ______  ______
 / ____/ / ____/ / ____/ / ____/ / ____/ / __  \
/ /     / /___  / /___  / /___  / /___  / /_/ /
| |    / ___/  / __/   |  __|  / __/  |  _  <
\ \___/ /____ / /___   _\ \   / /____ / / \ \
 \____/______/______/ /____/ /______/_/   \_\

  ______  __   __  ______  __   __  ______  ______
 / ____/ \ \ / / / ___  / \ \ / / / ____/ / __  \
/ /       \ V /  / /__/ /  \ V / / /___  / /_/ /
| |        | |  |  ____/    | | |  __|  |  _  <
\ \___     | |  | |         | | / /____ / / \ \
 \____/    |_|  |_|         |_|/______/_/   \_\

              -=[by the estifanos wondwossen]=-

                
''')
letters = list(string.ascii_lowercase)

direction = input("welcome to the mysterious ceasercypher do u wanna encode or decode \n ").lower()

def encode(message,shift):
    tar = list(message)
    for n in range(len(tar)):
        current = tar[n]
        if current in letters:
            current_index = letters.index(current)

            new_index = (current_index + shift) % 26

            tar[n] = letters[new_index]

    print(f"the encoded mysterious word is {"".join(tar)}")
def decode(message,shift):
    tar = list(message)
    for n in range(len(tar)):
        current=tar[n]
        if current in letters:
            current_index = letters.index(current)
            new_index = abs((current_index - shift) % 26)
            tar[n] = letters[new_index]
    print(f" the mysterious decoded term is {"".join(tar)}")
    

if direction  == "encode":
    message = input("what is the word or message \n").lower()
    encode(message,shift)
    shift = int(input("what is the shift number\n"))
elif direction  == "decode":
    message = input("what is the word or message \n").lower()
    shift = int(input("what is the shift number\n"))
    decode(message,shift)
else:
    print ("dummy choose either decode or encode")






    
    
    


