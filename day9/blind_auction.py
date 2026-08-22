print ("welcome to the blind auction center")
print (r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')



def auction():
    bid_list=[]
    bidding_open = True
    while bidding_open:
        name = input("what is ur name\n")
        bid = int(input("how much are they bidding for this masterpiece\n"))
        bid_list.append({
            "Name": name,
            "Bid": bid,
            })
        another = input("is another person bidding\n").lower()
        if another != "yes":
            bidding_open = False
    n = bid_list[0]["Bid"]
    m = bid_list[0]["Name"]
    for i in range (0,len(bid_list)):
        if n <= bid_list[i]["Bid"]:
            n = bid_list[i]["Bid"]
            m = bid_list[i]["Name"]
    print(f"and the winner is {m} who bid this crazy amount {n}")
auction ()


