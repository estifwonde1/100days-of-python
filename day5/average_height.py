print("welcome to the average height calulator")
students_height = []
add = "yes"

while add == "yes":
    n = int(input("add the the height of ur students"))
    add = input("wanna add more yes or no").lower()
    students_height.append(n)

summing = 0
for student in students_height:
    summing += int(student)
    le = len(students_height)
    av = summing/le
print (av)