print("welcome to the leap year calculator")
leap = int(input("please enter the year? "))
four = int(leap % 4)
hun = int(leap % 100)
f_hun=int(leap % 400)
if four == 0:
    if hun == 0:
        if f_hun == 0:
            print("The year "+ str(leap) + " is a leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print ("not a leap year")