print("welcome to the leap year calculator")
leap = int(input("please enter the year? "))
if leap % 4 == 0:
    if leap % 100 == 0:
        if leap % 400 == 0:
            print("The year "+ str(leap) + " is a leap year")
        else:
            print("not a leap year")
    else:
        print("The year "+ str(leap) + " is a leap year")
else:
    print ("not a leap year")