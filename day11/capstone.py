import random
print(
    r'''	
		
 /$$       /$$                     /$$                               /$$      
| $$      | $$                    | $$                              | $$      
| $$$$$$$ | $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$
| $$__  $$| $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/
| $$  \ $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/ 
| $$  | $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$|  $$$$$$$| $$ \  $$
|_______/ |__/ \_______/ \_______/|__/  \__/| $$ \_______/ \_______/|__/  \__/
                                       /$$  | $$                              
                                      |  $$$$$$/                              
                                       \______/                               


    '''
)
def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def deal_card():
    card_numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    computer = [random.choice(card_numbers),random.choice(card_numbers)]
    player = [random.choice(card_numbers),random.choice(card_numbers)]
    
       
    print(computer[0])
    print(player)
    def show_score():
        print(player)
        print(computer)
    isgame_over = False
    while not isgame_over:
        player_score = calculate_score(player)
        if player_score >= 21:
            break
        deal = input("deal or stand \n").lower()
        if deal == "deal":
            player.append(random.choice(card_numbers))
            player_score = calculate_score(player)
            
            print(player)           
        else:
            isgame_over = True
    player_score = calculate_score(player)
    computer_score = calculate_score(computer)
    
    if player_score <= 21:
        while computer_score < 14:
            computer.append(random.choice(card_number))
    computer_score = calculate_score(computer)


    if player_score > 21:
        show_score()
        print("bust u went over 21")
    elif computer_score > 21:
        show_score()
        print("u win computer went over 21")
    elif player_score > computer_score:
        show_score()
        print(" u won")
    elif player_score < computer_score:
        show_score()      
        print(" u lost sucka")
    else:
        show_score()
        print("it's a draw")  
con = True
while con:
    deal_card()
    new = input("wanna play new game. yes or no\n").lower()
    if new != "yes":
        con = False
        

