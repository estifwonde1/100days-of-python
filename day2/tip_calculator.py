print(" welcome to the tip calculator!")
total = input("what was the total bill? \n")
tip = input("how much tip would you like to give? 10% , 12% or 15 % ?")
split=input("how many ways do u wanna split the bill ?")

final = int(total) * int(tip)
this_time = int(final)/100
ultra = float(this_time) / int(split)

print (" Each person should pay: " + str(ultra))