print(r'''		
 dP""b8  dP"Yb  888888 888888 888888 888888   8b    d8    db     dP""b8 88  88 88 88b 88 888888 
dP   `" dP   Yb 88__   88__   88__   88__     88b  d88   dPYb   dP   `" 88  88 88 88Yb88 88__   
Yb      Yb   dP 88""   88""   88""   88""     88YbdP88  dP__Yb  Yb      888888 88 88 Y88 88""   
 YboodP  YbodP  88     88     888888 888888   88 YY 88 dP""""Yb  YboodP 88  88 88 88  Y8 888888 
''')
order =input("what would you like? (espresso/latte/cappuciono)\n")

def store():
    water = 300
    milk = 200
    Coffee = 100
    print(f"water:{water}\nmilk:{milk}\ncoffee:{Coffee}")

 
currency_value = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickel": 0.5,
    "penny":0.01,
}
  
    
    

def make_espresso():
    print("the price is $2.42\n")
    print("please insert coints:\n")
    bill = 2.42
    tar = 0
    quarter = float(input("please insert quarters: "))
    dime = float(input("please insert dime:  "))
    nickel = float(input("please insert quarter: "))
    penny = float(input("please insert penny: "))
    change = float(quarter + dime + nickel + penny)
    for q in range (quarter):
        tar += currency_value["quarter"]

    print(f"here is ur expresso and ur change {change} \n have a great day")

#done for today am stopping at solving the conversion i will continue tommorrow 
        

    