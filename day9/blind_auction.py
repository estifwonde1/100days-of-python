print ("welcome to the blind auction center")
name = input("what is ur name").lower()
bid = int(input("how much are u bidding for this masterpiece"))
another = input("is another person bidding").lower()
bid_list=[]

while another == "yes":
    name = input("what is their name")
    bid = int(input("how much are u bidding for this masterpiece"))
    bid_list.append({name:bid})

