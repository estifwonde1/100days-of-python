print(r'''		
 dP""b8  dP"Yb  888888 888888 888888 888888   8b    d8    db     dP""b8 88  88 88 88b 88 888888 
dP   `" dP   Yb 88__   88__   88__   88__     88b  d88   dPYb   dP   `" 88  88 88 88Yb88 88__   
Yb      Yb   dP 88""   88""   88""   88""     88YbdP88  dP__Yb  Yb      888888 88 88 Y88 88""   
 YboodP  YbodP  88     88     888888 888888   88 YY 88 dP""""Yb  YboodP 88  88 88 88  Y8 888888 
''')


water = 1000
milk = 1000
Coffee = 1000
Money = 0
print(f"water:{water}\nmilk:{milk}\ncoffee:{Coffee}\nMoney:{Money}")

 
currency_value = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickel": 0.5,
    "penny":0.01,
}          
price_tag ={
    "espresso" : 2.42,
    "latte" : 4.50,
    "cappuccino" : 5.40
}
def process_coin(quarter,dime,nickel,penny):
    paid = (currency_value["quarter"] * quarter)+(currency_value["dime"]+ dime) + (currency_value["nickel"] * nickel) + (currency_value["penny"] + penny)
    return paid
def not_sufficent():
    if water < 200:
        print("not sufficent supply")
    if milk < 100:
        print("not sufficient supply")
    if Coffee < 100:
        print("not sufficent supply")

def make_latte():
    global water
    global milk
    global Coffee
    global Money
    while not not_sufficent():
        water -= 200
        milk -= 50
        Coffee -= 24
        Money += 2.42
        print ("here is ur latte")
        break
def make_espresso():
    global water
    global Coffee
    global Money
    while not not_sufficent():
        water -= 100
        Coffee -= 15
        Money += 4.50
        print ("here is ur espresso")
        break
def make_cappucino():
    global water
    global milk
    global Coffee
    global Money
    while not not_sufficent():
        water -= 36 
        milk -= 100
        Coffee -= 18
        Money += 5.40
        print ("here is ur cappuccino")
        break
def refill():
    global water
    global milk
    global Coffee
    water += 300
    milk += 100
    Coffee += 100
    
def report():
    print(f"water: {water}\nmilk:{milk}\ncoffee:{Coffee}\nMoney:{Money}")

order =input("what would you like? (espresso/latte/cappuccino)\n")
if order == "report":
    report()
elif order == "refill":
    refill()

print("please insert coins:")
quarter = int(input("How many quartes: "))
dime = int(input("How many dimes: "))
nickel = int(input("how many nickel: "))
penny =int(input("how many pennies: "))
while order == "espresso":
    if price_tag["espresso"] == process_coin(quarter,dime,nickel,penny):
        make_espresso() 
        break
    elif price_tag["espresso"] < process_coin(quarter,dime,nickel,penny):
        make_espresso()
        change = process_coin(quarter,dime,nickel,penny)-price_tag["espresso"] 
        print(f"and here is ur change {change}")
        break
    else:
        print("not enough coins")
        break
while order == "latte":
    if price_tag["latte"] == process_coin(quarter,dime,nickel,penny):
        make_latte()
        break
    elif price_tag["latte"] < process_coin(quarter,dime,nickel,penny):
        make_latte()
        change = process_coin(quarter,dime,nickel,penny)-price_tag["latte"]
        print(f" and here is ur change {change}")
        break
    else:
        print("not enough coins")
        break
while order == "cappuccino":
    if price_tag["cappuccino"] == process_coin(quarter,dime,nickel,penny):
        make_latte()
        break
    elif price_tag["cappuccino"] < process_coin(quarter,dime,nickel,penny):
        make_latte()
        change = process_coin(quarter,dime,nickel,penny) - price_tag["cappuccino"]
        break
    else:
        print("not enough coins")
        break




#am in progress am understanding the jist of it

        

    