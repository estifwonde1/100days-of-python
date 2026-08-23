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
def add(num1,num2):
    return num1 + num2
def substract(num1,num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide (num1,num2):
    if num2 == 0:
        return "cannot devide by 0"
    return num1 / num2

operator = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}
def calculator():
    num1 = float(input("enter the first number \n"))  
    con = True
    for symbol in operator:
        print (symbol)
    while con:
        opa = (input("pick an operation"))
        num2 = float(input("enter the second number\n"))      
        sol = operator[opa]
        ans = sol(num1,num2)
        print (ans)
        que =input("wanna continue from total value or want new : yes or no\n").lower()
        if que == "yes":
            num1 = ans
        else :
            con = False
            calculator()
    
      
calculator()




