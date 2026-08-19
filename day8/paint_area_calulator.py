import math
print("welcome to the paint are calculator")
height = int(input("enter the height\n"))
width = int(input("enter the width\n"))
coverage = int(input("enter the coverage\n"))

def area_calculator(height,width,coverage):
    total = (height*width)/coverage  
    print(f"the total cans needed would be {math.ceil(total)}")
area_calculator(height,width,coverage)