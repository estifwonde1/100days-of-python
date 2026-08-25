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

def deal_card():
    card_numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    computer = []
    player = []
    n = 0
    player_total = 0
    computer_total = 0
    m = 2
    while n < 2:         
        computer.append(random.choice(card_numbers))
        player.append(random.choice(card_numbers))
        player_total += player[n] 
        computer_total += computer[n] 
        n += 1


    if 11 in player and player_total > 21:
        player.remove(11)
        player.append(1)
        print(player)
    if 11 in computer and computer_total > 21:
        computer.remove(11)
        computer.append(1)
        print(computer) 
        
    print(computer[0])
    print(player)
    deal = input("deal or stand\n").lower()
    while deal == "deal":  
              
        if player_total > 21:
            print ("bust u lost")
            print(player)
            print(player_total)
            break
            
        else:
            player.append(random.choice(card_numbers))
            print(player)
            player_total += player[m]
            if player_total > 21:
                print("bust")
                break   
            deal = input("deal or stand\n").lower()            
            m += 1
        
    if deal == "stand":
        while computer_total <= 14:
            computer.append(random.choice(card_numbers))
            computer_total += computer[n]
            n += 1
            if computer_total >21:
                break


        print(computer)
        print(player)
    if player_total > computer_total and player_total <= 21:
        print(computer)
        print ("u won")
    elif player_total < computer_total and computer_total <= 21:
        print("u lost")
    elif player_total < computer_total:
        print("u won")
    elif player_total == computer_total:
        print ("draw")
   

   


    
deal_card()

