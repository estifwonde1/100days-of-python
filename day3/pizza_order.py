print("Welcome to PythonPizza")
order = input("what kinda pizza do u want? 'S' , 'M' , 'L'")
bill = 0
if order == 'S':
    bill = 15
    print("The bill for Small is $15")
 
elif order == 'M':
    bill = 20
    print("The bill for Medium is $20")
elif order == 'L':
    bill = 25
    print("The bill for Large is $25")        
else:
    print("we don't serve that we only serve pizza s , m and l")
    exit()
add_on = input("would you like Pepperoni? Y or N")
cheese = input(" would you like extra cheese? Y or N")
if add_on == 'Y':
    if order == 'S':
        bill += 2  
    else:
        bill += 3
if cheese == 'Y':
    bill += 1

print(f"Thank you for choosing Python Pizza deliveries ir final bill is ${bill}")

