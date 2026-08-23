print(r'''
                      88                        88                     
                      88                        88              ,d     
                      88                        88              88     
 ,adPPYba, ,adPPYYba, 88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM  ,adPPYba,  8b,dPPYba,  
a8"     "" ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88     a8"     "8a 88P'   "Y8  
8b         ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88     8b       d8 88   
"8a,   ,aa 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,    "8a,   ,a8" 88
 `"Ybbd8"' `"8bbdP"Y8 88  `"Ybbd8"'  `"YbbdP'Y8 88 `"8bbdP"Y8   "Y888  `"YbbdP"'  88      
''')
print(r'''
 _____________________
|  _________________  | 
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

''')
def calculator():
    con = True
    while con:
        num1 = float(input("enter the first number \n"))
        operator = (input("+\n-\n*\n/\n"))
        num2 = float(input("enter the second number\n"))
        if operator == "+":
            total = num1 + num2
            print(f"the value is {total}")
        elif operator == "-":
            total = num1 - num2
            print(f"the value is {total}")
        elif operator == "*":
            total = num1 * num2
            print(f"the value is {total}")
        elif operator == "/":
            total = num1 / num2
            print(f"the value is {total}")
        else:
            print("invalid input")
        que =input("wanna continue from total value or want new : yes or no\n").lower()
        if que != "yes":
            con = False
        else:
            while que == "yes":
                operator =(input("+\n-\n*\n/\n"))
                num2 =float(input("enter the second number\n"))
                if operator == "+":
                    total = total + num2
                    print (f"the value is {total}")
                elif operator == "-":
                    total = total - num2
                    print(f"the value is {total}")
                elif operator == "*":
                    total = total * num2
                    print(f"the value is {total}")
                elif operator == "/":
                    total = total / num2
                    print(f"the value is {total}")
                else:
                    print("invalid input")
                que =input("wanna continue from total value or want new : yes or no\n").lower()
            if que != "yes":
                con = False
            



calculator()




