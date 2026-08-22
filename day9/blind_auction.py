print ("welcome to the blind auction center")
name = input("what is ur name\n").lower()
bid = int(input("how much are u bidding for this masterpiece\n"))
another = input("is another person bidding\n").lower()
bid_list=[]
bid_list.append({name:bid})

while another == "yes":
    name = input("what is their name")
    bid = int(input("how much are u bidding for this masterpiece"))
    bid_list.append({name:bid})

print(bid_list)

