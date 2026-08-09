print("welcome to the BMI calculator")
height = float(input("please enter ur height(cm)"))
weight = float(input("please enter ur weight"))
n = height * height
bmi = float(weight / n)
if bmi < 18.5:
    print("u are under weight eat more")
elif bmi > 18.5 and bmi < 25:
    print("u are normal height , good job")
elif bmi > 25 and bmi < 30:
    print (" u are slightly over weight , better start to exercise")
elif bmi > 30 and bmi < 35:
    print(" u are obese might suggest to start work out seriously")
else:
    print ("u are clinically obese u need help")